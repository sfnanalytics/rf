# setup.py

from setuptools import setup

setup(
    name='sfn_recency_frequency',
    version='0.0.2',
    description='Recency + Frequency',
    py_modules=['recency_frequency'],
    package_dir={'': 'src'},
    url='https://github.com/pypa/sfn_recency_frequency',
    author='jweinapple@gmail.com',
    license='MIT',
    install_requires=[
        'requests',
        'pandas',
        'xlrd',
        'openpyxl'],
  #   install_requires=[
  #       'requests',
  #       pandas==1.2.1,
  #       xlrd==2.0.1,
  #       openpyxl==3.0.6],
  # # classifiers=["Programming Language :: Python :: 3.9"]
    # entry_points={
    #     'console_scripts' : [
    #         'mycommand = mymodule.script:main',
    #     ]
    # # },,
)