# helloworld/setup.py

from setuptools import setup, find_packages

setup(
    name='helloworldthiyagu',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'helloworld-cli = helloworld.hello:say_hello',
        ],
    },
    author='thiyagubaskaranpypi',
    author_email='thiyagubaskaran359@gmail.com',
    description='A simple hello world package',
    long_description='A minimal package that prints "Hello, World!"',
    long_description_content_type='text/plain',
    # url='https://github.com/yourusername/helloworld',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
