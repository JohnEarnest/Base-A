from setuptools import setup

with open('requirements.txt', 'r') as f:
    install_requires = f.readlines()

# requires is a list of requirements
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
requires = [ir.strip() for ir in install_requires]

setup(
    name='basea',
    version='0.4.1',
    author='TnL Community',
    author_email='community@todandlorna.com',
    url='https://github.com/JohnEarnest/Base-A',
    packages=['basea'],
    description='encoding scheme for converting between small integers and names which would be appropriate for 260-foot tall, giant-monster-punching robots',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=requires,
    license='MIT',
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Religion",
        "Topic :: Utilities"
    ),
)
