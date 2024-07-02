# root/artifacts/queues/setup.py
from setuptools import setup, find_packages

setup(
    name='itba_microservices_raabitmq_connectors',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author='Gonzalo Beade',
    author_email='gbeade@itba.edu.ar',
    description="""
        A queues utility package for microservices.
        Consumers, producers and DTOs.
    """,
    url='https://gitlab.com/gbeade/microservices',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
