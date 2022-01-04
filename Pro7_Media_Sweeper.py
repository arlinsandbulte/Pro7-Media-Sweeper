import tkinter as tk
import platform
import plistlib
import os
import shutil
import re
from urllib.parse import unquote
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox
# from tkinter import PhotoImage
from pathlib import Path
import presentation_pb2  # Used to decode *.pro files
import propresenter_pb2  # Used to decode PlayList files, which do not have an extension
import propDocument_pb2  # Used to decode Props configuration file, which does not have an extension
import proworkspace_pb2  # Used to decode Workspace configuration file, which contains Mask info
import stage_pb2  # Used to decode Stage configuration file.


# This function pops up a folder picking dialog and sets the path in the text entry box.
def pick_media_folder():
    open_folder = filedialog.askdirectory(initialdir=path_entry.get())  # Returns opened path as str
    if open_folder != "":  # if folder dialog was not cancelled
        open_folder = Path(open_folder)
        path_entry.delete(0, tk.END)
        path_entry.insert(0, open_folder.__str__())


# This function does all the work of sweeping the chosen media folder
def sweep_the_folder():

    # Save timestamp of when sweep was performed.  Used later in log and moved files folder.
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    # Set folder path locations
    sweep_folder_location = Path.expanduser(Path(path_entry.get()))
    presentation_location = Path.expanduser(pro7_support_file_path) / "Libraries"
    playlist_location = Path.expanduser(pro7_support_file_path) / "Playlists"
    configuration_location = Path.expanduser(pro7_support_file_path) / "Configuration"

    if not os.path.exists(sweep_folder_location):
        msg = sweep_folder_location.__str__() + "\ndoes not exist!"
        title = "ERROR! Sweep Folder not Found!"
        tk.messagebox.showerror(title=title, message=msg)
        return

    #  Set Button Status indication
    btn_sweep_files.config(text="Working..........", state="disabled", relief="sunken")
    window.update()

    # Find all files in the chosen Media Location.
    # TODO: This is not very efficient if include subdirectories is not checked.
    media_files = []
    for subdir, dirs, files in os.walk(sweep_folder_location):
        for filename in files:
            if cb.get() == 0 and subdir.upper == sweep_folder_location.__str__().upper:
                # Include subdirectories is not checked.  Only add files in the root folder to media_files list
                filepath = subdir + os.sep + filename
                media_files.append(filepath)
            elif cb.get() == 1:
                # Include subdirectories is checked.  Add all files to media_files list
                filepath = subdir + os.sep + filename
                media_files.append(filepath)

    # Remove system files etc. from the media_files list, so they don't get swept.
    media_files = [s for s in media_files if Path(s).name[0] != "."]  # remove hidden files that start with "."

    # Define regex patterns to find media reference strings in ProPresenter files
    absolute_ref_regex = r"(?<= absolute_string: \").*(?=\")"
    relative_ref_regex = r"(?<= relative_path: \").*(?=\")"
    path_ref_regex = r"(?<= path: \").*(?=\")"

    # Initialize media file reference lists
    absolute_ref_list = []
    relative_ref_list = []
    path_ref_list = []

    # Find all media file references in .pro presentation files
    for subdir, dirs, files in os.walk(presentation_location):
        for filename in files:
            filepath = Path(subdir) / Path(filename)
            if (filepath.__str__()[-4:]) == ".pro":
                pro7pres = presentation_pb2.Presentation()
                file1 = open(filepath, mode='rb')
                pro7pres.ParseFromString(file1.read())
                file1.close()
                absolute_ref_list.extend(re.findall(absolute_ref_regex, pro7pres.__str__()))
                relative_ref_list.extend(re.findall(relative_ref_regex, pro7pres.__str__()))
                path_ref_list.extend(re.findall(path_ref_regex, pro7pres.__str__()))

    # Find all media file references in PlayList files
    for subdir, dirs, files in os.walk(playlist_location):
        for filename in files:
            filepath = Path(subdir) / Path(filename)
            pro7playlist = propresenter_pb2.PlaylistDocument()
            file2 = open(filepath, mode='rb')
            pro7playlist.ParseFromString(file2.read())
            file2.close()
            absolute_ref_list.extend(re.findall(absolute_ref_regex, pro7playlist.__str__()))
            relative_ref_list.extend(re.findall(relative_ref_regex, pro7playlist.__str__()))
            path_ref_list.extend(re.findall(path_ref_regex, pro7playlist.__str__()))

    # Find all media file references in Props config file
    # Find all media file references in Masks (Workspace config file)
    # Find all media file references in Stage config file
    for subdir, dirs, files in os.walk(configuration_location):
        for filename in files:
            if filename == "Props":
                filepath = Path(subdir) / Path(filename)
                pro7_props_file = propDocument_pb2.PropDocument()
                file2 = open(filepath, mode='rb')
                pro7_props_file.ParseFromString(file2.read())
                file2.close()
                absolute_ref_list.extend(re.findall(absolute_ref_regex, pro7_props_file.__str__()))
                relative_ref_list.extend(re.findall(relative_ref_regex, pro7_props_file.__str__()))
                path_ref_list.extend(re.findall(path_ref_regex, pro7_props_file.__str__()))
            if filename == "Workspace":
                filepath = Path(subdir) / Path(filename)
                pro7_workspace_file = proworkspace_pb2.ProPresenterWorkspace()
                file2 = open(filepath, mode='rb')
                pro7_workspace_file.ParseFromString(file2.read())
                file2.close()
                absolute_ref_list.extend(re.findall(absolute_ref_regex, pro7_workspace_file.__str__()))
                relative_ref_list.extend(re.findall(relative_ref_regex, pro7_workspace_file.__str__()))
                path_ref_list.extend(re.findall(path_ref_regex, pro7_workspace_file.__str__()))
            if filename == "Stage":
                filepath = Path(subdir) / Path(filename)
                pro7_stage_file = stage_pb2.Stage.Document()
                file2 = open(filepath, mode='rb')
                pro7_stage_file.ParseFromString(file2.read())
                file2.close()
                absolute_ref_list.extend(re.findall(absolute_ref_regex, pro7_stage_file.__str__()))
                relative_ref_list.extend(re.findall(relative_ref_regex, pro7_stage_file.__str__()))
                path_ref_list.extend(re.findall(path_ref_regex, pro7_stage_file.__str__()))

    # Convert absolute_ref_list items from url encoding with % codes to plain text
    #   This only applies to Mac, but conversion is done on everything, just in case
    for i in range(len(absolute_ref_list)):
        absolute_ref_list[i] = unquote(absolute_ref_list[i])

    # Convert reference lists from text to path objects
    for i in range(len(absolute_ref_list)):
        absolute_ref_list[i] = Path(absolute_ref_list[i])
    for i in range(len(relative_ref_list)):
        relative_ref_list[i] = Path(relative_ref_list[i])
    for i in range(len(path_ref_list)):
        path_ref_list[i] = Path(path_ref_list[i])

    # Convert media file list from text to path objects
    for i in range(len(media_files)):
        media_files[i] = Path(media_files[i])

    # Build list of files that are not used or referenced in ProPresenter, so they can be moved.
    files_to_move = []
    for media_file in media_files:
        ref_count = 0
        # Count file references in absolute_ref_list
        for ref in absolute_ref_list:
            if media_file.__str__().upper() in ref.__str__().upper():
                ref_count = ref_count + 1
        # Count file references in relative_ref_list
        for ref in relative_ref_list:
            if ref.__str__().upper() in media_file.__str__().upper():
                ref_count = ref_count + 1
        # Count file references in path_ref_list
        for ref in path_ref_list:
            if ref.__str__().upper() in media_file.__str__().upper():
                ref_count = ref_count + 1
        if ref_count == 0:
            files_to_move.append(media_file)

    # Move all unreferenced media files
    move_count = 0
    move_file_to_root_dir = home_dir / "Pro7 Media Sweeper" / Path("Swept Files (" + timestamp + ")")
    for move_file_from in files_to_move:
        start = len(sweep_folder_location.__str__()) + 1
        end = len(move_file_from.__str__())
        end_path = Path(move_file_from.__str__()[start:end])
        move_file_to = move_file_to_root_dir / end_path
        if not os.path.exists(move_file_to.parent):
            os.makedirs(move_file_to.parent)
        shutil.move(move_file_from, move_file_to)
        move_count = move_count + 1

    # Write Log File
    log_text = ["Pro7 Media Sweeper Log file. " + timestamp,
                move_count.__str__() + " Files Moved",
                "User Home Directory was: " + home_dir.__str__(),
                "Pro7 Support File Path was: " + pro7_support_file_path.__str__(),
                "All Files in Media Folder to Sweep (" + sweep_folder_location.__str__() + "):"]
    for line in media_files:
        log_text.append("- " + line.__str__())
    log_text.append("Found Absolute_String References:")
    for line in absolute_ref_list:
        log_text.append("- " + line.__str__())
    log_text.append("Found Relative_Path References:")
    for line in relative_ref_list:
        log_text.append("- " + line.__str__())
    log_text.append("Found Path References:")
    for line in path_ref_list:
        log_text.append("- " + line.__str__())
    log_text.append("Files to move:")
    for line in files_to_move:
        log_text.append("- " + line.__str__())

    log_file_path = Path(home_dir / "Pro7 Media Sweeper" / Path("Sweep_Log (" + timestamp + ").log"))
    if not os.path.exists(log_file_path.parent):
        os.makedirs(log_file_path.parent)

    log_file = open(log_file_path, mode="w", encoding="utf-8")
    try:
        for line in log_text:
            log_file.write(line + "\n")
        log_file.close()
    except BaseException as err:
        # Something went wrong writing the log file. No further logging will be captured! Display error to user.
        tk.messagebox.showinfo(title="Error!", message=err.__str__())
    log_file.close()

    # Set Button Status indication
    btn_sweep_files.config(text="Finished", state="normal", relief="raised")
    window.update()

    # Display pop-up when finished
    if move_count == 0:
        msg = "No Unreferenced Media Files Found."
    else:
        msg = move_count.__str__() + " files\nmoved to\n" + move_file_to_root_dir.__str__()
    tk.messagebox.showinfo(title="Done!", message=msg)

    # Set Button Status indication
    btn_sweep_files.config(text="Sweep Media Files!", state="normal", relief="raised")
    window.update()


# **********************************************************************************************************************
# Main program execution begins here

script_version = "2.0-beta1"

# Get the user's home_dir directory
home_dir = Path.home()

# Get the OS type this script is running on.
os_type = platform.system()

# Find the Pro7 folders for settings, libraries, playlists, and media
if os_type == "Windows":  # Set folder locations for Windows Machine
    pro7_app_data_location = home_dir / "AppData/Roaming/RenewedVision/ProPresenter"
    if not os.path.exists(pro7_app_data_location):
        tk.messagebox.showerror(title="Warning!", message="ProPresenter 7 Installation not found!  Program will end")
        exit()
    pro7_support_file_path = home_dir / "Documents/ProPresenter"
    media_location = home_dir / "/Documents/ProPresenter/Media"
    if os.path.exists(pro7_app_data_location / "PathSettings.proPaths"):
        file = open(pro7_app_data_location / "PathSettings.proPaths", 'r')
        file_lines = file.readlines()
        file.close()
        for file_line in file_lines:
            result = re.search(r"(?<=Base=).*(?=\\\\;)", file_line.strip())
            if result.group(0) != "":
                pro7_support_file_path = Path(result.group(0).replace("\\\\", "/"))
elif os_type == "Darwin":  # Set folder locations for Mac Machine
    pro7_pref_file_path = os.path.expanduser('~/Library/Preferences/com.renewedvision.propresenter.plist')
    if os.path.exists(pro7_pref_file_path):
        pro7_pref_file = open(pro7_pref_file_path, mode='rb')
        pl = plistlib.load(pro7_pref_file)
        pro7_pref_file.close()
        pro7_support_file_path = Path(pl["applicationShowDirectory"])
    else:
        tk.messagebox.showerror(title="Warning!", message="ProPresenter 7 Installation not found!  Program will end")
        pro7_support_file_path = Path("Not Found")
        exit()
else:
    tk.messagebox.showerror(title="Warning!", message="This OS is not supported!  Pro7 Media Sweeper will exit")
    pro7_support_file_path = Path("Not Found")
    exit()
media_location = pro7_support_file_path / "Media"

# Setup GUI
window = tk.Tk()
# icon = PhotoImage()  # TODO get window icon to work with pyinstaller
# window.iconphoto(False, icon)  # TODO get window icon to work with pyinstaller
window.title("Pro7 Media Sweeper - " + script_version)
window.config(borderwidth=10)

path_label = tk.Label(master=window, text="Media Folder to Sweep:")
path_label.pack()

path_text_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=2)
path_entry = tk.Entry(master=path_text_frame, width=80)
path_entry.insert(0, media_location.__str__())
path_entry.pack()
path_text_frame.pack()

btn_pick_folder = tk.Button(master=window, text="Change Folder to Sweep", command=pick_media_folder)
btn_pick_folder.pack()

cb = tk.IntVar(value=1)
ck_sub_folders = tk.Checkbutton(master=window, text='Include sub folders', variable=cb, onvalue=1, offvalue=0)
ck_sub_folders.pack()

btn_sweep_files = tk.Button(master=window, text="Sweep Media Files!", command=sweep_the_folder, width=30)
btn_sweep_files.pack()

window.mainloop()
