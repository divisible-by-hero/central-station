from setuptools import setup, find_packages

version = '0.1dev'

setup(name='django-central-station',
      version=version,
      description="Project tracking",
      long_description="",
      classifiers=[
          "Development Status :: 1 - Planning",
          "Environment :: Web Environment",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='',
      author='Derek Stegelman',
      author_email='dstegelman@gmail.com',
      url='http://github.com/dstegelman/central-station',
      license='MIT',
      packages=find_packages(),
      install_requires = ['django', 'south', 'sorl-thumbnail', 'django-tastypie'],
      include_package_data=True,
      zip_safe=False,
    )