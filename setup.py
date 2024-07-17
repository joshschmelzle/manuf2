from setuptools import setup

README = open("./README.md", "r").read()

REQUIREMENTS = open("./requirements.txt", "r").read().splitlines().strip()
    
setup(
    name="manuf2",
    packages=["manuf2"],
    version="2.0.1",
    description="Parser library for Wireshark's OUI database",
    author="Josh Schmelzle, Michael Huang",
    url="https://github.com/joshschmelzle/manuf2",
    license="Apache License 2.0 or GPLv3",
    keywords=["manuf2", "mac address", "networking"],
    entry_points={
        "console_scripts": ["manuf2=manuf2.manuf:main"],
    },
    package_data={"manuf2": ["manuf"]},
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=REQUIREMENTS,
)

# To publish package run:
# $ rm -rf dist #Delete all previous build that you might not want to upload
# $ python setup.py build check sdist bdist_wheel #Build
# $ twine upload --verbose dist/* #Upload
