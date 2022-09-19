import setuptools

setuptools.setup(
    name='ai4boundaries',
    version='0.0.1',
    author='Franz Waldner',
    author_email='francois.waldner.atwork@gmail.com',
    description='Utility package to download AI4Boundaries data',
    long_description='Utility package to download AI4Boundaries data',
    long_description_content_type="text/markdown",
    url='https://github.com/waldnerf/ai4boundaries',
    project_urls={
        "Bug Tracker": "https://github.com/waldnerf/ai4boundaries/issues"
    },
    license='MIT',
    packages=['ai4boundaries'],
    install_requires=['requests', 'bs4', 'pathlib', 'tqdm'],
)
