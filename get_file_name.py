import os

def get_file_id(file):
    file_name = os.path.basename(file)
    name_without_extention = os.path.splitext(file_name)[0]
    splited_data = name_without_extention.split("_")
    file_id = splited_data[1]
    return file_id