from setuptools import setup

setup(name='pydato',
      version='0.112',
      description='The tidyverse in Python',
      url='https://github.com/gfleetwood/pydata',
      author='Gorrdon Fleetwood',
      author_email='gfleetwood@protonmail.com',
      license='MIT',
      packages=['pydato'],
      install_requires=[
            "scikit-learn==0.19.1",
            "plotnine==0.3.0",
            "numpy==1.14.0",
            "matplotlib==2.1.2",
            "pandas==0.22.0",
      ],
      zip_safe=False)
