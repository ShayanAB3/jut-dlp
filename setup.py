from setuptools import setup, find_packages

setup(
    name="jut-dlp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests==2.32.3",
        "beautifulsoup4==4.13.3",
        "bs4==0.0.2",
        "tabulate==0.9.0",
        "tqdm==4.67.1",
        "loguru==0.7.3"
    ],
    entry_points={
        "console_scripts": [
            "jut-dlp=jut_dlp.main:main"
        ],
    },
    python_requires='>=3.8',
)
