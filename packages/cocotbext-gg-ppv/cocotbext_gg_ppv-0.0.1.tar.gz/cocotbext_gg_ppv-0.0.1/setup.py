# Minimal setup.py. Extend as needed.
from setuptools import setup, find_namespace_packages

setup(name = 'cocotbext-gg_ppv',
      version = '0.0.1',
      packages = find_namespace_packages(include=['cocotbext.*']),
      install_requires = ['cocotb', 'scapy'],
      python_requires = '>=3.6',
      classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Framework :: cocotb"])