from os import listdir

import urllib2
import json

import sys

def get_filenames():
	from os.path import isfile, join
	CURRENT_DIR = '.'
	files = [ f for f in listdir(CURRENT_DIR) if isfile(join(CURRENT_DIR, f)) ]
	return files

def get_ratings(movies):
	OMDB_URL = 'http://www.omdbapi.com/?t=%s&y=&plot=short&r=json';
	print 'Retrieving data, please wait...'

	movies = uniquify(movies)
	for movie in movies:
		try:
			movie_name = movie.replace(' ', '+')
			info = json.load(urllib2.urlopen(OMDB_URL % movie_name))
			print '{0}: IMDB -> {1}'.format(info['Title'], info['imdbRating'])
		except KeyboardInterrupt:
			print 'Leaving... Bye.'
			sys.exit()
		except:
			print 'Something happened with {0}'.format(movie_name)
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

def main():
	get_ratings(get_filenames())
	sys.exit(0)

if __name__ == '__main__':
	main()
