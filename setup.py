from __future__ import ( print_function, with_statement, absolute_import )
import sys
# When possible, use distribute_setup's version of tools
try:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
except ImportError:
    from setuptools import setup, find_packages
if sys.version >= '2.3':
  import re, os, sys
  version = re.search(
        "__version__.*'(.+)'",
        open(os.path.join('lazythreats','__init__.py')).read()).group(1)
else:
    raise Exception("only python 2.3 or newer supported")

setup(
    name='lazythreats',
    version= version,
    description='Module for farming opensource threat intelligence',
    author='Shomiron Das Gupta',
    author_email='shomiron@netmonastery.com',
    url='https://github.com/shomiron/lazythreats#lazythreats',
    packages=find_packages(where='.'),
    include_package_data=True,
    zip_safe=False,
    scripts=['scripts/lazythreats1','scripts/lazythreats2',],
    entry_points={
        'console_scripts': [ 'lazythreats3= lazythreats:command_line_runner',]  },
)
   
