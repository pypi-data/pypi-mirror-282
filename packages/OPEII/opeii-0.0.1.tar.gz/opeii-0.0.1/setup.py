from setuptools import setup, find_packages

setup(
    name='OPEII',
    version='0.0.1',
    author='OPEII',
    packages=find_packages(),
    url='http://pypi.python.org/pypi/OPEIRA/',
    license='MIT',
    description='An awesome package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        # Any dependencies the package might have. Example:
        # "requests >= 2.20.0",
    ],
)
