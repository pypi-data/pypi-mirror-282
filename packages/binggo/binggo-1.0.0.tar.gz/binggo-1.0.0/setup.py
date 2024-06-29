from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='binggo',
    version='1.0.0',
    description='The Bing Searcher On Python|Python Bing搜索工具',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Python学霸',
    author_email='python@xueba.com',
    py_modules=['binggo'],
    install_requires=['mechanicalsoup'],
    entry_points={
        'console_scripts': [
            'go=binggo:go','image=binggo:image']
    }
)