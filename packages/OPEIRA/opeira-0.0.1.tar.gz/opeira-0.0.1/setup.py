from setuptools import setup, find_packages

setup(
    name='OPEIRA',  # Choose a unique name for your package
    version='0.0.1',
    author='OPEIRA',
    packages=find_packages(),
    url='http://pypi.python.org/pypi/OPEIRA/',
    license='MIT',
    description='An awesome package',
    long_description=open('README.md').read(),
    install_requires=[
        # Any dependencies the package might have. Example:
        # "requests >= 2.20.0",
    ],
)
