from setuptools import setup, find_packages

setup(
    name='REAL_CIPHER_PACK',
    version='0.2',
    packages=find_packages(),
    description='A simple example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Abdelrahman Mahmoud',
    author_email='a.mahmoud1803@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'

)
