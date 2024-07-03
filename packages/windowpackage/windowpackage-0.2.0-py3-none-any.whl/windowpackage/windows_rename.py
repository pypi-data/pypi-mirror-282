import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
image_folder_path = filedialog.askdirectory(
    title="請選取圖片資料夾")

file_info_list = []
def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            image_path= os.path.join(root, file)
            #kind = filetype.guess(file_path)
            _, extension = os.path.splitext(file)
            extension = extension.lower() 
            if extension in ['.tiff', '.tif', '.jpg', '.jpeg', '.png']:  # 只添加圖像文件
                print(f'找到圖像文件: {image_path}')
                file_info_list.append(image_path)
            else:
                print(f'跳過非圖像文件: {image_path}')
                
scan_directory(image_folder_path)

def rename_files(directory):
    for image_path in file_info_list:
        file_info_list.sort()  # Sort the files to maintain any existing order, if necessary 對 files 列表進行了排序

# Rename files sequentially
    for index, filename in enumerate(file_info_list):  #同時獲得每個文件的索引(index)和文件名(filename)。
        _, extension = os.path.splitext(filename)# Generates '0000.tiff', '0001.tiff', etc.  #們使用 f-string 格式化的方式創建新的文件名,如 "0000.tiff"、"0001.tiff" 等。
        new_filename = f"{index:04d}{extension}"
        old_file = os.path.join(directory, filename)  #os.path.join(directory, filename) 用於拼接目錄路徑和文件名,獲得完整的舊文件路徑(old_file)。
        new_file = os.path.join(directory, new_filename)  #os.path.join(directory, new_filename) 用於構建新文件路徑(new_file)

        os.rename(old_file, new_file)  #os.rename(old_file, new_file) 函數用於將舊文件重命名為新文件名
        print(f"Renamed '{filename}' to '{new_filename}'")

    print("Renaming complete.")

rename_files(image_folder_path)