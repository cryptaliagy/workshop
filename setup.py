from setuptools import setup, find_packages


setup(
    name='workshop',
    author='Natalia Maximo',
    author_email='iam@natalia.dev',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['click'],
    tests_require=['pytest', 'flake8', 'mypy', 'pytest-cov'],
    extras_require={
        'tests': ['pytest', 'flake8', 'mypy', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': ['workshop = workshop.main:main']
    },
)
