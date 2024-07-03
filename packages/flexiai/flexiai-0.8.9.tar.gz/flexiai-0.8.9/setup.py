from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.run(['python', 'post_install.py'])

setup(
    name='flexiai',
    version='0.8.9',
    packages=find_packages(include=['flexiai', 'flexiai.*']),
    include_package_data=True,
    package_data={
        'flexiai': ['data/*.csv', '*.py'],
    },
    install_requires=[
        'annotated-types==0.7.0',
        'anyio==4.4.0',
        'azure-common==1.1.28',
        'azure-core==1.30.2',
        'azure-identity==1.17.1',
        'azure-mgmt-core==1.4.0',
        'azure-mgmt-resource==23.1.1',
        'httpx==0.27.0',
        'numpy==2.0.0',
        'openai==1.35.0',
        'pandas==2.2.2',
        'pydantic==2.7.4',
        'python-dotenv==1.0.1',
        'requests==2.32.3',
        'pytest==8.2.2',
    ],
    entry_points={
        'console_scripts': [
            # Define command line scripts here if needed
        ],
    },
    author='Savin Ionut Razvan',
    author_email='razvan.i.savin@gmail.com',
    description='A flexible AI framework for managing OpenAI and Azure OpenAI interactions, with Retrieval-Augmented Generation capabilities.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SavinRazvan/flexiai',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
    ],
    python_requires='>=3.10',
    project_urls={
        'Bug Reports': 'https://github.com/SavinRazvan/flexiai/issues',
        'Source': 'https://github.com/SavinRazvan/flexiai',
    },
    cmdclass={
        'install': PostInstallCommand,
    },
)
