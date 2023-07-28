import gdown
import os
file_url = 'https://drive.google.com/uc?id='            # Initial part of url


folder = "Dog Identification/Nose detection models"     # Folder name to which we need to download the files

if not os.path.exists(folder):
    os.makedirs(folder)

# from the complete url we just need the id which is after d/ and before /view
# complete_url = "https://drive.google.com/file/d/1UDp4dUfrynMRGCJyzt-OGW8PQHoRe11-/view?usp=drive_link"

id = "1UDp4dUfrynMRGCJyzt-OGW8PQHoRe11-"

url = file_url+id
saving_name = "model_1.pt"
file = gdown.download(url,os.path.join(folder,saving_name))


