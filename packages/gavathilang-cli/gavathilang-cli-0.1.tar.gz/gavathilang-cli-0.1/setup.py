from setuptools import setup, find_packages

setup(
    name='gavathilang-cli',
    version='0.1',
    py_modules=['gavathilang_cli'],
    install_requires=[
        # Add any dependencies here if needed
    ],
    entry_points='''
        [console_scripts]
        gavathilang=gavathilang_cli:main
    ''',
    author="Sonu Vishwakarma",
    author_email="sonu.v.s.771984@gmail.com",
    description="A CLI tool for GavathiLang",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gavathilang-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
