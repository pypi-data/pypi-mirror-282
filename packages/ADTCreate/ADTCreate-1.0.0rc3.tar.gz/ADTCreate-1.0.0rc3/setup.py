from setuptools import setup, find_packages

setup(
    name="ADTCreate",
    version="1.0.0rc3",
    packages=find_packages(), 
    install_requires=[
        "Levenshtein>=0.23.0",
        "numpy>=1.21.6",
    ],
    python_requires=">=3.7",
    author="Jayme Hebinck",
    author_email="jayme.hebinck@live.nl",
    description="ADT Create provides a general method to create and customize Attack-Defense Trees (ADTs), allowing users to visualize and analyse security scenarios. A user is able to create and customize ADTs from scratch, upload/download ADTs in XML format, generate ADTerms based on ADTs, compare ADTerms to determine equivalence using an equivalence threshold using the Levenshtein Distance, determine satisfiability of an ADT and generate statistics of an ADT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MainJay/ADTPythonLibrary/",
    project_urls={
        'Tracker': "https://github.com/MainJay/ADTPythonLibrary/issues",
    },
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)