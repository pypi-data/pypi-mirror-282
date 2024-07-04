from setuptools import setup, find_packages

setup(
    name='IndianSuryaSearchEngine',
    version='0.01',
    author='Suraj Sharma',
    author_email='surajsharma963472@gmail.com',
    description='Hi, are you ready for experiencing the first Indian search engine "Surya"? I know it is not that advanced, but it is my first module. Here are all the functions of my search engine: search different search engine results to give you results on one engine, read aloud function for those who want to hear it in English right now, which also looks good.',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'PyQt5',
        'pyttsx3',
        'qtwidgets',
        'PyQtWebEngine'
    ],
)
