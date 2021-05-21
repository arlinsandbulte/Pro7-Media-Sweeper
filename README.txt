# Pro7-Media-Sweeper
Find and clean media files that are not being used by ProPresenter7

Description:
This script will find and clean out all files of a selected folder that ProPresenter7 does not reference in any playlist or library presentation document.
All cleaned files are moved into a new directory to review.

Usage:
The user is prompted to choose a folder to clean.  The default folder location is ProPresenter's 'Media' folder (location set in Pro7's Support Files setting in advanced preferences).  This is ProPresenter7’s default media folder when the “Manage Media Automatically” option is checked.
User is prompted to choose to include subdirectories (Yes/No/Cancel).  Including subdirectories will recursively clean all files in the selected directory and any subdirectories within the chosen directory.
WARNING!  ANY file in the chosen directory that is not referenced in any ProPresenter7 playlist or *.pro document will be moved to a new location where they can be reviewed and deleted.  This applies to all files and file types!  More than just media files may be moved if other files also exist in the chosen folder.

How it works:
1. The script first builds a list of all referenced files in your ProPresenter installation.
2. Every *.pro file in your ProPresenter 'Libraries' folder is parsed (That folder location is set in Pro7's Support Files setting in advanced preferences).  It searches each line of every *.pro file and looks for a file path.  If a file path is found, that file path is added to a list.
3. Then, it parses every file in your ProPresenter Playlists folder.  It searches each line of every file (playlist files don’t have an extension) and looks for a file path string.  If it finds a file path string, it is added to the list of file paths.
4. Every file in the chosen folder is compared to the list of file paths.  Any file not also found in the list is moved to a new folder in the same directory as the script called Swept Files.
5. Swept Files can be reviewed and deleted without affecting any ProPresenter presentations or playlists.

The following regex is used to find and extract all full file paths from the playlist files and *.pro presentation document files:
FullRefRegex = (?<=[A-Z])[A-Z]:\\.*\.([0-9]|[a-z]|[A-Z])*(?=")
RelRefRegex = (?<=.).*\.([0-9]|[a-z]|[A-Z])*(?=)

This regex may not be perfect in finding all referenced file paths in the playlist and *.pro files.
False positives (extracting a string of characters that are not actually a file path) are not a problem because there won’t be a corresponding real file that can be moved.
False negatives (failing to recognize a valid path and not including it in the list of referenced paths) could cause a problem because files could be moved even when they are referenced and used in ProPresenter.
