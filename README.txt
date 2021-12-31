# Pro7-Media-Sweeper
Find and sweep media files that are not being used by ProPresenter7

Description:
This script will find and sweep out all files of a selected folder that ProPresenter7 does not use in any playlist, library presentation document, prop, stage display, or mask.
All swept files are moved into a new directory where they can be reviewed, restored, and/or deleted.

Usage:
User can choose which folder to sweep.  The default folder location is ProPresenter's 'Media' folder (location set in Pro7's Support Files setting in advanced preferences).  This is ProPresenter7’s default media folder when the “Manage Media Automatically” option is checked.
Select whether subdirectories under the chosen folder to sweep should be included.  Including subdirectories will recursively clean all files in the selected directory and any subdirectories within the chosen directory.  This option is checked by default.
Click the 'Sweep Media Files!' button to start the process of sweeping all unused files.  A log file will be generated and all unused media files will be moved to a folder in ~/Documents/Pro7 Media Sweeper/
WARNING!  ANY file in the chosen directory that is not used in any ProPresenter7 playlist, *.pro document, prop, stage display, or mask _WILL_ be moved to a new location where they can be reviewed and deleted.  This applies to all files and file types!  More than just media files may be moved if other files also exist in the chosen folder.

How it works:
1. The script first builds a list of all referenced files in your ProPresenter installation.  The ProPresetner files are decoded using reverse engineered Google Protocol Buffer files from Dan Owen, which can be found here: https://github.com/greyshirtguy/ProPresenter7-Proto (THANKS DAN!).
4. Every file in the chosen folder is compared to the list of file paths from the decoded ProPresenter files.  Any file that is not found to be used in the decoded ProPresenter files is moved to a new folder in '~/Documents/Pro7 Media Sweeper/'.  The relative folder structure is maintained to eliminate any duplicate filename collisions and make it easy to restore the swept files manually with cut/copy/past in your file browser of choice (Windows Explorer or MacOS Finder).
5. Swept Files can be reviewed and deleted without affecting any ProPresenter presentations or playlists.
