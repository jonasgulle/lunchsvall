import augustas
import bilbiten
import bryners
import delinorr
import estreet
import traktoren
import gardshuset
import himlabadet
import fernaeus
import nojet
import oasen
import opus
import invito
import kalabra
import knaust
import lacodicomo
import lunchguide
import mittgastronomi
import mokajen
import norrlandskallaren
import svartviksherrgard
import skonsmon
import tantanci
import dolcetto
import max
import wretmans
import brandstation

import sys, traceback
import simplejson as json

def get_scrapers():
	return [
		oasen,
		opus,
		invito,
		augustas,
		nojet,
		bryners,
		mokajen,
		tantanci,
		estreet,
		traktoren,
		delinorr,
		gardshuset,
		himlabadet,
		fernaeus,
		kalabra,
		knaust,
		lacodicomo,
		lunchguide,
		mittgastronomi,
		norrlandskallaren,
		svartviksherrgard,
		skonsmon,
		dolcetto,
		max,
		wretmans,
		bilbiten,
		brandstation,
	]

def get_daily_specials():
	specials = []
	for scraper in get_scrapers():
		# The result can either be a list of dicts or a simple dict
		try:
			result = scraper.get_daily_specials()
			# Try to convert so json for sanity reasons, if it fails then skip
			# that scraper result.
			json.dumps(result)
		except Exception, e:
			traceback.print_exc(file=sys.stderr)
			print >> sys.stderr, "*"*80
		else:
			if isinstance(result, list):
				specials.extend(result)
			else:
				specials.append(result)

	# Remove all restaurants with no daily specials
	return filter(lambda x: len(x["specials"]), specials)

