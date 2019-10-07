import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="pyDatahubDriver",
	version="0.1.1",
	author="King Abdullah Petroleum Studies and Research Center",
	author_email="anup.kumar@kapsarc.org",
	description="KAPSARC Datahub",
    keywords="model-data data-version modelers-data-version python jupyter ipython",
    install_requires=[
        "pandas",
        "requests"
    ],
	long_description=long_description,
	long_description_conent_type="text/markdown",
	url="https://github.com/kapsarc/pyDatahub",
	packages=['datahub'],
	package_dir={'datahub': 'datahub'},
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry"
	]
)