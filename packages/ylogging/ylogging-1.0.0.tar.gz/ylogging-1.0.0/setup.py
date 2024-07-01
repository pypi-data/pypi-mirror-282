from setuptools import setup, find_packages

setup(
    name='ylogging',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # ...
    ],
    author='yactouat',
    author_email='yacine.touati.pro@gmail.com',
    description='logging helper for python that I always use in my projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yactouat/ylogging',
    license='MIT',
)
