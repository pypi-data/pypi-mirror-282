from setuptools import setup, find_packages

setup(
    name='esp-helper',
    version='0.0.6',
    packages=find_packages(),
    install_requires=[
        'click==8.1.7',
        'requests==2.32.3',
        'beautifulsoup4==4.12.3',
        'pathlib==1.0.1',
        'urllib3==2.2.2',
    ],
    author='Jake Barbieur',
    author_email='barbieur@gmail.com',
    description='A helper application for ESP development',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/jake-barbieur/esp-helper',
    entry_points={
        'console_scripts': [
            'esp-helper = esp_helper.main:main',
        ],
    },
)
