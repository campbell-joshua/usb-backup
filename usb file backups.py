"""
Josh Campbell
18:11 2/25/2017
HackIllinois
This program takes all files from the D:\\ drive
The files on the drive are compared to directory C:\\Users\\Josh\\Documents\\PyCharm\\
If files are missing from the C:\\ drive they are copied from D:\\
If a file on D:\\ was modified more recently it will be copied to C:\\
The program will skip outdated and identical files to increase efficiency
"""

import os
import shutil

#global variables
flashdrive = 'D:\\'
C_drive = 'C:\\Users\\Josh\\Documents\\PyCharm'
flash_path = ''
c_path = ''


def flashdrive_files():
    """Returns the paths from D:\\"""
    global flashdrive
    file_paths = []

    #Loops through D:\\
    for subdir, dirs, files in os.walk(flashdrive):
        if not files:
            file_paths.append(subdir)
            continue

        #appends files to list
        for file in files:
            file_paths.append(os.path.join(subdir, file))

    return(file_paths)


def c_drive_files():
    """Returns paths from C:\\"""
    global C_drive
    c_file_paths = []

    #Loops through C:\\ and appends files to list
    for subdir, dirs, files in os.walk(C_drive):
        for file in files:
            c_file_paths.append(os.path.join(subdir, file))

    return(c_file_paths)


def new_directories(file_names, intersection_list):
    """Creates directories that are not found on C:\\"""
    global flashdrive

    #skips intersection list
    for file_name in file_names:
        if file_name in intersection_list:
            continue

        #finds the deepest directory path
        dirs = file_name.split('\\')[:-1]
        deepest_dir = '\\'.join(dirs)

        #rejoins the path if isdir
        if os.path.isdir(os.path.join(flashdrive, file_name)):
            deepest_dir = file_name

        #joins the C:\\ with directory to find correct path to creat folder
        new_file = os.path.join(C_drive, deepest_dir)
        if not os.path.exists(new_file):
            os.makedirs(new_file)

        print("New directory was created: ", deepest_dir)


def copy_files(file_names, intersection_list):
    """Copies files that are outdated and not found on C:\\ when compared to D:\\"""
    for i, file_name in enumerate(file_names):

        #determines if the file is aleady in C:\\
        if file_name in intersection_list:
            #compares time of last modification, if modification is newer on D:\\ it copies to C:\\
            #else it does nothing
            if os.path.getmtime(flash_path[i]) > os.path.getmtime(C_drive + '\\' + file_name):
                shutil.copyfile(flash_path[i], C_drive + '\\' + file_name)
                print('file was updated for: ', file_name)

        #if file is not in C:\\ it will do the following
        else:
            #try/except to catch errors
            try:
                #if file isdir it is skipped to avoid rewriting empty folders as blank files
                if os.path.isdir(os.path.join(flashdrive, file_name)):
                    continue

                #creates a new file in C:\\ with same name as file in D:\\
                with open(C_drive + '\\' + file_name, 'w') as f:
                    pass

                #copies new and updated fiels from D:\\ to C:\\
                shutil.copyfile(flash_path[i], C_drive + '\\' + file_name)
                print('New file was created for or updated:', file_name)
            #except for FileNotFoundError
            except(FileNotFoundError, IOError):
                print("File not found error for:", file_name)
                pass


def main():
    global flash_path, c_path

    #calls functions to set vars
    flash = flashdrive_files()
    c = c_drive_files()
    flash_path, c_path = flash, c

    #removes :C\\Users\\Josh\\Documents\\PyCharm and :D\\ to allow for easier manipulation
    flash_base = [file[3:] for file in flash]
    c_base = [file[len(C_drive+'\\'):] for file in c]

    #finds files with the same basename
    intersection_points = set(flash_base).intersection(c_base)
    intersection_list = list(intersection_points)

    #calls functions to copy new and updated files
    new_directories(flash_base, intersection_list)
    copy_files(flash_base, intersection_list)

main()