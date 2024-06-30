from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os

current_file_path = os.path.abspath(__file__)
current_folder_path = os.path.dirname(current_file_path)

with open(os.path.join(current_folder_path, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.check_call(['pip', 'install', '-r', os.path.join(current_folder_path, 'requirements.txt')]),

setup(
    name='segcount',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        '': ['*.py'],  # Include all Python files in the root directory
    },
    description= "Segment and count object using SAM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    cmdclass={
        'install': PostInstallCommand,
    },
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
