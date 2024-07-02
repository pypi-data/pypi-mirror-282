from setuptools import setup, find_packages

setup(
    name="DOCK_BYTE",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pymupdf",
        "pdf2image",
        "pytesseract",
        "langchain_community",
        "streamlit",
    ],
    entry_points={
        'console_scripts': [
            'chat_with_doc=dock_byte.script:chat_with_doc',
        ],
    },
    author="Muhammad Abdullah",
    author_email="abdullahcodewizard@gmail.com",
    description="A module to extract text from documents and chat with the content.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/CodeByte-hash/DOCK_BYTE",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
