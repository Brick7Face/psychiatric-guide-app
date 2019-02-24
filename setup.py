import re
import os

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name="Psychiatric Guide",
    version="1.0",
    description="Implements the Prescribers Guide 2012",
    long_description="Implements prescribing algorithms for depression, bipolar, and their corresponding forms.",
    author="Bryan Plant, Keely Weisbeck, Madison Fichtner, Alex Harry, Nate Tranel",
    author_email="njtranel@gmail.com",
    url="https://github.com/Brick7Face/psychiatric-guide-app",
    download_url="https://github.com/Brick7Face/psychiatric-guide-app.git",
    license="MIT License",
    packages=[],
    include_package_data=True,
    install_requires=[
        "Django>=1.7.0",
    ],
    tests_require=[
        "nose",
        "coverage",
    ],
    zip_safe=False,
    test_suite="tests.runtests.start",
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)

