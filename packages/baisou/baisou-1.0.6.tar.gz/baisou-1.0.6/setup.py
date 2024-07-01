from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='baisou',
    version='1.0.6',
    description='The Baidu Searcher On Python|Python 百度搜索工具',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Python学霸',
    author_email='python@xueba.com',
    py_modules=['baisou'],
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'sou=baisou:sou']
    }
)