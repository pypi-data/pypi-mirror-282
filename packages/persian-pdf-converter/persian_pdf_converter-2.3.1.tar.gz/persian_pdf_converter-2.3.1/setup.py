import os
import zipfile
from setuptools import setup, find_packages
from setuptools.command.install import install
import io
import requests

destination_dir = os.path.join(os.path.dirname(__file__), 'static')

class InstallCommand(install):

    def run(self):
        install.run(self)

        zip_file_urls = [
            "https://linklick.ir/dl/hash/wTXvbQRAg20ptxhZ"
        ]

        os.makedirs(destination_dir, exist_ok=True)

        for url in zip_file_urls:
            response = requests.get(url)
            if response.status_code == 200:
                with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                    z.extractall(destination_dir)
            else:
                pass

setup(
    name="persian_pdf_converter",
    version="2.3.1",
    packages=find_packages(),
    package_data={'my_pkg':['my_pkg/resources/*']},
    include_package_data=True,

    install_requires=[
        "tqdm",
        "pdf2image",
        "pytesseract",
        "Pillow",
        "python-docx",
        "requests"
    ],
    author="mahdiramezani",
    author_email="mahdiramezanii.official@gmail.com",
    description="persian_pdf_converter by Mahdi Ramazani is a Python package that converts PDF files to Word documents with OCR support for Persian and English. It automatically downloads and sets up necessary tools like Tesseract and Poppler.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mahdiramezanii/persian_pdf_converter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.6',
)
