from setuptools import setup

setup(name='json-recipes',
      version='0.1',
      description='Find anagrams in tweets',
      url='http://github.com/killakam3084/recipes.git',
      author='Cameron Rison',
      author_email='cameron.rison@utexas.edu',
      license='MIT',
      packages=['recipes'],
      scripts=['bin/recipes-to-json'],
      zip_safe=False)
