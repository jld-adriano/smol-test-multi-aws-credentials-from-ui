```python
import os
from .constants import AWS_PROFILE_PATH
from .encryption import encrypt, decrypt

class Profile:
    def __init__(self, id, secret, region):
        self.id = id
        self.secret = secret
        self.region = region

    def save(self, name, password=None):
        data = {
            'id': self.id,
            'secret': self.secret,
            'region': self.region
        }
        if password:
            data = encrypt(data, password)
        with open(os.path.join(AWS_PROFILE_PATH, f"{name}.creds"), 'w') as f:
            f.write(data)

    @classmethod
    def load(cls, name, password=None):
        with open(os.path.join(AWS_PROFILE_PATH, f"{name}.creds"), 'r') as f:
            data = f.read()
        if password:
            data = decrypt(data, password)
        return cls(data['id'], data['secret'], data['region'])
```