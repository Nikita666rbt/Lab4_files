import os


def GetFileNames(directory_path):
    try:
        file_names = os.listdir(directory_path)

        #file_names = [f for f in file_names if os.path.isfile(os.path.join(directory_path, f))]

        return file_names
    except Exception as e:
        print(f"Ошибка: {e}")
        return []


path = "D:/3к1с"
files = GetFileNames(path)

for file in files:
    print(file)
