from setuptools import setup, find_packages

setup(
    name="bees-exam",
    version="0.1.0",
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Rodolfo Lotte',
    author_email='rodolfo.lotte@email.com',
    entry_points={
        'console_scripts': [
            # Add your console scripts here
        ],
    },
)
