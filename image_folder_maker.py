
import os
import datetime

def image_folder_maker():
    folder_name =  'images_to_be_video_' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs(folder_name)
    return folder_name