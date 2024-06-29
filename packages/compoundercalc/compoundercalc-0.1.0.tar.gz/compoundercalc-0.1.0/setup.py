# setup.py

from setuptools import setup, find_packages

setup(
    name='compoundercalc',
    version='0.1.0',
    description='A package for compound interest calculations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/croketillo/compoundercalc',
    author='Croketillo',
    author_email='croketillo@gmail.com',
    license='GNU v3',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
)
