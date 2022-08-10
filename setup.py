import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pytest-sqlalchemy-mock',
    license='MIT',
    description='pytest sqlalchemy plugin for mock',
    # long_description=read("README.rst"),
    version='0.1.0',
    author='Resul Yurttakalan',
    author_email='resulyrt93@gmail.com',
    url='https://github.com/resulyrt93/pytest-sqlalchemy-mock',
    py_modules=['pytest_sqlalchemy_mock'],
    entry_points={'pytest11': ['sqlalchemy = pytest_sqlalchemy_mock']},
    install_requires=['pytest>=2.0', 'sqlalchemy'],
    classifiers=[
        'Framework :: Pytest',
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ]
)
