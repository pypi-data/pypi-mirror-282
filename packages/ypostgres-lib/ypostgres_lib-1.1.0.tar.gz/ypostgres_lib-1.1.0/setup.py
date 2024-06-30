from setuptools import setup, find_packages

setup(
    name='ypostgres_lib',
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here if any
    ],
    author='yactouat',
    author_email='yacine.touati.pro@gmail.com',
    description='helper functions when I talk to Postgres directly',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yactouat/ypostgres_lib',
    license='MIT',
)
