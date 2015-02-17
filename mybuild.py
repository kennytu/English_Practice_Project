#!/usr/bin/env python3
import os,sys
sys.path.append("./data_module")

from cx_Freeze import setup, Executable

image_files = []
files = os.listdir("./images")

for file in files :
    try :
        file.rindex(".png")
        t = "images\\" + file
        print t
        image_files.append(t)
    except ValueError :
        pass

image_files.append("images\\previous.jpg")

#includefiles = ['user_data.txt'] + image_files
includefiles =  image_files

#print(includefiles)

epp_version = "0.1.2"

epp_install_target_dir = "c:\English_Practise_Project__" + epp_version

if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', epp_install_target_dir]

exe = Executable(
        script="EPP.pyw",
        base="Win32GUI",
        #base ="console",
        shortcutName = "EGG Shortcut",
        icon = "window_book_icon.ico",
        compress = True
        )

setup(
        name = "English Practise Project",
        version = epp_version,
        author = 'Kenny Tu',
        author_email = 'kenny.tw@hotmail.com',
        description = "English Practise Project for Practise English Skill",
        options = 
        {
            'build_exe': 
            {
                'include_files':includefiles, 
                "optimize":2,
                "compressed": True
            }
        }, 
        executables = [exe]
     )




