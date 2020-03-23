from setuptools import setup, find_packages

setup(
    name='so_chat_search',
    version='0.0.1',
    description='Simple RSS-based search for Stack Exchange / Stack Overflow chat',
    author='tripleee',
    author_email='tripleee@users.noreply.github.com',
    #url='',
    #license=['MIT', 'Apache'],
    platforms='all',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        'License :: OSI Approved :: Apache Software License',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],

    install_requires=['feedparser'],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'rss-search=rss_search:main',
            'ip-search=ip_search:main',
            'ns-search=ns_search:main',
            'phones=phones:main',
            'pharma-redirects=pharma_redirects_main',
            ]
    },
    #tests_require=
)
