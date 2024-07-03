from setuptools import setup, find_packages
import sys

# Check if the system is Windows
if sys.platform != 'win32':
    raise RuntimeError('This package is only compatible with Windows.')


setup(
    name='dately',
    version="2.1.4",
    author='Cedric Moore Jr.',
    author_email='cedricmoorejunior5@gmail.com',
    description='A comprehensive Python library for advanced date and time manipulation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cedricmoorejr/dately',
    project_urls={
        'Source Code': 'https://github.com/cedricmoorejr/dately/tree/main/dately',
    },
    packages=find_packages(),
    package_data={
        'dately': [
            'mold/pyd/*.pyd',
            'mold/pyd/cdatetime/*.pyd'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',        
    ],
    python_requires='>=3.8',
    install_requires=[
        'numpy',
        'pandas',
        'pytz',
        'requests',
    ],
    license='MIT',
)




