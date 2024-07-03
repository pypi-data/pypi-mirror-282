from setuptools import setup, find_packages
import os

with open("README.md", "r") as fh:
    long_description = fh.read()
def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append((path, [os.path.join(path, filename)]))
    return paths

setup(
    name='chatbot_code',
    version='0.3.15',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'manage.py = chatbot.manage:main',
            'configure-aws = chatbot.scripts.configure_aws:main',
            'readme = chatbot.scripts.readme:main',
        ],
    },
    package_data={
        'app1': ['static/*', 'templates/*', 'templatetags/*'],
    },
    # data_files=[
    #     ('', ['README.md', 'manage.py', 'requirements.txt', 'static/*']),
    # ],
    data_files = package_files('static') + [('', ['README.md', 'manage.py', 'requirements.txt','validate_api_key.py'])],
    
    author='Swati Saini',
    author_email='swati@mixorg.com',
    description='A Django app for chatbot functionality.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/saini2001/chatbot_code',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3.11',
    ],
)
