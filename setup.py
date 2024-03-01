from setuptools import setup, find_packages

setup(
    name='telegram_bot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'aiogram',
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'telegram_bot = telegram_bot.__main__:main'
        ]
    },
)
