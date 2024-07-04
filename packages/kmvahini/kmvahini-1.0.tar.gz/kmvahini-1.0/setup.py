from setuptools import setup, find_packages  # type: ignore

setup(
    name='kmvahini',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'pandas',
        'lxml',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'run_scraper=kmvahini.scraper:main',
        ],
    },
    author='Manojkumar Patil',
    author_email='patil.manojkumar@hotmail.com',
    description='Fetch Price data from Krishimaratvahini website',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/patilmanojkumar/kmvahini',
    project_urls={
        'Source': 'https://github.com/patilmanojkumar/kmvahini',
        'Bug Reports': 'https://github.com/patilmanojkumar/kmvahini/issues',
    },
    license='MIT',
)
