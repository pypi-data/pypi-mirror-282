import setuptools

setuptools.setup(
    name="xfarm",
    version="0.0.0",
    author="Pwnzer0tt1",
    author_email="pwnzer0tt1@poliba.it",
    scripts=[],
    install_requires=["exploitfarm"],
    include_package_data=True,
    description="Exploit Farm client alias to exploitfarm on pypi",
    long_description="# Exploit Farm client - alias to 'exploitfarm' on pypi",
    long_description_content_type="text/markdown",
    url="https://github.com/pwnzer0tt1/exploitfarm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
