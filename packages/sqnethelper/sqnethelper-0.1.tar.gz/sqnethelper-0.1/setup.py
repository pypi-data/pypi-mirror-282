from setuptools import setup, find_packages

setup(
    name='sqnethelper',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'aliyun-python-sdk-core',
        'aliyun-python-sdk-ecs',
    ],
    entry_points='''
        [console_scripts]
        sqnethelper=sqnethelper.cli:cli
    ''',
)