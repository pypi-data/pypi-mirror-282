# setup.py
from setuptools import setup, find_packages

setup(
    name='flexiai',
    version='0.9.23',
    packages=find_packages(include=['flexiai', 'flexiai.*']),
    include_package_data=True,
    package_data={
        'flexiai': [
            'assistant/*.py',
            'config/*.py',
            'core/*.py',
            'core/utils/*.py',
            'docs/*.md',
            'examples/*.ipynb',
            'examples/*.py',
            'logs/*.log',
            'tests/*.py',
            'user_flexiai_rag/*.py',
            'user_flexiai_rag/data/*.csv',
            '.env.template',
            'requirements.txt'
        ],
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
        'setuptools>=70.2.0',
    ],
    entry_points={
        'console_scripts': [
            # Define command line scripts here if needed
        ],
    },
    author='Savin Ionut Razvan',
    author_email='razvan.i.savin@gmail.com',
    description='FlexiAI is a versatile and powerful AI framework designed to streamline the integration and management \
                of OpenAI and Azure OpenAI services. With advanced Retrieval-Augmented Generation (RAG) capabilities,  \
                FlexiAI enables developers to build sophisticated AI-driven applications efficiently and effectively.',
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
)
