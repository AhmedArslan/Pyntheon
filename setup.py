#!/usr/bin/env python

import os
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
		name = "Pyntheon",

		version = "0.1",

		description = "An automated tool to map mutations to Post Translational Modifitcaions (PTMs)",

		url = "https://github.com/AhmedArslan/ptmAction",

		author = "Ahmed Arslan",

		author_email = "ahmed.arslan@kuleuven.be",

		maintainder = "Ahmed Arslan",

		license = "MIT",

		long_desciption = read("README.md"),

		keywords = (

			'Bioinformatics',

			'Protein variants',

			'PTMs',

			'Protein functoinal regions',

			'UniMap',

			),

		classifiers=[ 
		'Intended Audience :: Science/Research',
		'Topic :: Education',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
    	'Programming Language :: Python :: 3',
    	'Programming Language :: Python :: 3.3',
    	'Programming Language :: Python :: 3.4',
    	'Programming Language :: Python :: 3.5',
    	],

    	packages = ['pyntheon'],

    	include_package_data = True,

    	zip_safe = False,

    	entry_points={
        	'console_scripts': [
            
            		'pyntheon = pyntheon.pyntheon:pyn'


        ],
    }
)

