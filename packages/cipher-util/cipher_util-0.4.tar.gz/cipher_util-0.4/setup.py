from setuptools import setup, find_packages

setup(
    name='cipher_util',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0.0',
    ],
    python_requires='>=3.8.8',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
