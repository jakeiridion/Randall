import os
from datetime import datetime, timedelta
import config

path = config.usb_path


def generate_folder_name():
    return datetime.now().strftime("%d.%m.%Y")


def generate_file_name():
    return datetime.now().strftime("%H:%M:%S")


def does_folder_exist(folder_path):
    if os.path.isdir(folder_path) is True:
        return True
    return False


def create_folder(folder_name):
    folder_path = os.path.join(path, folder_name)
    if does_folder_exist(folder_path) is False:
        os.mkdir(folder_path)


def return_whole_file_path(folder_name, file_name):
    return str(os.path.join(os.path.join(path, folder_name),
                            file_name))


def calculate_record_time(time_str):
    start_time = datetime.strptime(time_str, "%H:%M:%S")
    end_time = start_time.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    record_time = end_time - start_time
    return record_time.seconds


def rename_folder(file_path):
    os.renames(file_path + ".mp4", file_path + "-" + generate_file_name() + ".mp4")
