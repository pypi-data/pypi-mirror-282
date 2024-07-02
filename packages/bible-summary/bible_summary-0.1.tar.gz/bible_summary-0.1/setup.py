from setuptools import setup, find_packages

setup(
    name="bible_summary",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    description="A package for summarizing Bible books",
    author="Riki Morohashi",
    author_email="rikimorohashi@gmail.com",
    url="https://github.com/rikim811/bible_summary",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
