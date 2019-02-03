from setuptools import setup

setup(
    name='shopify-multipass',
    version='1.0.0',
    description='Shopify Multipass module for Python',
    url='https://github.com/gureuso/shopify-multipass',
    author='gureuso',
    author_email='wyun13043@gmail.com',
    license='Apache 2.0 License',
    packages=['multipass'],
    install_requires=['pycryptodome~=3.7.2'],
)
