from setuptools import setup, find_packages

setup(
    name='pygitloc',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'GitPython',
        'PyGithub'
    ],
    entry_points={
        'console_scripts': [
            'pygitloc = pygitloc.main:main'
        ]
    },
    author='Shubham Shinde',
    author_email='shubhamshindesunil@gmail.com',
    description='A package to calculate lines of code from a GitHub repository link',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pygitloc',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
