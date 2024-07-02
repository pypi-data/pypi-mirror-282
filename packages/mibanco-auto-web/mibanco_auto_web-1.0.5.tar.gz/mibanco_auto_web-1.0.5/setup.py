from setuptools import setup, find_packages
from setuptools.command.install import install
from mibanco_auto_web.variables import *

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='mibanco_auto_web',
    version= version,
    description='A simple functional test library using Python and Selenium',
    author='Automation & Performance Team',
    packages=find_packages(),
    include_package_data=True, #Esto hace que setuptools lea el archivo MANIFEST.in
    install_requires=[
        "behave==1.2.6",
        "behave2cucumber==1.0.3",
        "docxcompose==1.4.0",
        "docxtpl==0.16.8",
        "psutil==5.9.8",
        "pillow==10.3.0",
        "openpyxl==3.1.2",
        "customtkinter==5.2.2",
        "PyPDF2==3.0.1",
        "python-docx==1.1.0",
        "selenium==4.20.0"
    ],
    entry_points={
        'console_scripts': [
            'mibanco_auto_web=mibanco_auto_web.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
    keywords=['selenium', 'testing', 'web', 'chrome', 'firefox', 'edge', 'python', 'cucumber'],
    long_description=long_description,
    long_description_content_type="text/markdown",
)