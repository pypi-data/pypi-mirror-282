from setuptools import setup, find_packages

setup(
    name='StateVector',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            # Define any command-line scripts here
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A vector database optimized for cosine similarity using quantum algorithms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/crystal-tensor/StateVector',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
