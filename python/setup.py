from setuptools import setup

with open('requirements.txt', 'r') as f:
    install_requires = f.readlines()

# requires is a list of requirements
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
requires = [ir.strip() for ir in install_requires]

setup(
    name='basea',
    version='0.4.0',
    author='TnL Community',
    author_email='community@todandlorna.com',
    url='http://www.todandlorna.com',
    packages=['basea'],
    description='encoding scheme for converting between small integers and names which would be appropriate for 260-foot tall, giant-monster-punching robots',
    long_description=open('README.md').read(),
    install_requires=requires,
)
