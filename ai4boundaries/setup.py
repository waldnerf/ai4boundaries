import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ai4boundaries',
    version='0.0.1',
    author='Franz Waldner',
    author_email='francois.waldner.atwork@gmail.com',
    description='Utility package to download AI4Boundaries data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/waldnerf/ai4boundaries',
    project_urls={
        "Bug Tracker": "https://github.com/waldnerf/ai4boundaries/issues"
    },
    license='MIT',
    packages=['waldnerf'],
    install_requires=['requests', 'urllib', 'bs4', 'pathlib', 'tqdm'],
)
