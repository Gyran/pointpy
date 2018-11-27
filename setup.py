from setuptools import setup

setup(
    name='pointpy',
    version='1.0.0',
    description='point client',
    author="@gyran",
    author_email="gustav.ahlberg@gmail.com",
    install_requires=[
        'requests>=2.3.0',
    ],
    license='LICENSE.txt',
    packages=['pointpy']
)
