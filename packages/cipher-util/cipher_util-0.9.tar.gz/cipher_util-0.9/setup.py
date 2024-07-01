from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='cipher_util',
    version='0.9',
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0.0',
        'setuptools'
    ],
    python_requires='>=3.8.10',
    long_description=long_description,
    long_description_content_type='text/markdown', 
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
