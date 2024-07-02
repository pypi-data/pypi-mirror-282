from setuptools import setup, find_packages

setup(
    name="bible_summary",
    version="0.1.3",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'bible_summary': ['data/*.json'],
    },
    description="A package for summarizing Bible books",
    author="Your Name",
    author_email="rikimorohashi@gmail.com",
    url="https://github.com/rikim811/bible_summary-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'bible-summary=bible_summary.summary:main',
        ],
    },
)
