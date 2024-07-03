# post_install.py
import os
import shutil

def create_user_flexiai_rag_folder():
    src_folder = os.path.join(os.path.dirname(__file__), 'flexiai', 'user_flexiai_rag')
    dst_folder = os.path.join(os.path.expanduser("~"), 'user_flexiai_rag')

    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    for filename in os.listdir(src_folder):
        src_file = os.path.join(src_folder, filename)
        dst_file = os.path.join(dst_folder, filename)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)

def copy_file(src, dst):
    if os.path.isfile(src):
        shutil.copy2(src, dst)

def copy_env_template():
    src_file = os.path.join(os.path.dirname(__file__), '.env.template')
    dst_template_file = os.path.join(os.path.expanduser("~"), '.env.template')
    dst_env_file = os.path.join(os.path.expanduser("~"), '.env')
    
    copy_file(src_file, dst_template_file)
    
    # Create .env file from .env.template if it doesn't exist
    if not os.path.exists(dst_env_file):
        shutil.copy2(src_file, dst_env_file)

def copy_requirements():
    src_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    dst_file = os.path.join(os.path.expanduser("~"), 'requirements.txt')
    copy_file(src_file, dst_file)

if __name__ == "__main__":
    create_user_flexiai_rag_folder()
    copy_env_template()
    copy_requirements()
