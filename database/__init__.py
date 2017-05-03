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

class Database:
	def _connect(self, connstr=_conn_string):
		# Creates a connection to the database using the given connection string
		return psycopg2.connect(connstr)

	def _write(self, sql, args=tuple()):
		# Executes a query which modifies the database
		connection = self._connect()
		try:
			with connection.cursor(cursor_factory=_cursor_class) as cursor:
				cursor.execute(sql, args)
			connection.commit()
		finally:
			connection.close()

	def _read(self, sql, args=tuple()):
		# Executes a query which doesn't modify the database but returns data
		connection = self._connect()
		result = None
		try:
			with connection.cursor(cursor_factory=_cursor_class) as cursor:
				cursor.execute(sql, args)
				result = cursor.fetchall()
		finally:
			connection.close()
		return result

	def build(self):
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
				   state      VARCHAR,
				   other      VARCHAR); -- Useful to store additional data about the user state
				 INSERT INTO users(id, username, admin)
				   SELECT 62805296, 'Carlovan', true
				   WHERE NOT EXISTS (SELECT * FROM users WHERE id != 62805296);
				 CREATE TABLE IF NOT EXISTS confronta_items (
				   itemid INTEGER REFERENCES items(id),
				   userid BIGINT  REFERENCES users(id),
				   PRIMARY KEY(itemid, userid));
			  '''
		self._write(sql)
