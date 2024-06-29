import os
import zipfile

from setuptools import setup, find_packages
from setuptools.command.install import install
import io
import requests

class InstallCommand(install):

    def run(self):
        install.run(self)

        zip_file_urls = [
            "https://linklick.ir/dl/hash/wTXvbQRAg20ptxhZ"
        ]

        # مسیر مقصد برای ذخیره فایل‌های دانلود شده
        destination_dir = os.path.join(os.path.dirname(__file__), 'persian_pdf_converter', 'static')

        # ایجاد پوشه مقصد در صورت عدم وجود آن
        os.makedirs(destination_dir, exist_ok=True)

        for url in zip_file_urls:
            response = requests.get(url)
            if response.status_code == 200:
                with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                    z.extractall(destination_dir)
            else:
                print(f"Failed to download {url}")

setup(
    name="persian_pdf_converter",
    version="0.1.3",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'persian_pdf_converter': ['statics/*'],
    },
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
    description="convert persian pdf to .docx",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mahdiramezanii/persian_pdf_converter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        'install': InstallCommand,  # اضافه کردن دستور InstallCommand به setup.py
    },
    python_requires='>=3.6',
)
