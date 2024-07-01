from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='nekosia.py',
  version='1.0.0',
  description='api nekosia',
  long_description=open('README.rst').read(),
  url='',  
  author='ubijacz',
  author_email='neczko05@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='nekosia api anime',
  packages=find_packages(),
  install_requires=['requests','easy-pil', 'discord.py'] 
)