```python
import os
from .constants import AWS_CREDENTIALS_PATH, AWS_PROFILE_PATH

def get_profile_path(profile_name):
    return os.path.join(AWS_PROFILE_PATH, f"{profile_name}.creds")

def get_credentials_path():
    return AWS_CREDENTIALS_PATH

def check_file_exists(file_path):
    return os.path.exists(file_path)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def delete_file(file_path):
    if check_file_exists(file_path):
        os.remove(file_path)
```