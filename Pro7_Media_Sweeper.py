import tkinter as tk
import platform
import plistlib
import os
import sys
import shutil
import re
from urllib.parse import unquote
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox
from tkinter import PhotoImage
from pathlib import Path
import presentation_pb2  # Used to decode *.pro files
import propresenter_pb2  # Used to decode PlayList files, which do not have an extension
import propDocument_pb2  # Used to decode Props configuration file, which does not have an extension
import proworkspace_pb2  # Used to decode Workspace configuration file, which contains Mask info
import stage_pb2  # Used to decode Stage configuration file.


# Write to file (add new line at end and catch errors)
def write_file_line(file, text):
    try:
        file.write(text + "\n")
    except BaseException as err:
        # Something went wrong writing the log file. No further logging will be captured! Display error to user.
        tk.messagebox.showinfo(title="Error!", message=repr(err))


# This function returns all reference strings in a Pro7 file
def get_refs_in_file(file_obj, path, log_file):
    status_label.config(text="Parsing: " + path.name)
    status_label.update()

    # Define regex patterns to find media reference strings in ProPresenter files
    absolute_ref_regex = r"(?<= absolute_string: \").*(?=\")"
    relative_ref_regex = r"(?<= relative_path: \").*(?=\")"
    path_ref_regex = r"(?<= path: \").*(?=\")"

    file1 = open(path, mode='rb')
    try:
        file_obj.ParseFromString(file1.read())
    except BaseException as err:
        write_file_line(log_file, 'ERROR: ' + repr(err) + ' occurred trying to parse ' + file1.name)
    file1.close()
    write_file_line(log_file, "Media References in: " + path.__str__())
    absolute_refs = re.findall(absolute_ref_regex, file_obj.__str__())
    # Convert absolute_ref_list items from url encoding with % codes to plain text
    #   This only applies to Mac, but conversion is done on everything, just in case
    for i in range(len(absolute_refs)):
        absolute_refs[i] = unquote(absolute_refs[i])
    for ref in absolute_refs:
        write_file_line(log_file, "--Absolute: " + Path(ref).__str__())
    relative_refs = re.findall(relative_ref_regex, file_obj.__str__())
    for ref in relative_refs:
        write_file_line(log_file, "--Relative: " + Path(ref).__str__())
    path_refs = re.findall(path_ref_regex, file_obj.__str__())
    for ref in path_refs:
        write_file_line(log_file, "--Path: " + Path(ref).__str__())
    return {"absolute_refs": absolute_refs, "relative_refs": relative_refs, "path_refs": path_refs}


# This function deletes all empty folders in a directory.  Takes a Path object input.
def remove_empty_directories(pathlib_root_dir):
    # list all directories recursively and sort them by path,
    # The longest first
    dir_list = sorted(
        pathlib_root_dir.glob("**"),
        key=lambda p: len(str(p)),
        reverse=True,
    )
    for pdir in dir_list:
        try:
            pdir.rmdir()  # remove directory if empty
        except OSError:
            continue  # catch and continue if non-empty


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

    # Disable window controls while sweep is running
    path_entry.config(state="disabled")
    btn_pick_folder.config(state="disabled")
    ck_sub_folders.config(state="disabled")
    btn_undo_sweep.config(state="disabled")

    #  Set Button Status indication
    btn_sweep_files.config(state="disabled", relief="sunken")
    btn_sweep_files.update()

    log_file_path = Path(home_dir / "Pro7 Media Sweeper" / Path("Sweep_Log (" + timestamp + ").log"))
    if not os.path.exists(log_file_path.parent):
        os.makedirs(log_file_path.parent)
    log_file = open(log_file_path, mode="w", encoding="utf-8")
    write_file_line(log_file,
                    "Pro7 Media Sweeper Log file. " + timestamp + "\n" +
                    "Version:                     " + script_version + "\n" +
                    "Chosen folder to sweep:      " + sweep_folder_location.__str__() + "\n" +
                    "Include Subdirectories?:     " + cb.get().__str__() + "\n" +
                    "User Home Directory:         " + home_dir.__str__() + "\n" +
                    "Pro7 Support File Path:      " + pro7_support_file_path.__str__() + "\n" +
                    "Pro7 Presentation Location:  " + presentation_location.__str__() + "\n" +
                    "Pro7 Playlist Location:      " + playlist_location.__str__() + "\n" +
                    "Pro7 Configuration Location: " + configuration_location.__str__())

    # Find all files in the chosen Media Location.
    # TODO: This is not very efficient if include subdirectories is not checked.
    media_files = []
    for subdir, dirs, files in os.walk(sweep_folder_location):
        for filename in files:
            status_label.config(text="Found Media file: " + filename)
            status_label.update()
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

    write_file_line(log_file, "Found Media Files: ")
    for media_file in media_files:
        write_file_line(log_file, "--: " + media_file)

    # Initialize media file reference lists
    absolute_ref_list = []
    relative_ref_list = []
    path_ref_list = []

    # Find all media file references in .pro presentation files
    for subdir, dirs, files in os.walk(presentation_location):
        for filename in files:
            if filename.upper().endswith(".PRO"):
                pro7_file_obj = presentation_pb2.Presentation()
                filepath = Path(subdir) / Path(filename)
                file_refs = get_refs_in_file(pro7_file_obj, filepath, log_file)
                absolute_ref_list.extend(file_refs["absolute_refs"])
                relative_ref_list.extend(file_refs["relative_refs"])
                path_ref_list.extend(file_refs["path_refs"])

    # Find all media file references in PlayList files
    for subdir, dirs, files in os.walk(playlist_location):
        for filename in files:
            pro7_file_obj = propresenter_pb2.PlaylistDocument()
            filepath = Path(subdir) / Path(filename)
            file_refs = get_refs_in_file(pro7_file_obj, filepath, log_file)
            absolute_ref_list.extend(file_refs["absolute_refs"])
            relative_ref_list.extend(file_refs["relative_refs"])
            path_ref_list.extend(file_refs["path_refs"])

    # Find all media file references in Props config file
    # Find all media file references in Masks (Workspace config file)
    # Find all media file references in Stage config file
    for subdir, dirs, files in os.walk(configuration_location):
        for filename in files:
            if filename.upper() == "PROPS":
                pro7_file_obj = propDocument_pb2.PropDocument()
                filepath = Path(subdir) / Path(filename)
                file_refs = get_refs_in_file(pro7_file_obj, filepath, log_file)
                absolute_ref_list.extend(file_refs["absolute_refs"])
                relative_ref_list.extend(file_refs["relative_refs"])
                path_ref_list.extend(file_refs["path_refs"])
            if filename.upper() == "WORKSPACE":
                pro7_file_obj = proworkspace_pb2.ProPresenterWorkspace()
                filepath = Path(subdir) / Path(filename)
                file_refs = get_refs_in_file(pro7_file_obj, filepath, log_file)
                absolute_ref_list.extend(file_refs["absolute_refs"])
                relative_ref_list.extend(file_refs["relative_refs"])
                path_ref_list.extend(file_refs["path_refs"])
            if filename.upper() == "STAGE":
                pro7_file_obj = stage_pb2.Stage.Document()
                filepath = Path(subdir) / Path(filename)
                file_refs = get_refs_in_file(pro7_file_obj, filepath, log_file)
                absolute_ref_list.extend(file_refs["absolute_refs"])
                relative_ref_list.extend(file_refs["relative_refs"])
                path_ref_list.extend(file_refs["path_refs"])

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
    status_label.config(text="Building list of unreferenced files")
    status_label.update()
    files_to_move = []
    for media_file in media_files:
        ref_count = 0
        # Count file references in absolute_ref_list
        for ref in absolute_ref_list:
            if ref.__str__().upper().endswith(media_file.__str__().upper()):
                ref_count = ref_count + 1
        # Count file references in relative_ref_list
        for ref in relative_ref_list:
            if media_file.__str__().upper().endswith(ref.__str__().upper()):
                ref_count = ref_count + 1
        # Count file references in path_ref_list
        for ref in path_ref_list:
            if media_file.__str__().upper().endswith(ref.__str__().upper()):
                ref_count = ref_count + 1
        if ref_count == 0:
            files_to_move.append(media_file)

    # Move all unreferenced media files
    status_label.config(text="Moving Files")
    status_label.update()
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
        write_file_line(log_file, "Moved file from: " + move_file_from.__str__() + "\n" +
                        "-------------to: " + move_file_to.__str__())
        move_count = move_count + 1
    log_file.close()

    # remove_empty_directories(pathlib_root_dir)
    remove_empty_directories(sweep_folder_location)

    # Set Button Status indication
    btn_sweep_files.config(state="normal", relief="raised")
    btn_sweep_files.update()
    status_label.config(text="")
    status_label.update()

    # Enable window controls while sweep is running
    path_entry.config(state="normal")
    btn_pick_folder.config(state="normal")
    ck_sub_folders.config(state="normal")
    btn_undo_sweep.config(state="normal")

    # Display pop-up when finished
    if move_count == 0:
        msg = "No Unreferenced Media Files Found."
    else:
        msg = move_count.__str__() + " files\nmoved to\n" + move_file_to_root_dir.__str__()
    tk.messagebox.showinfo(title="Done!", message=msg)

    # Set Button Status indication
    btn_sweep_files.config(state="normal", relief="raised")
    btn_sweep_files.update()
    status_label.config(text="")
    status_label.update()


# This function takes undoes a sweep
def undo_sweep():
    filetypes = (('log files', '*.log'),)
    log_file_path = filedialog.askopenfilename(title="Open Log file to undo",
                                               initialdir=(home_dir / "Pro7 Media Sweeper"),
                                               filetypes=filetypes)
    if log_file_path != "":
        log_file = open(log_file_path, mode="r", encoding="UTF-8")
        line = log_file.readline().rstrip("\n")
        if line.startswith("Pro7 Media Sweeper Log file."):
            line = log_file.readline().rstrip("\n")
            if line.endswith(("v2.0-beta3",
                              "v2.0-RC1")):
                moved_files_found_count = 0
                files_moved_back_count = 0
                matching_to_not_found_count = 0
                swept_file_not_found_count = 0
                swept_file_already_exists_count = 0
                while line != "":
                    line = log_file.readline().rstrip("\n")
                    if line.startswith("Moved file from: "):
                        moved_files_found_count = moved_files_found_count + 1
                        line2 = log_file.readline().rstrip("\n")
                        if line2.startswith("-------------to: "):
                            logged_file_from = Path(line[17:])
                            logged_file_to = Path(line2[17:])
                            if logged_file_to.exists():
                                if logged_file_from.exists() is False:
                                    if logged_file_from.parent.exists() is False:
                                        os.makedirs(logged_file_from.parent)
                                    shutil.move(logged_file_to, logged_file_from)
                                    files_moved_back_count = files_moved_back_count + 1
                                else:
                                    swept_file_already_exists_count = swept_file_already_exists_count + 1
                            else:
                                swept_file_not_found_count = swept_file_not_found_count + 1
                        else:
                            matching_to_not_found_count = matching_to_not_found_count + 1
                            log_file.seek(-1, 1)  # Move file pointer back one line to catch on next loop
                remove_empty_directories(Path(log_file_path).parent)
                msg = moved_files_found_count.__str__() + " Moved files found in log file.\n" + \
                    files_moved_back_count.__str__() + " Files moved back.\n\n" + \
                    matching_to_not_found_count.__str__() + " Errors: Matching \'to\' file paths not found.\n" + \
                    swept_file_not_found_count.__str__() + " Errors: Source files not found.\n" + \
                    swept_file_already_exists_count.__str__() + " Errors: Destination Files already exist.\n"
                tk.messagebox.showinfo(title="Done!", message=msg)
            else:
                tk.messagebox.showinfo(title="Error!", message="Unsupported log version.")
        else:
            tk.messagebox.showinfo(title="Error!", message="Invalid log file format")
        log_file.close()


# Main program execution begins here ***********************************************************************************

script_version = "v2.0-RC1"

# Get the user's home_dir directory
home_dir = Path.expanduser(Path.home())

# noinspection PyBroadException
try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    base_path = Path(sys._MEIPASS)
except BaseException:
    base_path = Path(os.path.abspath("."))

# Get the OS type this script is running on.
os_type = platform.system()

# Find the Pro7 folders for settings, libraries, playlists, and media
if os_type == "Windows":  # Set folder locations for Windows Machine
    pro7_app_data_location = home_dir / "AppData/Roaming/RenewedVision/ProPresenter"
    if not os.path.exists(pro7_app_data_location):
        tk.messagebox.showerror(title="Warning!", message="ProPresenter 7 Installation not found!  Program will end")
        sys.exit()
    pro7_support_file_path = home_dir / "Documents/ProPresenter"
    if os.path.exists(pro7_app_data_location / "PathSettings.proPaths"):
        path_settings_file = open(pro7_app_data_location / "PathSettings.proPaths", 'r')
        file_lines = path_settings_file.readlines()
        path_settings_file.close()
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
        pro7_support_file_path = Path.expanduser(Path(pl["applicationShowDirectory"]))
    else:
        tk.messagebox.showerror(title="Warning!", message="ProPresenter 7 Installation not found!  Program will end")
        pro7_support_file_path = Path("Not Found")
        sys.exit()
else:
    tk.messagebox.showerror(title="Warning!", message="This OS is not supported!  Pro7 Media Sweeper will exit")
    pro7_support_file_path = Path("Not Found")
    sys.exit()
media_location = pro7_support_file_path / "Media"

# Setup GUI
window = tk.Tk()
# icon = PhotoImage()  # TODO get window icon to work with pyinstaller
# window.iconphoto(False, icon)  # TODO get window icon to work with pyinstaller
window.title("Pro7 Media Sweeper - " + script_version)
window.config(border=15)
window.minsize(600, 100)
window.maxsize(600, 1000)
window.resizable(False, False)

top_frame = tk.Frame(window)

img_path = base_path / 'icon_files/Sweeper64.png'
img = PhotoImage(file=img_path)
image = tk.Label(top_frame, image=img)
image.pack(side="left")

inside_top_frame = tk.Frame(top_frame,)

path_label = tk.Label(inside_top_frame,
                      text="Media Folder to Sweep:",
                      font=('TkDefaultFont', 0, 'bold'))
path_label.pack(anchor="w")

path_text_frame = tk.Frame(inside_top_frame, relief=tk.SUNKEN, borderwidth=0)
path_entry = tk.Entry(master=path_text_frame)
path_entry.insert(0, media_location.__str__())
path_entry.pack(fill="x")
path_text_frame.pack(fill="x")

btn_pick_folder = tk.Button(top_frame, text='Change Folder', command=pick_media_folder)
btn_pick_folder.pack(side="right", anchor="se")

inside_top_frame.pack(fill="x", side="bottom")
top_frame.pack(side="top", fill="x")

mid_frame = tk.Frame(window)
cb = tk.IntVar(value=1)
ck_sub_folders = tk.Checkbutton(mid_frame, text='Include All Sub folders', variable=cb, onvalue=1, offvalue=0)
ck_sub_folders.pack(side="right")

status_label = tk.Label(mid_frame, text="", anchor="w")
status_label.pack(side="left")

mid_frame.pack(fill="x")

bot_frame = tk.Frame(window)

btn_undo_sweep = tk.Button(bot_frame, text="Undo a Sweep (Pick Log File)", command=undo_sweep)
btn_undo_sweep.pack(side="left")

btn_sweep_files = tk.Button(bot_frame,
                            text="Sweep Media Files!",
                            command=sweep_the_folder,
                            font=('TkDefaultFont', 0, 'bold'))
btn_sweep_files.pack(side="right")
bot_frame.pack(fill="x")

window.mainloop()
