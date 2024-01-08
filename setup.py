from setuptools import setup, find_packages

setup(
    name='fuzzy_search',
    version='0.1.0',
    author='Sebas Pastor',
    author_email='sebas@cubyc.com',
    description='Fuzzy string matching functions using thefuzz library.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/spastorferrari/fuzzy-search',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'thefuzz'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)