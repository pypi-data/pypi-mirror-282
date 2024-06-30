# setup.py

from setuptools import setup, find_packages

setup(
    name='pandas-xml',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'my_package_script = my_package.my_module:main_function',
        ],
    },
    install_requires=[
        # add any dependencies here
    ],
    author='ROInsight',
    author_email='support@roinsight.com',
    description='pandas-xml management',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/roinsightsupport/pandas-xml',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


