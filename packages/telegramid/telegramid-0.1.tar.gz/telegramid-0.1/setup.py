from setuptools import setup, find_packages

setup(
    name='telegramid',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'telegramid=telegramid.main:main',
        ],
    },
    install_requires=[
        'requests',
    ],
    author='Fidal',
    author_email='mrfidal@proton.me',
    description='A package to fetch Telegram group chat ID, user ID, username, and message info',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ByteBreach/telegramid', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
