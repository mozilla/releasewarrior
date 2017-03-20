from setuptools import setup

requirements = open("requirements.txt").readlines()

setup(
    name='releasewarrior',
    version='0.1.0',
    packages=['releasewarrior'],
    entry_points={
        'console_scripts': [
            'release = releasewarrior.__main__:main'
        ]
    },
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
