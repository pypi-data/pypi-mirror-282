from setuptools import setup, find_packages

setup(
    name='TamilLexicheck',
    version='1.0.12',
    packages=find_packages(),
    package_data={
        'TamilLexicheck': ['words.pickle'],  # Adjust the path as per your actual directory structure
    },
    install_requires=[
        # List your dependencies here
    ],
    author='raamkishore',
    author_email='raamkishore@megalai.com',
    description='Tamil Lexicheck is an open-source project aimed at providing a tool for identifying and suggesting corrections for misspelled words in Tamil text. This project is licensed under the Apache License 2.0.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Raam-kishore/TamilLexicheck-public-.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


