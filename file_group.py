import os
import re
import shutil

class FileExtensionGroup:
    """A collection of file extension strings."""

    def __init__(self, group_name: str, extensions: list[str]):
        self.group_name = group_name
        self.extensions = []

        for extension_str in extensions:
            if extension_str.startswith('.'):
                self.extensions.append(extension_str)

    def add_file_extension(self, extension_str: str):
        self.extensions.append(extension_str)

    def add_extension_of_file(self, filename: str):
        extension_match = re.search(r'\.\w+$', filename)
        if extension_match: self.add_file_extension(extension_match.group())

class FileGroup:
    """A collection of filenames that follow a FileExtensionGroup."""

    def __init__(self, extension_group: FileExtensionGroup):
        self.extension_group = extension_group
        self.group_name = self.extension_group.group_name + '_file_group'
        self.filenames = []
        self.output_filename = self.extension_group.group_name + '_file_list.txt'

    def try_add_file(self, filename: str) -> bool:
        """
        Tries to add file to group.\n
        Will only add file if it contains an extension from the FileExtensionGroup.
        """
        extension_match = re.search(r'\.\w+$', filename)
        extensions = self.extension_group.extensions

        if extension_match and extension_match.group().lower() in extensions:
            self.filenames.append(filename)
            return True
        else:
            return False

    def try_add_files(self, filenames: list[str]) -> dict[str, bool]:
        """
        Wrapper for try_add_file that tries to add multiple files to group.\n
        Will only add files that contain extensions from the FileExtensionGroup.\n
        """
        filenames_status = {}
        for filename in filenames:
            status = self.try_add_file(filename)
            filenames_status[filename] = status

        return filenames_status

    def output_file_list(self):
        """Outputs list of files to be moved."""
        filenames_str = '\n'.join(self.filenames)
        print(self.output_filename)
        with open(self.output_filename, 'w', encoding='utf-8') as file:
            file.write(filenames_str)

    def move_file_list(self, mode: int) -> int:
        """Outputs all files in file group to a newly created directory."""
        end_index = self.output_filename.find('_list')
        new_dir_name = self.output_filename[:end_index] + 's'

        os.makedirs(new_dir_name, exist_ok=True)

        cwd = os.getcwd()
        new_dir_path = os.path.join(cwd, new_dir_name)
        count = 0
        for filename in self.filenames:
            cwd_file = os.path.join(cwd, filename)
            new_dir_file = os.path.join(new_dir_path, filename)

            try:
                if mode == 0:
                    shutil.move(cwd_file, new_dir_file)
                elif mode == 1:
                    shutil.copy2(cwd_file, new_dir_file)

                count += 1
            except PermissionError:
                print(f"\tSkipped (due to permission denied): {os.path.basename(cwd_file)}")

        if mode == 0:
            print(f'Copied {count} files to {new_dir_name} from {cwd}!')
        elif mode == 1:
            print(f'Moved {count} files to {new_dir_name} from {cwd}!')

        return count