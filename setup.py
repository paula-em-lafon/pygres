from setuptools import setup

setup(
    name = 'pygres',
    packages = ['pygres'], # this must be the same as the name above
    version = '1.2.4',
    description = 'Postgres simple driver',
    author = 'Rodrigo Gamba',
    author_email = 'gamba.lavin@gmail.com',
    url = 'https://github.com/rogamba/pygres', # use the URL to the github repo
    download_url = 'https://github.com/rogamba/pygres/tarball/0.1', # I'll explain this in a second
    keywords = ['postgres', 'psql', 'postgresql'],
    install_requires=[
        'psycopg2>=2.6.2',
    ],
    classifiers = [],
)
