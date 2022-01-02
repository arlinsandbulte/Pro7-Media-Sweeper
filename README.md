# Pro7-Media-Sweeper
Find and sweep media files that are not being used by ProPresenter7

## Description:
This utility will find and sweep out all files of a selected folder that ProPresenter7 does not use in any playlist, library presentation document, prop, stage display, or mask.
All swept files are moved into a new directory where they can be reviewed, restored, and/or deleted.

## Usage:
1. User can choose which folder to sweep.  The default folder location is ProPresenter's 'Media' folder (location set in Pro7's Support Files setting in advanced preferences).  This is ProPresenter7’s default media storage folder when the “Manage Media Automatically” option is checked in ProPresenter7's Advanced Preferences.
2. Select whether subdirectories should be included.  Including subdirectories will recursively clean all files in the selected directory and any subdirectories within the chosen directory.  This option is checked by default.
3. Click the 'Sweep Media Files!' button to start the process of sweeping all unused files.  A log file will be generated and all unused media files will be moved to a folder in '~/Documents/Pro7 Media Sweeper/'  

**WARNING!**  ANY AND ALL files in the chosen sweep directory that are not used in any ProPresenter7 playlist, *.pro document, prop, stage display, or mask _WILL_ be moved to a new location where they can be reviewed and deleted.  This applies to all files and file types!  More than just media files may be moved if other files also exist in the chosen folder.

## How it works:
1. The utility first builds a list of all referenced files in your ProPresenter installation.  
ProPresetner files are decoded using reverse engineered Google Protocol Buffer files from Dan Owen, which can be found [here: https://github.com/greyshirtguy/ProPresenter7-Proto](https://github.com/greyshirtguy/ProPresenter7-Proto) (THANKS DAN!).
   - Find media reference path strings in all *.pro files.  
     The *.pro files are all stored in the 'Libraries' folder ('~/ProPresenter/Libraries/' by default).
   - Find media reference path strings in all Playlists.  
     Playlist files are all stored in one location ('~/ProPresenter/Playlists/' by default).
   - Find media reference path strings in Props.  
     Props config data is stored in the Props config file ('~/ProPresenter/Configuration/Props' by default).
   - Find media reference path strings in Masks.
     Masks config data is stored in the Workspace config file ('~/ProPresenter/Configuration/Workspace' by default).
   - Find media reference path strings in Stage displays.  
     Stage config data is stored in the Stage config file ('~/ProPresenter/Configuration/Stage' by default).
2. The full path string of every 'real' file in the chosen media folder to sweep is compared all of the file path strings from the ProPresenter files.  Any 'real' file that is not found to be referenced in ProPresenter is moved to a new folder at '~/Documents/Pro7 Media Sweeper/' (except a few key system files & hidden files).  The relative folder structure is maintained to eliminate any duplicate filename collisions and make it easy to restore the swept files manually with cut/copy/paste in your file browser of choice (Windows Explorer or MacOS Finder or other).
3. The Swept Files can be reviewed and/or deleted without affecting the integrity of any ProPresenter presentations or playlists.
