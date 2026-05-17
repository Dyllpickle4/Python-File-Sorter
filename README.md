# Python File Sorter
This project is a basic file sorter script in Python. It uses only the Python Standard Library and, as such, can be used after installing [Python](https://www.python.org/) itself.

## What does this do?
The script will attempt to sort any files of its current directory based on its file extension into 1 of 12 newly created directory groupings and also output. To view these groupings and relating outputs, reference the "What is the output?" section.<br>

## How does this run?
To run this script, simply run the `file_sorter.py` with the argument of `<path_to_dir_to_sort>`. This would look like `python file_sorter.py C:\Users\example_user\Downloads` for a Windows system.<br>

## What is the output?
As stated, this program outputs all files moved, or sorted, into new directories relating to their extention. They are grouped as follows, in format `<description> (<new_dir_nam>)`:
* **Compressed Files (compressed_files)**: 
    * .zip
    * .gz
    * .tar
    * .7z
    * .rar
    
* **Image Files (image_files)**: 
    * .png
    * .jpg / .jpeg
    * .gif
    * .svg
    * .webp
    * .bmp
    * .raw
* **Document Files (document_files)**: 
    * .doc
    * .docx
    * .pdf
    * .rtf
    * .odt
* **Text-Like Formatted Files (text_document_files)**: 
    * .txt
    * .json
    * .xml
    * .yaml
    * .yml
    * .ini
    * .md
* **Video and Audio Files (multimedia_files)**: 
    * .mp3
    * .mp4
    * .wav
    * .avi
    * .mov
    * .mkv
* **Spreadsheet Files (spreadsheet_files)**: 
    * .xlsx
    * .xls
    * .csv
* **Presentation Files (presentation_files)**: 
    * .pptx
    * .ppt
* **Runnable Files (program_files)**: 
    * .exe
    * .jar
    * .deb
    * .msi
    * .cmd
    * .com
    * .sys
    * .app
    * .dmg
    * .pkg
    * .rpm
    * .bin
    * .apk
    * .ipa
* **Editing Software Save Files (editing_files)**: 
    * .afdesign
    * .afphoto
    * .psf
    * .psb
    * .xcf
    * .ai
    * .cdr
    * .fig
    * .kra
    * .clip
    * .rif
    * .procreate
    * .xmp
    * .piskel
    * .mlt
* **Web-Based Files (web_files)**
    * .html
    * .htm
    * .css
    * .js
    * .php
* **Script-Based Files (script_files)**: 
    * .bat
    * .sh
    * .py
    * .ts
    * .rb
    * .pl
    * .lua
* **Compile-Based Files (code_files)**: 
    * .c
    * .h
    * .cpp
    * .cc
    * .hpp
    * .java
    * .cs
    * .go
    * .rs
    * .swift