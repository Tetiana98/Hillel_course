import os
import pickle

path = '/Users/tanya_mazarella/venv/lib/python3.10/site-packages/pandas/tests/tools'
file_count = 0
dir_count = 0
results_file = 'results.csv'
max_count = 100

try:
    for root, dirs, files in os.walk(path):
     file_count += len(files)
     dir_count += len(dirs)

     smallest_file = None
     smallest_file_size = float('inf')
     largest_file = None
     largest_file_size = 0
     shortest_name = None
     shortest_name_length = float('inf')
     longest_name = None
     longest_name_length = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
        if file_size < smallest_file_size:
           smallest_file = file_path
           smallest_file_size = file_size
        if file_size > largest_file_size:
           largest_file = file_path
           largest_file_size = file_size
        if len(file) < shortest_name_length:
           shortest_name = file_path
           shortest_name_length = len(file)
        if len(file) > longest_name_length:
           longest_name = file_path
           longest_name_length = len(file)

    if len(results_file) >= max_count:
        breakpoint()

    results = {
        'file_count': file_count,
        'dir_count': dir_count,
        'smallest_file': smallest_file,
        'largest_file': largest_file,
        'shortest_name': shortest_name,
        'longest_name': longest_name
    }
    with open(results_file, 'wb') as f:
        pickle.dump(results_file, f)

except KeyboardInterrupt:
    results_file = {
        'file_count': file_count,
        'dir_count': dir_count,
        'smallest_file': smallest_file,
        'largest_file': largest_file,
        'shortest_name': shortest_name,
        'longest_name': longest_name
    }
    with open(results_file, 'wb') as f:
        pickle.dump(results, f)
    print('Interrupted by user')
    exit()

    with open(results_file, 'rb') as f:
         results = pickle.load(f)
    exclude_files = [results['smallest_file'], results['largest_file']]
    exclude_dirs = [os.path.dirname(p) for p in exclude_files]
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if os.path.join(root, d)]

print('Smallest file:', smallest_file)
print('Largest file:', largest_file)
print('Shortest name:', shortest_name)
print('Longest name', longest_name)
print('Found files:', file_count)
print('Found folders:', dir_count)