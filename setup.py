#!/usr/bin/env python


from setuptools import setup


setup(name='FlowSOM',
      version='0.1.2',
      url="https://github.com/krglkvrmn/FlowSOM",
      description='A Python implementation of FlowSOM algorithm for clustering and visualizing a mass cytometry data set. This repository is a fork, please refer to author of original repository for more information.',
      author='Sangyu Shen',
      author_email='sangyushen@gmail.com',
      packages=["flowsom"],
      package_dir={"flowsom": "script"},
      install_requires=['FlowCytometryTools', 'matplotlib', 'networkx', 'minisom', 'scikit-learn', 'numpy', 'pandas'],
      license='MIT',
      keywords=['flowsom', 'cytometry', 'machine learning', 'visualization', 'clustering', 'dimentionality reduction']
)
