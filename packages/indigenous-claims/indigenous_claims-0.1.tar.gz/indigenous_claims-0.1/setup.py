from setuptools import setup, find_packages

setup(
    name='indigenous_claims',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'indigenous_claims=indigenous_claims.indigenous_claims:main',
        ],
    },
    package_data={
        'indigenous_claims': ['Complete_Indigenous_Land_Claims_and_Lawsuits.csv'],
    },
)
