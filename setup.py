
from setuptools import setup

setup(
    name = "seqsero2",
    version = "2.0",
    author = "DengLab",
    author_email = "seqsero@gmail.com",
    description = ("Serotyping for Salmonella."),
    license = "GPL-2.0",
    keywords = "salmonella",
    url = "https://github.com/CFSAN-Biostatistics/SeqSero2",
    packages=['seqsero2'],
    scripts=['scripts/SeqSero2.py'],
     entry_points={
        'console_scripts': ['SeqSero2 = seqsero2.SeqSero2:main']
    },
    package_dir = {'seqsero2': 'scripts'}
)
