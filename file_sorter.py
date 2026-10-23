import os
import sys
import sort_info as info
import tkinter as tk
from tkinter import ttk, filedialog

MISC_FILENAME = "misc_file_list.txt"
misc_filenames = []

def handle_browse_dialog(dir_path: tk.StringVar):
    """Handles the dialog to select filepath."""
    folder_path = filedialog.askdirectory(title='Select a Folder')

    if folder_path:
        dir_path.set(folder_path)

def get_dir_path() -> str:
    """Gets directory path to be sorted from second CLI argument."""
    argv_len = len(sys.argv)
    if argv_len == 2:
        return sys.argv[1]

    return '.'

def print_dir_files(dir: str):
    """Outputs a list of all directory files sorted into their relating files."""
    os.chdir(dir)
    dir_filenames = os.listdir()

    # Determine where each file falls under file groups
    for filename in dir_filenames:
        success = False

        # Look at each file group
        for file_group in info.file_groups:
            # Try to add filename to file group
            success = file_group.try_add_file(filename)

            # Continue to next filename if success
            if success:
                break

        # If no match for file group, add to misc filenames list
        if not success:
            misc_filenames.append(filename)

    os.makedirs('moved_lists', exist_ok=True)
    os.chdir('moved_lists')

    print('Writing sorted filename lists!')
    print('-' * 10)
    # Output filename lists
    for file_group in info.file_groups:
        file_group.output_file_list()

    print(MISC_FILENAME)
    with open(MISC_FILENAME, 'w', encoding='utf-8') as file:
        misc_filenames_str = '\n'.join(misc_filenames)
        file.write(misc_filenames_str)
    print('-' * 10)

def move_dir_files(dir: str, mode: int):
    """Moves directory files to corresponding folder."""
    os.chdir(dir)
    count = 0
    for file_group in info.file_groups:
        count += file_group.move_file_list(mode)

    print(f"Total files sorted: {count}")
    print(f"Couldn't move: {misc_filenames}")

def handle_sorting(dir: str, mode_list_result):
    """Handles the various sorting mode conditions."""
    if mode_list_result != ():
        print_dir_files(dir)
        if mode_list_result[0] <= 1:
            move_dir_files(dir, mode_list_result[0])
    else:
        print("Please select a mode first.")

def handle_gui():
    """Handles the graphical user interface window of the sorting system."""
    window_root = tk.Tk()
    window_root.title('Python File Sorter')
    style = ttk.Style()
    style.theme_use('clam')
    py_logo = tk.PhotoImage(file='assets/Python-logo.png')
    window_root.iconphoto(False, py_logo)
    frame = ttk.Frame(window_root, padding=10)
    frame.grid()

    tk.Label(frame, text="Select a Mode", justify='center', pady=5).grid(row=0, column=0, sticky="nsew")
    mode_list = tk.Listbox(frame, height=3, width=12)
    mode_list.grid(row=1, column=0, sticky="nsew")
    options = ['Move Mode', 'Copy Mode', 'List Mode']
    for i in options:
        mode_list.insert(tk.END, i)

    browse = lambda: handle_browse_dialog(dir_path)
    sort = lambda: handle_sorting(dir_path.get(), mode_list.curselection())
    dir_frame = ttk.Frame(frame, padding=(0, 5))
    dir_frame.grid(row=2, column=0)
    tk.Label(dir_frame, text='Directory Path', padx=5, justify='center').grid(row=0, column=0)
    dir_path = tk.StringVar(value=get_dir_path())
    dir_path_entry = tk.Entry(dir_frame, width=50, textvariable=dir_path)
    dir_path_entry.grid(row=0, column=1)
    dir_browse_btn = tk.Button(dir_frame, text='Browse', command=browse)
    dir_browse_btn.grid(row=0, column=2)
    submit_btn = tk.Button(dir_frame, text='Submit', command=sort)
    submit_btn.grid(row=1, column=1)

    window_root.mainloop()

def main():
    handle_gui()

if __name__ == '__main__':
    main()