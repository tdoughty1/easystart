#! /usr/bin/env python
"""

Module to automate the creation of setup files for the start project approach.

"""

def write_python(config):

    # Open file for writing
    f = open('setup.py','w')

    # Module docstring
    f.write('#! /usr/bin/env python\n')
    f.write('\n')
    f.write('"""\n')
    f.write('A setuptools based setup module for ' + config.project_name + '.\n')
    f.write('Modeled from:\n')
    f.write('https://packaging.python.org/en/latest/distributing.html\n')
    f.write('https://github.com/pypa/sampleproject\n')
    f.write('"""\n\n')

    # Module loding steps
    f.write('# Always prefer setuptools over distutils\n')
    f.write('from setuptools import setup, find_packages\n')
    f.write('# To use a consistent encoding\n')
    f.write('from codecs import open\n')
    f.write('from os import path\n\n')

    # Get description from README
    f.write('# Get the long description from the README file\n')
    f.write('here = path.abspath(path.dirname(__file__))\n')
    f.write("with open(path.join(here, 'README.rst'), encoding='utf-8') as f:\n")
    f.write('    long_description = f.read()\n\n')
    
    # Include Setup configuration options
    f.write('setup(\n')
    f.write('    name=' + config.project_name + ',\n\n')

    # Version info
    f.write('    # Versions should comply with PEP440.  For a discussion on single-sourcing\n')
    f.write('    # the version across setup.py and the project code, see\n')
    f.write('    # https://packaging.python.org/en/latest/single_source_version.html\n')
    f.write("    version=" + config.version + ",\n\n")
    
    # Description info
    f.write("    description='A sample Python project',\n")
    f.write("    long_description=long_description,\n\n")

    # Hosting info
    f.write("    # The project's main homepage.\n")
    f.write("    url='https://github.com/pypa/sampleproject',\n\n")

    # Author info
    f.write("    # Author details\n")
    f.write("    author='The Python Packaging Authority',\n")
    f.write("    author_email='pypa-dev@googlegroups.com',\n\n")

    # License info
    f.write('    # Choose your license\n')
    f.write("    license='MIT',\n\n")

    # Classifier info
    f.write('    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers\n')
    f.write('    classifiers=[\n')
    f.write('        # How mature is this project? Common values are\n')
    f.write('        #   3 - Alpha\n')
    f.write('        #   4 - Beta\n')
    f.write('        #   5 - Production/Stable\n')
    f.write("        'Development Status :: 3 - Alpha',\n\n")

    # Project Audience info
    f.write('        # Indicate who your project is intended for\n')
    f.write("        'Intended Audience :: Developers',\n")
    f.write("        'Topic :: Software Development :: Build Tools',\n\n")

    # License Classification info
    f.write('        # Pick your license as you wish (should match "license" above)\n')
    f.write("        'License :: OSI Approved :: MIT License',\n\n")

    # Python Version info
    f.write('        # Specify the Python versions you support here. In particular, ensure\n')
    f.write('        # that you indicate whether you support Python 2, Python 3 or both.\n')
    f.write("        'Programming Language :: Python :: 2',\n")
    f.write("        'Programming Language :: Python :: 2.6',\n")
    f.write("        'Programming Language :: Python :: 2.7',\n")
    f.write("        'Programming Language :: Python :: 3',\n")
    f.write("        'Programming Language :: Python :: 3.2',\n")
    f.write("        'Programming Language :: Python :: 3.3',\n")
    f.write("        'Programming Language :: Python :: 3.4',\n")
    f.write("        'Programming Language :: Python :: 3.5',\n")
    f.write('    ],\n\n')

    # Project Keywords
    f.write('    # What does your project relate to?\n')
    f.write("    keywords='sample setuptools development',\n\n")

    # Automatic Package inclusion
    f.write('    # You can just specify the packages manually here if your project is\n')
    f.write('    # simple. Or you can use find_packages().\n')
    f.write("    packages=find_packages(exclude=['contrib', 'docs', 'tests']),\n\n")

    f.write('    # Alternatively, if you want to distribute just a my_module.py, uncomment\n')
    f.write('    # this:\n')
    f.write('    #   py_modules=["my_module"],\n\n')

    # Run Time dependency
    f.write('    # List run-time dependencies here.  These will be installed by pip when\n')
    f.write('''    # your project is installed. For an analysis of "install_requires" vs pip's\n''')
    f.write('    # requirements files see:\n')
    f.write('    # https://packaging.python.org/en/latest/requirements.html\n')
    f.write("    install_requires=['peppercorn'],\n\n")

    # Additional dependencies
    f.write('    # List additional groups of dependencies here (e.g. development\n')
    f.write('    # dependencies). You can install these using the following syntax,\n')
    f.write('    # for example:\n')
    f.write('    # $ pip install -e .[dev,test]\n')
    f.write('    extras_require={\n')
    f.write("        'dev': ['check-manifest'],\n")
    f.write("        'test': ['coverage'],\n")
    f.write('    },\n')

    # Required datafiles
    f.write('    # If there are data files included in your packages that need to be\n')
    f.write('    # installed, specify them here.  If using Python 2.6 or less, then these\n')
    f.write('    # have to be included in MANIFEST.in as well.\n')
    f.write('    package_data={\n')
    f.write("        'sample': ['package_data.dat'],\n")
    f.write('    },\n\n')

    f.write("    # Although 'package_data' is the preferred approach, in some case you may\n")
    f.write('    # need to place data files outside of your packages. See:\n')
    f.write('    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa\n')
    f.write("    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'\n")
    f.write("    data_files=[('my_data', ['data/data_file'])],\n\n")

    # Executable scripts
    f.write('    # To provide executable scripts, use entry points in preference to the\n')
    f.write('    # "scripts" keyword. Entry points provide cross-platform support and allow\n')
    f.write('    # pip to create the appropriate form of executable for the target platform.\n')
    f.write('    entry_points={\n')
    f.write("        'console_scripts': [\n")
    f.write("            'sample=sample:main',\n")
    f.write('        ],\n')
    f.write('    },\n')
    f.write(')\n')

    # Close file after writing
    f.close()

def write_config(self):
    pass
