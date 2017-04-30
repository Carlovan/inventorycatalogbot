# -*- coding: utf-8 -*-
# Useful function to handle the database

import psycopg2, psycopg2.extras
import urllib.parse as urlparse
import settings

_cursor_class = psycopg2.extras.DictCursor

# Parse the database url to extract the informations
urlparse.uses_netloc.append('postgres')
_parsed = urlparse.urlparse(settings.database_url)
_conn_string = "host='{}' port='{}' user='{}' password='{}' dbname='{}'".format(_parsed.hostname, _parsed.port, _parsed.username, _parsed.password, _parsed.path[1:])

def _connect(connstr=_conn_string):
	# Creates a connection to the database using the given connection string
	return psycopg2.connect(connstr)

def _write(sql, args=tuple()):
	# Executes a query which modifies the database
	connection = _connect()
	try:
		with connection.cursor(cursor_factory=_cursor_class) as cursor:
			cursor.execute(sql, args)
		connection.commit()
	finally:
		connection.close()

def _read(sql, args=tuple()):
	# Executes a query which doesn't modify the database but returns data
	connection = _connect()
	result = None
	try:
		with connection.cursor(cursor_factory=_cursor_class) as cursor:
			cursor.execute(sql, args)
			result = cursor.fetchall()
	finally:
		connection.close()
	return result

def build():
	# Creates all the tables (does not drop anything)
	sql = '''CREATE TABLE IF NOT EXISTS items (
	           id     SERIAL     PRIMARY KEY,
	           name   VARCHAR    NOT NULL UNIQUE,
	           rarity VARCHAR(5) NOT NULL,
	           usable BOOLEAN    NOT NULL);
	         CREATE TABLE IF NOT EXISTS users (
	           id         BIGINT  PRIMARY KEY,
	           username   VARCHAR NOT NULL DEFAULT '',
	           admin      BOOLEAN NOT NULL DEFAULT false,
	           state      VARCHAR);
	         INSERT INTO users(id, username, admin) VALUES (62805296, 'Carlovan', true) ON CONFLICT DO NOTHING;
	      '''
	_write(sql)


