import os
import sys
import file_info as f_info
from tkinter import *
from tkinter import ttk

MISC_FILENAME = "misc_file_list.txt"
misc_filenames = []

def get_dir_path() -> str:
    """Gets directory path to be sorted from second CLI argument."""
    argv_len = len(sys.argv)
    if argv_len == 2:
        return sys.argv[1]

    return ''

def print_dir_files(dir: str):
    """Outputs a list of all directory files sorted into their relating files."""
    os.chdir(dir)
    dir_filenames = os.listdir()

    # Determine where each file falls under file groups
    for filename in dir_filenames:
        success = False

        # Look at each file group
        for file_group in f_info.file_groups:
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
    for file_group in f_info.file_groups:
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
    for file_group in f_info.file_groups:
        count += file_group.move_file_list(mode)

    print(f"Total files sorted: {count}")
    print(f"Couldn't move: {misc_filenames}")

def handle_sorting(dir: str, mode_list_result):
    """Handle the various sorting mode conditions."""
    if mode_list_result != ():
        print_dir_files(dir)
        if mode_list_result[0] <= 1:
            move_dir_files(dir, mode_list_result[0])
    else:
        print("Please select a mode first.")

def handle_gui():
    """Handle the graphical user interface window of the sorting system."""
    sort = lambda: handle_sorting(dir_path.get(), mode_list.curselection())

    window_root = Tk()
    window_root.title('Python File Sorter')
    frame = ttk.Frame(window_root, padding=10)
    frame.grid()
    Label(frame, text='Directory Path', padx=5, justify='center').grid(row=0, column=0)

    dir_path = StringVar(value=get_dir_path())
    dir_path_entry = Entry(frame, width=50, textvariable=dir_path)
    dir_path_entry.grid(row=0, column=1)

    Label(frame, text="Select a Mode", justify='center', pady=5).grid(row=1, column=0)

    mode_list = Listbox(frame, height=3, width=12)
    mode_list.grid(row=2, column=0)
    options = ['Move Mode', 'Copy Mode', 'List Mode']
    for i in options:
        mode_list.insert(END, i)

    submit_btn = Button(frame, text='Submit', command=sort)
    submit_btn.grid(row=1, column=1)

    window_root.mainloop()

def main():
    handle_gui()

if __name__ == '__main__':
    main()