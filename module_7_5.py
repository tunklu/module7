import os
import time

for root, dirs, files in os.walk(os.getcwd()):
  for file in files:
      if os.path.isfile(file):
        filepath = os.getcwd()
        filetime = os.stat(file).st_mtime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(file).st_size
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
