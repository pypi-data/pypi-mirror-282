from setuptools import setup, find_packages

setup(
    name="my_Quran",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tkinter',  # Although tkinter is included with Python, you may add it for completeness
        'pillow',  # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'my-quran=my_Quran.main:run',
        ],
    },
    package_data={
        '': ['*.db'],  # Include database files
    },
    author="Isaiah Olad",
    author_email="isaiaholad@gmail.com",
    description="A Tkinter application to read and search the Quran.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/isaiaholad/my_Quran",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
