```python
import os
from .constants import AWS_CREDENTIALS_PATH
from .encryption import decrypt

class Credentials:
    def __init__(self, id, secret, region):
        self.id = id
        self.secret = secret
        self.region = region

    def save(self, profile_name, encrypted=False, password=None):
        creds_path = os.path.join(AWS_CREDENTIALS_PATH, f"{profile_name}.creds")
        with open(creds_path, 'w') as f:
            if encrypted:
                f.write(decrypt(self.id, password))
                f.write(decrypt(self.secret, password))
            else:
                f.write(self.id)
                f.write(self.secret)
            f.write(self.region)

    @classmethod
    def load(cls, profile_name, encrypted=False, password=None):
        creds_path = os.path.join(AWS_CREDENTIALS_PATH, f"{profile_name}.creds")
        with open(creds_path, 'r') as f:
            id = f.readline().strip()
            secret = f.readline().strip()
            region = f.readline().strip()

            if encrypted:
                id = decrypt(id, password)
                secret = decrypt(secret, password)

            return cls(id, secret, region)
```