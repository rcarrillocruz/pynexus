from setuptools import setup

setup(name='pynexus',
      version='0.1',
      description='Python REST client for Sonatype Nexus',
      url='https://github.com/rcarrillocruz/pynexus',
      author='Ricardo Carrillo Cruz',
      author_email='ricardo.carrillo.cruz@gmail.com',
      license='Apache',
      packages=['pynexus', 'tests'],
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Topic :: Software Development :: Libraries',
                   'License :: OSI Approved :: Apache Software License'
                  ],
      test_suite='tests',
      )
