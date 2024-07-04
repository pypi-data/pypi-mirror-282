from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
setup(
    name='Python123',
    version='1.0.6',
    keywords='Python123',
    description='Python123 平台',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT License',
    url='https://github.com/Python123-io/Python123',
    author='XuehangCang',
    author_email='xuehangcang@outlook.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[
        'requests~=2.32.3',
        'tqdm~=4.66.4',
        'loguru~=0.7.2',
        'markdownify~=0.12.1'
    ],
)