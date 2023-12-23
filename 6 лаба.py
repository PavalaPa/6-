import os

while True:
    path = os.path.abspath(input('Enter folder path: '))
    if os.path.exists(path):
        break
    print('File not found :(((((')

output_file_path = os.path.join(path, 'hierarchy.txt')

with open(output_file_path, 'w') as output_file:
    for folder, subfolders, files in os.walk(path):
        max_files = []
        max_size = 0

        for file in files:
            file_path = os.path.join(folder, file)
            size = os.stat(file_path).st_size

            if size > max_size:
                max_size = size
                max_files = [(file, file_path, size)]
            elif size == max_size:
                max_files.append((file, file_path, size))

        if max_files:
            output_file.write(f'Folder: {folder}\n')
            for file_info in max_files:
                file_name, file_path, file_size = file_info
                output_file.write(f'File: {file_name}\n')
                output_file.write(f'Path: {file_path}\n')
                output_file.write(f'Size: {file_size} bytes\n')
            output_file.write('\n')

print(f'Information written to {output_file_path}')
