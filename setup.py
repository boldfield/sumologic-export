"""Our python packaging stuff."""


from setuptools import setup


setup(

    # Basic package information:
    name = 'sumologic-export',
    version = '0.0.1',
    scripts = ['sumologic-export'],

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['docopt>=0.6.2', 'requests>=2.3.0'],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'r@rdegges.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/sumologic-export',
    keywords = ['sumologic', 'logs', 'export', 'utility'],
    description = 'Easily export your Sumologic log data.',
    long_description = 'Easily export your Sumologic log data.',

)
