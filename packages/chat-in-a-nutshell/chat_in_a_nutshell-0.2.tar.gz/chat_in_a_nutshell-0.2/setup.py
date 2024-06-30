from setuptools import setup, find_packages

setup(
    name='chat_in_a_nutshell',
    version='0.2',
    packages=find_packages(),
    py_modules=['chat_openai'],
    entry_points={
        'console_scripts': [
            'chat=chat_openai:main',
        ],
    },
    install_requires=[
        'openai~=1.35.7'
    ],
)