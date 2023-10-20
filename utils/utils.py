import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()
from basic_app.models import Image

folder_path = r'C:\Users\user\PycharmProjects\user\kale\images2'
file_list = os.listdir(folder_path)
size_limit = 380
size = 0

for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    file_size = os.path.getsize(file_path)
    file_size_mb = file_size / (1024 * 1024)

    if file_size == 0:
        os.remove(file_path)
        print(f"Removed {file_name}")
    else:
        print(f"File name {file_name}  {file_size_mb} MB")

    if size + file_size_mb <= size_limit:
        code = file_name.split('.')[0]
        with open(file_path, 'rb') as f:
            image = Image(code=code)
            image.image.save(file_name, File(f))
            image.save()
        print(f"Created {file_name}")
        os.remove(file_path)
        size += file_size_mb
    else:
        break
