from setuptools import setup, find_packages

setup(
    name='data_anonymization',
    version='0.1.0',
    description='A FastAPI application for DICOM data anonymization and uploading to Firebase.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi',
        'uvicorn',
        'aiohttp',
        'firebase-admin',
        'pydicom',
        'python-multipart',
        'werkzeug',
    ],
    entry_points={
        'console_scripts': [
            'data-anonymization = data_anonymization.api:main',
        ],
    },
    package_data={
        'data_anonymization': ['firebase-key.json'],
    },
)
