from setuptools import setup, find_packages

setup(
    name='random_quote_cli',
    version='1.0.4',
    description='A CLI tool to fetch and display random quotes, with an option to send them to a WebSocket server.',
    long_description='README.md',
    long_description_content_type='text/markdown',
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
