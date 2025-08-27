from setuptools import setup, find_packages


setup(
    name='mappy_json-object-mapper',
    version='1.0',
    license='MIT',
    author="Zoltan Pazsit",
    author_email='pazsitz@pazsitz.hu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/pazsitz/mappy_json-object-mapper',
    keywords='python json object mapper',
    install_requires=[ ],

)