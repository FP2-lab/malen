import os
def find_and_rename_files(directory, extension, new_name_prefix):
    counter=1
    for root, _, files in os.walk(directory):
        # Фильтруем файлы по расширению
        filtered_files = filter(lambda f: f.endswith(extension), files)
        
        # Переименовываем файлы
        for file_name in filtered_files:
            old_path = os.path.join(root, file_name)
            new_file_name = f"{new_name_prefix}_{counter}{extension}"
            new_path = os.path.join(root, new_file_name)
            
            os.rename(old_path, new_path)
            yield new_path  
            counter +=1 


directory = "C:\\Users\\артем\Desktop\\lab5"  
extension = ".txt"  
new_name_prefix = "renamed"  
for renamed_file in find_and_rename_files(directory, extension, new_name_prefix):
    print(f"Переименован файл: {renamed_file}")