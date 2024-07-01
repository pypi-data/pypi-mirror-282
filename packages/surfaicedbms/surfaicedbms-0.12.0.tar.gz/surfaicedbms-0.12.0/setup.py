from setuptools import setup, find_packages


setup(
    name="surfaicedbms",
    version="0.12.0",
    author="Atahan Kap",
    author_email="atahan.kap@student.tuwien.ac.at",
    description="Surfaicedbms PyPi Version",
    long_description=open('README.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url="https://git.ift.tuwien.ac.at/lab/ift/sis/projects/surfaice/surfaice-dbms",
    packages=find_packages(),
    install_requires=[
        'iftaixpath>=0.0.2',
        'numpy',
        'pandas',
        'fpdf',
        'matplotlib',
        'pymongo',
        'psycopg2',
        'PyYAML'
    ],
    include_package_data=True,
    package_data={
        'surfaice-dbms': ['data/*.prt', 'data/*.csv', 'data/*.txt', 'data/*.yaml', 'data/*.csv.gz', 'data/*.pdf', 'data/*.ptp', 'data/*.json', 'data/*.log']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
