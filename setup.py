from setuptools import setup
import mongobackup


setup(name='mongobackup',
      version=mongobackup.__version__,
      description=mongobackup.__description__,
      author=mongobackup.__author__,
      url='https://github.com/robintiwari/mongobackup',
      license=mongobackup.__license__,
      platforms=['all'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: Jython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: MongoDB backup and restore utility',
      ],
      py_modules=['mongobackup'],
      )
