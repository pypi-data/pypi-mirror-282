from setuptools import setup, find_packages

setup(
    name='vaibhav_function_tester',
    version='0.2.0',
    author='Vaibhav Rokde',
    author_email='vaibhavrokde232@gmail.com',
    description='A package to test functions with given inputs and expected outputs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vaibhav-rokde/function_tester',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'function_tester=vaibhav_function_tester.cli:main',  # Update entry point
        ],
    },
)
