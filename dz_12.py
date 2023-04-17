import os

#os.mkdir('files')

os.chdir('files')

for i in range(1, 10):
    new_folder = f"folder_{i}"
    #os.mkdir(new_folder)

file_path = os.path.join(new_folder, 'file.txt')
if os.path.isfile(file_path):
      print(f"{file_path} існує")
else:
      print(f"{file_path} не існує")

os.rmdir('folder_7')
os.rmdir('folder_8')
import shutil # імпортую shutil, щоб видалити не пусту директорію!
shutil.rmtree('folder_9')


import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to run.")
        return result
    return wrapper