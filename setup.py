from setuptools import setup

exec(open('ecospold2matrix_mod/version.py').read())

setup(
    name='ecospold2matrix_mod',
    packages=['ecospold2matrix_mod', ],
    version=__version__,
    author='Guillaume Majeau-Bettez',
    author_email="guillaume.majeau-bettez@ntnu.no",
    description="Class for recasting Ecospold2 LCA dataset into Leontief matrix representations or Supply and Use Tables",
    license=open('LICENSE.txt').read(),
    long_description=open('README.md').read(),
    url='https://github.com/majeau-bettez/ecospold2matrix',
    install_requires=['numpy >= 1.11.0',
                     'lxml',
                     'nose >= 1.3.7',
                     'pandas >= 0.18.0',
                     'python-dateutil >= 2.5.3',
                     'scipy >= 0.17.0',
                     'six >= 1.10.0',
                     'xlrd >= 0.9.4',
                     'xlwt >= 1.0.0'],
    data_files=[('parameters', ['ecospold2matrix_mod/parameters/cas_conflicts.csv',
                                'ecospold2matrix_mod/parameters/custom_factors.csv',
                                'ecospold2matrix_mod/parameters/synonyms.csv']),
                ('', ['LICENSE.txt', 'README.md']),
                ],
    include_package_data=True,
)
