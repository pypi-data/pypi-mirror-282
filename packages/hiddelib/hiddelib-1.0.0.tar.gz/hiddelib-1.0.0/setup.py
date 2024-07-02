import setuptools
with open(r'D:\scripts\hiddenlib\hiddenlib\README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='hiddelib',
	version='1.0.0',
	author='agenthiddenoriginal',
	author_email='tejajat421@joeroc.com',
	description='hiddentool inc',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/SuperZombi/Pypi-uploader',
	packages=['hiddenlib'],
	include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)