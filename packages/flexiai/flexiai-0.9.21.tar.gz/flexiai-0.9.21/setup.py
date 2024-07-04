# setup.py
from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import shutil

# I need to make corrections here. I want to provide the user with files and folders after installing `pip install flexiai` 
# to enable RAG and help them start their project more easily. This way, they can focus on building assistants, functions 
# for them, teams of assistants, and more.
class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        project_root = os.path.abspath(os.getcwd())
        try:
            self.create_user_flexiai_rag_folder(project_root)
            self.copy_env_template(project_root)
            self.copy_requirements(project_root)
            self.create_logs_folder(project_root)
        except Exception as e:
            print(f"Post-installation step failed: {e}")


    def create_user_flexiai_rag_folder(self, project_root):
        """
        Create the 'user_flexiai_rag' folder in the project root directory and
        copy contents from the source directory if the folder does not already exist.

        Args:
            project_root (str): The root directory of the project.
        """
        src_folder = os.path.join(os.path.dirname(__file__), 'flexiai', 'user_flexiai_rag')
        dst_folder = os.path.join(project_root, 'user_flexiai_rag')

        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder)

        for filename in os.listdir(src_folder):
            src_file = os.path.join(src_folder, filename)
            dst_file = os.path.join(dst_folder, filename)
            if os.path.isfile(src_file) and not os.path.exists(dst_file):
                try:
                    shutil.copy2(src_file, dst_file)
                except IOError as e:
                    print(f"Failed to copy {src_file} to {dst_file}: {e}")


    def create_logs_folder(self, project_root):
        """
        Create the 'logs' folder in the project root directory if it does not already exist.

        Args:
            project_root (str): The root directory of the project.
        """
        log_folder = os.path.join(project_root, 'logs')
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

    def copy_file(self, src, dst):
        """
        Copy a file from the source path to the destination path if the file
        does not already exist.

        Args:
            src (str): The source file path.
            dst (str): The destination file path.
        """
        if os.path.isfile(src) and not os.path.exists(dst):
            try:
                shutil.copy2(src, dst)
            except IOError as e:
                print(f"Failed to copy {src} to {dst}: {e}")


    def copy_env_template(self, project_root):
        """
        Copy the .env.template file to the project root directory as .env
        if it does not already exist.

        Args:
            project_root (str): The root directory of the project.
        """
        src_file = os.path.join(os.path.dirname(__file__), '.env.template')
        dst_file = os.path.join(project_root, '.env')
        self.copy_file(src_file, dst_file)


    def copy_requirements(self, project_root):
        """
        Copy the requirements.txt file to the project root directory if it
        does not already exist.

        Args:
            project_root (str): The root directory of the project.
        """
        src_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
        dst_file = os.path.join(project_root, 'requirements.txt')
        self.copy_file(src_file, dst_file)


setup(
    name='flexiai',
    version='0.9.21',
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
    cmdclass={
        'install': PostInstallCommand,
    },
)
