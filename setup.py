from setuptools import setup

setup(
    name='shopify-multipass',
    version='1.0.1',
    description='Shopify Multipass module for Python',
    url='https://github.com/hawflakes/shopify-multipass',
    author='hawflakes',
    author_email='jack@saltedfish.net',
    license='Apache 2.0 License',
    packages=['multipass'],
    install_requires=['pycryptodome~=3.7.2'],
)
