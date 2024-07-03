from setuptools import setup, find_packages

setup(
    name='Delta_Bypasser',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    description='A module to bypass delta',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='iwcool.gg',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
