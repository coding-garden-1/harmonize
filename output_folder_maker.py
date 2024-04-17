
import os
import datetime

def output_folder_maker():
    folder_name =  'output ' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs(folder_name)
    return folder_name