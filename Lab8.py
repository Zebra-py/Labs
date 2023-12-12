import tarfile
import os

def unpack_images_from_tar(tar_path, save_path):
    with tarfile.open(tar_path, 'r') as tar:
        image_files = [file for file in tar.getmembers() if os.path.splitext(file.name)[1] in ['.jpg', '.jpeg', '.png', '.gif']]

        for image_file in image_files:
            image_file.name = os.path.basename(image_file.name)
            tar.extract(image_file, path=save_path)

tar_path = 'путь к файлу'
save_path = 'куда сохраняем'
unpack_images_from_tar(tar_path, save_path)
