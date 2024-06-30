from setuptools import setup, find_packages

setup(
    name='chat_in_a_nutshell',
    version='0.1',
    packages=find_packages(),
    py_modules=['chat_openai'],
    entry_points={
        'console_scripts': [
            'chat=chat_openai:main',
        ],
    },
    install_requires=[
        'openai~=1.35.7',
        'numpy~=2.0.0',
        'sounddevice~=0.4.7',
        'pydub~=0.25.1'
    ],
)