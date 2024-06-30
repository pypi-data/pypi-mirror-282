from setuptools import setup, find_packages

with open("README.md","r") as f:
    description = f.read()

setup(
    name='animefan',
    version='1.1.3',
    description='A CLI tool for anime quotes and ASCII art',
    author='Arman Sethi',
    author_email='armansethi64@gmail.com',
    url='https://github.com/arman0333/anime-cli',
    packages=find_packages(include=['animefan', 'animefan.*']),  
    include_package_data=True,
    install_requires=[
        'requests',
        'pyfiglet',
    ],
     entry_points={
        'console_scripts': [
            'anime-fan=animefan:hello',
        ],
    },
     package_data={
        "animefan": ["content/*", "ascii-images/*"],  
    },

    long_description=description,
    long_description_content_type="text/markdown",
)
