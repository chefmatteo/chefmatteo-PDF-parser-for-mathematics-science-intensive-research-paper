from setuptools import setup, find_packages

setup(
    name="pdf_parser",
    version="0.1",
    packages=find_packages(),
    package_dir={'': '.'},
    install_requires=[
        'pdfplumber>=0.7.0',
        'PyMuPDF>=1.19.0',
        'opencv-python>=4.5.0',
        'Pillow>=8.0.0',
        'pytesseract>=0.3.8',
        'numpy>=1.19.0',
        'transformers>=4.0.0',
        'torch>=1.8.0',
        'PyYAML>=5.4.0',
        'PyQt6>=6.0.0',
        'pdfminer.six>=20221105',
        'python-Levenshtein>=0.21.0',
        'regex>=2023.0.0',
        'chardet>=5.0.0',
    ],
) 