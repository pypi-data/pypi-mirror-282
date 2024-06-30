from setuptools import setup

readme = open("./README.md", "r")


setup(
    name="ultramiko",
    packages=["ultramiko"],  # this must be the same as the name above
    version="0.1",
    description="Esta es la descripcion de mi paquete",
    long_description=readme.read(),
    long_description_content_type="text/markdown",
    author="Josue Villamar",
    author_email="",
    # use the URL to the github repo
    url="https://github.com/villamar32/ultramiko",
    download_url="https://github.com/villamar32/ultramiko/tarball/0.1",
    keywords=["network", "automation", "python"],
    classifiers=[],
    license="MIT",
    include_package_data=True,
)
