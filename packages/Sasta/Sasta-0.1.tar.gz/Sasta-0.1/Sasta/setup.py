from setuptools import setup, find_packages

setup(
    name="Sasta",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'Sasta-cli=Sasta.cli:main',
        ],
    },
    install_requires=[
        # List your package dependencies here
    ],
    author="Sasta Hari Haran R",
    author_email="sastahariharn0567@gmail.com",
    description="Hi just introducing me through cmd",
    url="https://github.com/Sastahariharan567/Sasta",
)
