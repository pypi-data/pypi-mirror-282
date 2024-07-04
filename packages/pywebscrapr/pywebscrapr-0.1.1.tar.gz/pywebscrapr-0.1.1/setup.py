from setuptools import setup, find_packages

setup(
    name='pywebscrapr',
    version='0.1.1',
    author='Infinitode Pty Ltd',
    author_email='infinitode.ltd@gmail.com',
    description='An open-source Python library for web scraping tasks.',
    long_description='An open-source Python library for web scraping tasks. Includes support for both image scraping and text scraping.',
    long_description_content_type='text/markdown',
    url='https://github.com/infinitode/pywebscrapr',
    packages=find_packages(),
    install_requires=[
        'requests',
        'bs4',
        'pillow'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.6',
)
