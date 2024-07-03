from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="projects_ws_test",  # Název vašeho balíčku
    version="0.1.1",  # Počáteční verze
    author="Šmíd, Špánik",
    author_email="vase.email@example.com",
    description="ws projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spana21/projects_ws",
    packages=find_packages(include=['app', 'app.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.12',
    install_requires=[
        # Zde uveďte požadavky z requirements-dev.txt, např.
        'selenium',
        'python-dotenv',
        'numpy',
        'bs4',
        'requests'
    ],
)