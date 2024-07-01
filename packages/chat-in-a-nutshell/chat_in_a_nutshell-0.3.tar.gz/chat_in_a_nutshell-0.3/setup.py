from setuptools import setup, find_packages
from setuptools.command.install import install
import sys

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        print("\n\nThank you for installing chat-in-a-nutshell! Enjoy using it!\n\n"
              "You can start chatting by: chat -m 'Your message.'\n"
              "Make sure you have set your OpenAI API key to OPENAI_API_KEY environment variable.\n")

setup(
    name='chat_in_a_nutshell',
    version='0.3',
    description="A terminal-based script for interacting with OpenAI's API.",
    packages=find_packages(),
    py_modules=['chat_openai'],
    entry_points={
        'console_scripts': [
            'chat=chat_openai:main',
        ],
    },
    python_requires='>=3.6',
    install_requires=[
        'openai~=1.35.7'
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
)