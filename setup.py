import setuptools

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

setuptools.setup(
    name="fuckfuncap",
    author="accusable",
    description="An audio-solving python funcaptcha solving module",
    url="https://github.com/accusable/funcaptcha-solver",
    packages=setuptools.find_packages(),
    classifiers=[],
    install_requires=requirements,
    include_package_data=True,
    version="1.0.3"
)
