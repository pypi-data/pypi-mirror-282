from setuptools import setup, find_packages
import io
import typing


def read_requirements() -> typing.List:
    with open("requirements.txt", "r+") as file:
        requirements = [line.strip() for line in file.readlines()]
    return requirements


setup(name='genomics-product',
      description='Genomics Product',
      long_description=io.open('README.md', encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      version='1.0.0',
      author='InstaDeep Genomics',
      author_email='genomics_product@instadeep.com',
      url='https://github.com/instadeepai/genomics-product-sdk',
      packages=find_packages(),
      install_requires=read_requirements(),
      scripts=[],
      entry_points={'console_scripts': ['genomics=genomics.__main__:main']},
      zip_safe=False,
      include_package_data=True,
      test_suite='tests')
