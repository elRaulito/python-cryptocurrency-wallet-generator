from setuptools import setup, find_packages

setup(
    name='cryptocurrency-wallet-generator-fork',
    packages=find_packages(),
    version='0.0.1',
    url='https://github.com/elRaulito/python-cryptocurrency-wallet-generator'
 ,   author='raulrosa',
    author_email='raulr912@gmail.com',
    description='Fork of Arseni work, adding Einsteinium as coin',
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=[
        'ecdsa==0.13',
        'ethereum==2.1.0',
    ],
)
