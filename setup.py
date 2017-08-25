from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='soundtest',
      version='1.1.0',
      description='play sounds on windows',
      long_description=readme(),
      keywords='',
      url='http://github.com/eric-s-s/sound_test',
      author='Eric Shaw',
      author_email='shaweric01@gmail.com',
      license='MIT',
      classifiers=[
        'Development Status :: 4 - Beta',
        "Operating System :: Windows",
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
      ],
      packages=['soundtest'],
      entry_points={
          'console_scripts': ['soundtest=soundtest.soundtest:main',
                              'hearingtest=soundtest.hearingtest:hearing_test'],
      },
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
