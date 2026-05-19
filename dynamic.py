import os

UPLOAD_FOLDER = 'static'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

filepath = os.path.join(UPLOAD_FOLDER, 'temp.jpg')
file.save(filepath)