import os


def GetFileNames(directory_path):
    try:
        file_names = os.listdir(directory_path)

        return file_names
    except Exception as e:
        print(f"Ошибка: {e}")
        return []


path = "D:/3к1с"
files = GetFileNames(path)

for file in files:
    print(file)
