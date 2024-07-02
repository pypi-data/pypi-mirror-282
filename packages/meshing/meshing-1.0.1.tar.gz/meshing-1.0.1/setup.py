from setuptools import setup

setup(
    name='meshing',
    version='1.0.1',
    author='Xizhen Du',
    author_email='xizhendu@gmail.com',
    url='https://github.com/xizhendu/meshing-sdk-python',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    description='Simple Python client library for https://devnull.cn/meshing',
    # packages=['thedns'],
    install_requires=[
        "requests",
    ]
)
