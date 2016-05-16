from setuptools import setup

setup(
    name='releasewarrior',
    version='0.1.0',
    packages=['releasewarrior'],
    entry_points={
        'console_scripts': [
            'release = releasewarrior.__main__:main'
        ]
    },
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
