#!/usr/bin/env python
from setuptools import setup, find_packages



setup(
	name='djangobb_forum',
	version='0.1',
	description='DjangoBB is a quick and simple forum which uses the Django Framework.',
	license='BSD',
	url='https://github.com/hemebond/djangobb',
	author='Alexey Afinogenov, Maranchuk Sergey, James O\'Neill',
	author_email='James O\'Neill <hemebond@gmail.com>',
	packages=find_packages(),
	include_package_data=True,
	install_requires=open('requirements.txt').readlines(),
	keywords='django forum bulletinboard',
	classifiers=[
		'Framework :: Django',
		'Framework :: Django :: 3.0',
		'License :: OSI Approved :: BSD License',
		'Natural Language :: English',
	],
)
