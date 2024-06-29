from setuptools import setup, find_packages

setup(
    name='pypi_upload_test',
    version='0.1',
    packages=find_packages(),
    description='A simple example package',
    # long_description=open('README.md').read(),
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/LunFengChen/pypi_upload_test',
    author='LunFengChen',
    author_email='1622246366@qq.com',
    license='MIT',
    install_requires=[
        # 依赖列表
    ],
    classifiers=[
        # 分类信息
    ]
)
