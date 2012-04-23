from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.2'

install_requires = [
    'collective.contentleadimage',
]


setup(name='collective.slidernavigation',
    version=version,
    description="Provides a jQuery slider navigation viewlet",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='',
    author='Maik Derstappen',
    author_email='maik.derstappen@inqbus.de',
    url='https://github.com/collective/collective.slidernavigation',
    license='GPL',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['collective.slidernavigation=collective.slidernavigation:main']
    }
)
