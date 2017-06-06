#!/usr/bin/env python
from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session='hack')
reqs = [str(ir.req) for ir in install_reqs]

setup(name='Python Experiment Suite',
      version='0.1',
      author='Thomas Rückstieß'
      description='A Python experiment suite',
      packages=['expsuite'],
      install_requires=reqs,
)
