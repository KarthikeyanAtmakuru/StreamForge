import setuptools

setuptools.setup(
    name='streamforge-tests',
    version='3.3.0',

    author="KARTHIKEYAN ATMAKURU",
    author_email="karthikeyan.atmakuru33@gmail.com",

    description='Docker image tests',

    url="https://github.com/KarthikeyanAtmakuru",

    dependency_links=open("requirements.txt").read().split("\n"),

    packages=['test'],

    include_package_data=True,

    python_requires='>=2.7',
    setup_requires=['setuptools-git'],

)
