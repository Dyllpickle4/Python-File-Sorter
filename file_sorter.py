import os
import sys
import file_info as f_info
from file_info import program_file_group

MISC_FILENAME = "misc_file_list.txt"

def get_dir_path() -> str:
    """Gets directory path to be sorted from second CLI arg."""
    argv_len = len(sys.argv)
    if argv_len == 2:
        return sys.argv[1]

    raise RuntimeError(
        "CLI arguments are not of required shape. "
        "Please ensure program is ran with format "
        "'file_sorter.py <sort_dir_path>' "
        "or this exception will be raised."
    )

def print_dir_files(dir: str):
    """Outputs all directory files sorted into list based files. Used for debugging."""
    os.chdir(dir)
    dir_filenames = os.listdir()
    misc_filenames = []

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

def sort_dir_files(dir: str):
    os.chdir(dir)
    for file_group in f_info.file_groups:
        file_group.move_file_list()

def main():
    dir_path = get_dir_path()
    print_dir_files(dir_path)
    sort_dir_files(dir_path)

if __name__ == '__main__':
    main()