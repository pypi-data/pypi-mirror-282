from setuptools import setup, find_packages

setup(
    name="turkiye-son-depremler",
    version="0.3.2",
    author="Arıbilgi Akademi",
    author_email="aribilgiogr@gmail.com",
    description="Türkiye ve yakın çevresindeki son 500 deprem.",
    long_description=open('README.md', 'r', encoding="utf8").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aribilgiogr/turkiye-son-depremler',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'request', 'beautifulsoup4', 'bs4'
    ],
    python_requires='>=3.6',
)
