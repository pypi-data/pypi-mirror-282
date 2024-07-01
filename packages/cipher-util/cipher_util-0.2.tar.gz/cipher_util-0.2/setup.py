from setuptools import setup , find_packages

setup(
    name='cipher_util',
    version= '0.2',
    packages = find_packages(),
    install_requires=[
        'Flask>=2.0.0'
    ],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)