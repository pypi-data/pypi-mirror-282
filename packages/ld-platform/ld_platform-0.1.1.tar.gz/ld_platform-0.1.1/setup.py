from setuptools import setup, find_packages

setup(
    name='ld_platform',
    version='0.1.1',
    description='本地和s3的连接器',
    packages=find_packages(),
    install_requires=[
        'airflow==2.5.0',
        'smart-open==6.3.0',
        'boto3==1.27.0',
        'pymongo==4.3.3'
    ],
)
