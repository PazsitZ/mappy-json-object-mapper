from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='mappy_json-object-mapper',
    version='1.0.2',
    license='MIT',
    author="Zoltan Pazsit",
    author_email='pazsitz@pazsitz.hu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/PazsitZ/mappy-json-object-mapper',
    keywords='python json object mapper',
    install_requires=[ ],
    description = "MapPy Json - Object Mapper",
    long_description=long_description,
    long_description_content_type='text/markdown'
)