from setuptools import setup, find_packages
import setuptools
setup(
    name='Vinted_api_scraper',  # Nouveau nom de votre projet
    version='0.5.0',
    author='Simon BEGUIN',
    author_email='simon.beguin7@gmail.com',
    description='Vinted API wrapper for python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/simonbeguin/Vinted_api_scraper',  # Lien vers votre dépôt GitHub ou autre
    install_requires=["requests"],
    keywords=["python", "Vinted api", "Vinted API wrapper", "python vinted"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6"
    )
