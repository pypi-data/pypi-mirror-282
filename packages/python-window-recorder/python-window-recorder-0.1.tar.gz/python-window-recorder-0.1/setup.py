from setuptools import setup

setup(
    name = 'python-window-recorder',
    packages = ['window_recorder'],
    install_requires=['opencv-python', 'pywin32'],
    version = '0.1',
    description = 'Background window recorder',
    url = 'https://github.com/xjxckk/window-recorder/',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
    )