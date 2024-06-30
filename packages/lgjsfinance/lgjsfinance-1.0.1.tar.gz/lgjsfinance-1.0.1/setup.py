from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='lgjsfinance',
    version='1.0.1',    
    description='LGJS Finance',
    url='https://liamgenjs.vercel.app',
    author='liamgen.js',
    author_email='liamgen.js@proton.me',
    license='BSD 2-clause',
    packages=['lgjsfinance'],
    install_requires=['yfinance>=0.2.38',
                      'matplotlib',
                      'datetime',
                      'python-binance'           
                      ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)