from setuptools import setup, find_packages

setup(
    name='random_quote_cli',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'websockets',
    ],
    entry_points={
        'console_scripts': [
            'random-quote-cli = random_quote.cli:main',
        ],
    },
)
