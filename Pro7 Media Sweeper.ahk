#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


MsgBox, 4, , WARNING!`n`nThis Script will move *ALL* files in the chosen directory if they are not referenced in any presentation or playlist.`n`nContinue?
IfMsgBox No
    Exit

; Get the path for the current user's home directory and stores it in vUserProfile
EnvGet, vUserProfile, USERPROFILE

; Set Regex search strings to find Full file reference paths & Relative file reference paths
FullRefRegex = (?<=[A-Z])[A-Z]:\\.*\.([0-9]|[a-z]|[A-Z])*(?=")
RelRefRegex = (?<=.).*\.([0-9]|[a-z]|[A-Z])*(?=)

; Initialize list of file reference strings
FileFullRefArray :=[]
FileRelRefArray :=[]

; Set default directory locations
Pro7AppDataLocatoin = %vuserProfile%\AppData\Roaming\RenewedVision\ProPresenter
PresentationLocation = %vuserProfile%\Documents\ProPresenter\Libraries
PlaylistLocation = %vuserProfile%\Documents\ProPresenter\Playlists
MediaLocation = %vuserProfile%\Documents\ProPresenter\Media

; Find ProPresenter's Support Files location setting
; If the Support Files location is different than default, modify directory locations accordingly
Loop, read, %Pro7AppDataLocatoin%\PathSettings.proPaths
{
	If RegExMatch(A_LoopReadLine,"(?<=Base=).*(?=\\\\;)",Pro7SupportFilePath)
	{
		Pro7SupportFilePath := StrReplace(Pro7SupportFilePath,"\\","\")
		PresentationLocation = %Pro7SupportFilePath%\Libraries
		PlaylistLocation = %Pro7SupportFilePath%\Playlists
		MediaLocation = %Pro7SupportFilePath%\Media
	}
}

; Let user choose Media folder to sweep.  Defaults to ProPresenter's Auto-Managed Media folder
FileSelectFolder, OutputVar, *%MediaLocation%, 0, Choose Media Folder to clean`n(Default is Pro7's Media folder)
if OutputVar =
{
    MsgBox, You didn't select a folder.  `nScript will terminate.
	Exit
}
else
{
	MediaLocation = %OutputVar%
}

; Let user choose whether to recurse subdirectories
MsgBox, 3, Recurse, Include Subdirectories?,
IfMsgBox Yes
    recurse = R
else ifMsgBox No
    recurse = 
else
	Exit

SplashTextOn , , , WORKING, WORKING

; Find all presentation files with a *.pro filename
; Then parse each .pro file, extract all file paths, and save path strings into FileFullRefArray[] & FileRelRefArray[]
Loop Files, %PresentationLocation%\*.pro, R  ; Recurse into subfolders.
{
	Loop, read, % A_LoopFileFullPath
	{
		If RegExMatch(A_LoopReadLine, FullRefRegex , FilePath)
		{
			FilePath := StrReplace(FilePath, "/" , "\")
			FileFullRefArray.Push(FilePath)
		}
		If RegExMatch(A_LoopReadLine, RelRefRegex , FilePath)
		{
			FilePath := StrReplace(FilePath, "/" , "\")
			FileRelRefArray.Push(FilePath)
		}
	}
}

; Find all playlist files
; Then parse each playlist file, extract all file paths, and save path strings into FileFullRefArray[] & FileRelRefArray[]
Loop Files, %PlaylistLocation%\*, R  ; Recurse into subfolders.
{
	Loop, read, % A_LoopFileFullPath
	{
		If RegExMatch(A_LoopReadLine, FullRefRegex , FilePath)
		{
			FilePath := StrReplace(FilePath, "/" , "\")
			FileFullRefArray.Push(FilePath)
		}
		If RegExMatch(A_LoopReadLine, RelRefRegex , FilePath)
		{
			FilePath := StrReplace(FilePath, "/" , "\")
			FileRelRefArray.Push(FilePath)
		}
	}
}

; Check all files in the Media folder.
; If the file is not referenced in any .pro presentation file or any playlist, move it to the script directory!
; Moved files retain the original directory structure
MoveCount := 0
MoveErrors := 0
Loop Files, %MediaLocation%\*, %recurse%
{
	FullRefsFound := 0
    Loop % FileFullRefArray.MaxIndex()
	{
		FullRefsFound := FullRefsFound + (InStr(A_LoopFileFullPath, FileFullRefArray[A_Index]) > 0)
	}
	
	If % FullRefsFound = 0
	{
		RelRefsFound := 0
		Loop % FileRelRefArray.MaxIndex()
		{
			RelRefsFound := RelRefsFound + (InStr(A_LoopFileFullPath, FileRelRefArray[A_Index]) > 0)
		}
	}
	
	If % FullRefsFound + RelRefsFound = 0 ;no references found for this file.  Move it!
	{
		MoveLocation := SubStr(A_LoopFileFullPath, StrLen(MediaLocation)+2)
		SplitPath, A_LoopFileFullPath , , FileDir, , , 
		MovePath := SubStr(FileDir, StrLen(MediaLocation)+2)
		FileCreateDir, Swept Files\%MovePath%
		FileMove, %A_LoopFileFullPath%, %A_ScriptDir%\Swept Files\%MoveLocation%
		If ErrorLevel = 0
		{
			MoveCount := MoveCount + 1
		}
		Else
		{
			MoveErrors := MoveErrors + 1
		}
	}
}

SplashTextOff

MsgBox, Done!`n`nFound %MoveCount% unreferenced files and moved them to:`n%A_ScriptDir%\Swept Files\`n`n%MoveErrors% Errors
