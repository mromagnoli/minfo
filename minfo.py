#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Marce Romagnoli"
__copyright__ = "Copyright 2015"
__version__ = "0.1"
__email__ = "marce.romagnoli@gmail.com"

from os import listdir

import urllib2
import json
import sys
import argparse

def get_filenames():
	""" Retrieve current directory filenames.

	Returns:
		A list with file names
	"""
	from os.path import isfile, join
	CURRENT_DIR = '.'
	files = [ f for f in listdir(CURRENT_DIR) if isfile(join(CURRENT_DIR, f)) ]
	return files


def get_ratings(movies):
	""" Get movie ratings.

	Args:
		movies: List of movies names
	Returns:
		void
	"""
	if movies is None:
		print "There's no movies here, bro."
		return

	OMDB_URL = 'http://www.omdbapi.com/?t=%s&y=&plot=short&r=json';
	print 'Retrieving data, please wait...'
#	movies = ['speed', 'frozen.srt', 'zoolander.srt', 'speed.mkv'] # Test

	movies = uniquify(movies)
	for movie in movies:
		try:
			movie_name = movie.replace(' ', '+')
			info = json.load(urllib2.urlopen(OMDB_URL % movie_name))
			print '{0}: IMDB -> {1}'.format(info['Title'], info['imdbRating'])
		except KeyboardInterrupt:
			print ' Leaving... Bye.'
			sys.exit()
		except:
			print 'Something happened retrieving "{0}" ratings. Better check your spell ;)'.format(movie)
			pass

def uniquify(items):
	""" Remove already set items in a list.
	Also remove extension from files.

	Args:
		items: List of items
	Returns:
		list of uniquify items
	"""
	_items = []
	for item in items:
		if item.find('.') != -1:
			_items.append(item[:item.find('.')])
		else:
			_items.append(item)

	return list(set(_items))

def manage_args():
	""" Manage arguments from console.
	"""
	parser = argparse.ArgumentParser(description = 'Get your directory movies ratings without check\'em one each by hand!')
	parser.add_argument('-m', '--movie', help = 'The movie name. Could be several movies comma-separated', required = False)
	return parser.parse_args()

def main():
	args = manage_args()
	if not args.movie is None:
		movies = args.movie.split(',')
	else:
		movies = get_filenames()

	get_ratings(movies)

	sys.exit(0)

if __name__ == '__main__':
	main()
