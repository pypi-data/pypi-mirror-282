from setuptools import setup

setup(
    name='keepintouch',
    version='1.0.2',
    author='Xizhen Du',
    author_email='xizhendu@gmail.com',
    url='https://github.com/xizhendu/keepintouch-sdk-python',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    description='Simple Python client library for https://httpbin.cn/kit',
    # packages=['thedns'],
    install_requires=[
        "requests",
    ]
)
