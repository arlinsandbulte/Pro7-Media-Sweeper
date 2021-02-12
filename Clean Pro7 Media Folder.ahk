#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

MsgBox, 4, , This Script will move ALL files from ProPresenter's Media folder if they are not referenced in any presentation or playlist.  Do you want to continue?
IfMsgBox No
    return

; Get the path for the current user's home directory and stores it in vUserProfile
EnvGet, vUserProfile, USERPROFILE

; Initialize list of file reference strings
FileRefArray :=[]

; Set directory locations
PresentationLocation = %vuserProfile%\Documents\ProPresenter\Libraries
PlaylistLocation = %vuserProfile%\Documents\ProPresenter\Playlists
MediaLocation = %vuserProfile%\Documents\ProPresenter\Media

; Find all presentation files with a *.pro filename
; Then parse each .pro file, extract all file paths, and save path strings into FileRefArray[]
Loop Files, %PresentationLocation%\*.pro, R  ; Recurse into subfolders.
{
	Loop, read, % A_LoopFileFullPath
	{
		If RegExMatch(A_LoopReadLine, "[A-z]:(\\.*\.([A-z|0-9]*))" , FilePath)
		{
			; debug MsgBox, Found ref path %FilePath%
			FileRefArray.Push(FilePath)
		}
	}
}

; Find all playlist files
; Then parse each playlist file, extract all file paths, and save path strings into FileRefArray[]
Loop Files, %PlaylistLocation%\*, R  ; Recurse into subfolders.
{
	Loop, read, % A_LoopFileFullPath
	{
		If RegExMatch(A_LoopReadLine, "[A-z]:(\\.*\.([A-z|0-9]*))" , FilePath)
		{
			; debug MsgBox, Found ref path %FilePath%
			FileRefArray.Push(FilePath)
		}
	}
}

; Check all files in the Media folder.
; If the file is not referenced in any .pro presentation file or any playlist, move it to the script directory!
FileCreateDir, Moved
Loop Files, %MediaLocation%\*, R
{
	RefsFound := 0
	FileIndex := A_Index
    Loop % FileRefArray.MaxIndex()
	{
		StringLower, refPathLower, % FileRefArray[A_Index]
		StringLower, filePathLower, A_LoopFileFullPath
		RefsFound := RefsFound + (refPathLower = filePathLower)
	}
	; debug MsgBox, %A_LoopFileFullPath% %RefsFound% references
	If % RefsFound = 0
	{
		FileMove, %A_LoopFileFullPath%, %A_ScriptDir%\Moved
		; FileDelete, %A_LoopFileFullPath%
	}
	
}