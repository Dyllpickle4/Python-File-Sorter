from file_group import FileGroup, FileExtensionGroup

compressed_file_group = FileGroup(
    FileExtensionGroup(
        'compressed',
        [
            '.zip', '.gz', '.tar', '.7z', '.rar'
        ]
    )
)

image_file_group = FileGroup(
    FileExtensionGroup(
        'image',
        [
            '.png', '.jpg', '.jpeg', '.gif', '.svg',
            '.webp', '.bmp', '.raw'
        ]
    )
)

doc_file_group = FileGroup(
    FileExtensionGroup(
        'document',
        [
            '.doc', '.docx', '.pdf', '.rtf', '.odt'
        ]
    )
)

txt_file_group = FileGroup(
    FileExtensionGroup(
        'text_document',
        [
            '.txt', '.json', '.xml', '.yaml', '.yml',
            '.ini', '.md'
        ]
    )
)

multimedia_file_group = FileGroup(
    FileExtensionGroup(
        'multimedia',
        [
            '.mp3', '.mp4', '.wav', '.avi', '.mov',
            '.mkv'
        ]
    )
)

spreadsheet_file_group = FileGroup(
    FileExtensionGroup(
        'spreadsheet',
        [
            '.xlsx', '.xls', '.csv'
        ]
    )
)

presentation_file_group = FileGroup(
    FileExtensionGroup(
        'presentation',
        [
            '.pptx', '.ppt'
        ]
    )
)

program_file_group = FileGroup(
    FileExtensionGroup(
        'program',
        [
            '.exe', '.jar', '.deb', '.msi', '.cmd',
            '.com','.sys', '.app', '.dmg', '.pkg',
            '.rpm', '.bin', '.apk', '.ipa', '.iso'
        ]
    )
)

editing_file_group = FileGroup(
    FileExtensionGroup(
        'editing',
        [
            '.afdesign', '.afphoto', '.psf', '.psb', '.xcf',
            '.ai', '.cdr', '.fig', '.kra', '.clip', '.rif',
            '.procreate', '.xmp', '.piskel', '.mlt', '.3mf',
            '.stl', '.bbmodel'
        ]
    )
)

web_file_group = FileGroup(
    FileExtensionGroup(
        'web',
        [
            '.html', '.htm', '.css', '.js', '.php'
        ]
    )
)

script_file_group = FileGroup(
    FileExtensionGroup(
        'script',
        [
            '.bat', '.sh', '.py', '.ts', '.rb', '.pl', '.lua', '.ipynb'
        ]
    )
)

code_file_group = FileGroup(
    FileExtensionGroup(
        'code',
        [
            '.c', '.h', '.cpp', '.cc', '.hpp', '.java', '.cs', '.go', '.rs', '.swift'
        ]
    )
)

file_groups = [
    compressed_file_group,
    image_file_group,
    doc_file_group,
    txt_file_group,
    multimedia_file_group,
    spreadsheet_file_group,
    presentation_file_group,
    program_file_group,
    editing_file_group,
    web_file_group,
    script_file_group,
    code_file_group
]