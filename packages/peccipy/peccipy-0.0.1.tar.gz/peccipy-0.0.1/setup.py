from setuptools import setup, find_packages

setup(
    name='peccipy',
    version='0.0.1', 
    packages=find_packages(),  
    install_requires=[ 
        'pandas',
        'numpy',
    ],
    entry_points={  # Entry points for command-line scripts
        'console_scripts': [
            'peccipy_hello = peccipy.main:hello',
        ],
    },
    author='ashik',
    author_email='datas293@gmail.com',
    description='A package for doing preprocessing. Not something new but just combined.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ashiknazar/peccipy',  # Fixed URL syntax
)
