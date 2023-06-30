```python
import os

# Constants for file paths
AWS_CREDENTIALS_PATH = os.path.expanduser("~/.aws/credentials")
AWS_PROFILE_PATH = os.path.expanduser("~/.aws/$NAME.creds")

# Constants for command names
COMMANDS = ["add", "change", "list", "rename", "upsert", "env", "env-run", "encrypt", "remove", "help"]

# Constants for option names
OPTIONS = ["-V", "--version", "-h", "--help"]
```