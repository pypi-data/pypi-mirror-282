from setuptools import setup

setup(
    name='carnotpy',
    version='0.2.1',
    author='Carnot Innovations',
    description='Carnot Connection as a Python Package',
    py_modules=['carnotpy'],
    install_requires=[
        'pandas',
        'requests',
        'python-dateutil',
    ],
)
