from distutils.core import setup

setup(
    # Application name:
    name="base-crm-api-client",

    # Version number (initial):
    version="0.1.0",

    # Packages
    packages=["base_api"],

    # Include additional files into the package
    include_package_data=True,

    # Dependent packages (distributions)
    install_requires=[
    ],
)
