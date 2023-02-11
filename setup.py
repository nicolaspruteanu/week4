from setuptools import setup, find_packages

setup(
    name="comp0034-week4",
    version="1.0",
    description="Activies and apps for COMP0034 week 4",
    packages=find_packages(
        where="src"
    ),  # Looks for packages in the src folder. Any folders without an init.py will be ignored
    package_dir={"": "src"},
    include_package_data=True,  # automatically install any data files found
    install_requires=[
        "dash",
        "pandas",
        "dash-bootstrap-components",
        "plotly",
        "colorlover",
    ],
)
