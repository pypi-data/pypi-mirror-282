import os
import shutil
from distutils.sysconfig import get_python_lib

def create_user_flexiai_rag_folder():
    """
    Creates the 'user_flexiai_rag' folder in the current working directory and copies files from 
    the site-packages 'flexiai/user_flexiai_rag' directory to the newly created folder.

    This function ensures that the user-defined task management and function mapping files are 
    available in the working directory.

    Steps:
        1. Determines the path to the site-packages directory.
        2. Constructs the source and destination folder paths.
        3. Creates the destination folder if it doesn't exist.
        4. Copies files from the source folder to the destination folder.

    Returns:
        None
    """
    site_packages_path = get_python_lib()
    src_folder = os.path.join(site_packages_path, 'flexiai', 'user_flexiai_rag')
    dest_folder = os.path.join(os.getcwd(), 'user_flexiai_rag')

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created directory: {dest_folder}")

    for filename in os.listdir(src_folder):
        src_file = os.path.join(src_folder, filename)
        dest_file = os.path.join(dest_folder, filename)
        if os.path.isfile(src_file):
            shutil.copy(src_file, dest_file)
            print(f"Copied {src_file} to {dest_file}")

def create_env_file():
    """
    Creates a '.env' file in the current working directory with the provided content.

    This function ensures that the environment configuration file is available in the working directory.

    Returns:
        None
    """
    env_content = """# ========================== #
                    # Example .env file template #
                    # ========================== #

                    # Your OpenAI API key
                    OPENAI_API_KEY='your_openai_api_key_here'

                    # Your Azure OpenAI API key
                    AZURE_OPENAI_API_KEY='your_azure_openai_api_key_here'
                    # Your Azure OpenAI endpoint
                    AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint_here'
                    # Azure OpenAI API version
                    AZURE_OPENAI_API_VERSION='2024-05-01-preview'

                    # Credential type (either 'openai' or 'azure')
                    CREDENTIAL_TYPE='openai'
                    """

    dest_file = os.path.join(os.getcwd(), '.env')
    if not os.path.exists(dest_file):
        with open(dest_file, 'w') as file:
            file.write(env_content)
            print(f"Created .env file at: {dest_file}")

if __name__ == "__main__":
    create_user_flexiai_rag_folder()
    create_env_file()
