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

	for movie in movies:
		try:
			movie_name = movie[:movie.find('.')].replace(' ', '+')
			info = json.load(urllib2.urlopen(OMDB_URL % movie_name))
			print '{0}: IMDB -> {1}'.format(info['Title'], info['imdbRating'])
		except:
			print 'Something happened with {0}'.format(movie_name)
			pass

def main():
	get_ratings(get_filenames())

if __name__ == '__main__':
	main()
