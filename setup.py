from setuptools import setup, find_packages
import versioneer


def main():

    setup(name='msda',
          version=versioneer.get_version(),
          description='msda',
          long_description=(
              'DataRail is a framework for managing, transforming,'
              ' visualizing, and processing scientific data, in particular'
              ' that generated by high-dimensional multi-factorial'
              ' experimental designs.'
          ),
          author='Kartik Subramanian',
          author_email='kartik_subramanian@hms.harvard.edu',
          url='http://github.com/sorgerlab/msda',
          packages=find_packages(),
          install_requires=['numpy', 'pandas', 'xarray'],
          cmdclass=versioneer.get_cmdclass(),
          keywords=['systems', 'biology', 'data', 'array', 'matrix'],
          classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
            'Topic :: Scientific/Engineering :: Chemistry',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Scientific/Engineering :: Visualization',
            ],
          )


if __name__ == '__main__':
    main()
