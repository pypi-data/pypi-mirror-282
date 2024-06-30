from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os

current_file_path = os.path.abspath(__file__)
current_folder_path = os.path.dirname(current_file_path)

with open(os.path.join(current_folder_path, 'README.md'), 'r', encoding='utf-8') as fh:
    long_description = fh.read()

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.check_call(['pip', 'install', '-r', os.path.join(current_folder_path, 'requirements.txt')])

setup(
    name='openvino_trackface',
    version='0.0.1',
    include_package_data=True,
    packages=find_packages(),
    description= "Face tracking using OpenVINO Face detection and ByteTrack model",
    long_description = long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        # List other pip dependencies here if any
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ]
)
