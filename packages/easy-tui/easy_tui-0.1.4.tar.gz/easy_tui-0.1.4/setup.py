from setuptools import setup, find_packages

setup(
    name="easy_tui",
    version="0.1.4",
    packages=find_packages(),
    include_package_data=True,
    description="A miniTUI with the ability to handle simple keyboard events in a terminal.\nIt's about avoiding all the noise when learning to program.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mon Maldonado",
    author_email="monterdi@gmail.com",
    url="https://github.com/digestiveThinking/simple_screen",
    install_requires=[
        'simple_screen==0.1.14'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
