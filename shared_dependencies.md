Shared Dependencies:

1. "multi_aws_credentials" - This is the main package name that all the files belong to.

2. "Profile" - This is a data schema that is used across the files to represent an AWS profile. It likely contains fields such as "id", "secret", and "region".

3. "Credentials" - This is another data schema that represents the AWS credentials. It is used across the files and is likely linked to the "Profile" schema.

4. "encrypt" and "decrypt" - These are function names that are used for password encryption and decryption. They are likely used in the "encryption.py" file and may be used in other files as well.

5. "add", "change", "list", "rename", "upsert", "env", "env-run", "remove", "help" - These are command names that are used in the "command.py" file and likely used in the "main.py" file to handle user commands.

6. "AWS_CREDENTIALS_PATH" - This is a constant that represents the path to the AWS credentials file. It is likely used in the "credentials.py" file and possibly in other files as well.

7. "AWS_PROFILE_PATH" - This is another constant that represents the path to the AWS profile file. It is likely used in the "profile.py" file and possibly in other files as well.

8. "version" and "help" - These are option names that are used in the "main.py" file and possibly in other files as well.

9. "setup" - This is a function name that is used in the "setup.py" file to set up the application. It may also be used in other files.

10. "README.md" - This file likely contains information that is used across the other files, such as the application description, installation instructions, and usage instructions.