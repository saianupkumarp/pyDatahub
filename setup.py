import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="pyDatahub",
	version="0.1",
	author="King Abdullah Petroleum Studies and Research Center",
	author_email="anup.kumar@kapsarc.org",
	description="KAPSARC Datahub",
	long_description=long_description,
	long_description_conent_type="text/markdown",
	url="https://github.com/kapsarc/pyDatahub",
	packages=['pyDatahub'],
	package_dir={'Datahub': 'SMP'}
	classifiers=[
		'Development Status :: 3 - Alpha',
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent"
	]
)