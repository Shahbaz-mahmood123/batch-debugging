from setuptools import setup, find_packages

VERSION = '0.0.6'
DESCRIPTION = 'A SDK that helps debug batch compute enviornments in AWS, GCP and Azure and Kubernetes'
LONG_DESCRIPTION = 'A package that makes it easier to debug issues with batch compute enviornments in GCP, AWS and Azure'

setup(
    name="batch_debugging",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="shahbaz mahmood",
    author_email="shahbazmahmooood@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'httpx',
        'attrs',
        'boto3'
        ],
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
