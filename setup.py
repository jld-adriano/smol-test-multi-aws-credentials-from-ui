```python
from setuptools import setup, find_packages

setup(
    name='multi-aws-credentials',
    version='1.0.0',
    description='Simple tool to manage multiple aws credentials locally',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/multi-aws-credentials',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'click',
        'cryptography',
    ],
    entry_points={
        'console_scripts': [
            'multi-aws-credentials=multi_aws_credentials.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
```