from setuptools import setup, find_packages

setup(
    name='techv-cloud_logger',
    version='0.1.0',
    description='A logger implementation for AWS, GCP, and local logging.',
    author='TechVedika',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'google-cloud-logging',
        'python-dotenv',
        'colorama'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
