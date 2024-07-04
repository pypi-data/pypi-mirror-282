from setuptools import setup, find_packages

setup(
    name='Vinted_api_scraper',  # Nouveau nom de votre projet
    version='0.3.0',
    packages=find_packages(),
    install_requires=[
        # Listez ici les dépendances nécessaires, par exemple :
        # 'requests',
    ],
    author='Simon BEGUIN',
    author_email='simon.beguin7@gmail.com',
    description='Une description de votre bibliothèque',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/simonbeguin/Vinted_api_scraper',  # Lien vers votre dépôt GitHub ou autre
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
