# -*- coding: utf-8 -*-
# Useful function to handle the database

try:
	import psycopg2, psycopg2.extras as psycopg2extras
except ImportError:
	import psycopg2cffi as psycopg2, psycopg2cffi.extras as psycopg2extras
import urllib.parse as urlparse
import settings
import logging

logger = logging.getLogger(__name__)

_cursor_class = psycopg2extras.DictCursor

# Parse the database url to extract the informations
urlparse.uses_netloc.append('postgres')
_parsed = urlparse.urlparse(settings.database_url)
_conn_string = "host='{}' port='{}' user='{}' password='{}' dbname='{}'".format(_parsed.hostname, _parsed.port, _parsed.username, _parsed.password, _parsed.path[1:])

class Database:
	def __init__(self):
		self.connection = self._connect()
		self.initialized = True
		self.initialized = self._read('SELECT SUM(1) FROM information_schema.tables WHERE table_schema=\'public\' AND table_name IN (\'items\', \'users\');')[0][0] == 2

	def __del__(self):
		self.connection.close()

	def _connect(self, connstr=_conn_string):
		# Creates a connection to the database using the given connection string
		return psycopg2.connect(connstr)

	def _write(self, sql, args=tuple()):
		# Executes a query which modifies the database
		if not self.initialized: return []
		try:
			with self.connection.cursor(cursor_factory=_cursor_class) as cursor:
				cursor.execute(sql, args)
			self.connection.commit()
		except Exception as ex:
			logger.error(str(ex))
			raise ex

	def _read(self, sql, args=tuple()):
		# Executes a query which doesn't modify the database but returns data
		if not self.initialized: return []
		result = None
		try:
			with self.connection.cursor(cursor_factory=_cursor_class) as cursor:
				cursor.execute(sql, args)
				result = cursor.fetchall()
		except Exception as ex:
			logger.error(str(ex))
			raise ex
		return result

	def build(self):
		# Creates all the tables (does not drop anything)
		self.initialized = True
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
				   changelog  BOOLEAN NOT NULL DEFAULT false, -- true if the user already received the last changelog
				   other      VARCHAR); -- Useful to store additional data about the user state
				 INSERT INTO users(id, username, admin)
				   SELECT {admin_id}, '', true
				   WHERE NOT EXISTS (SELECT * FROM users WHERE id = {admin_id});
				 CREATE TABLE IF NOT EXISTS user_items (
				   itemid   INTEGER REFERENCES items(id) ON DELETE CASCADE,
				   userid   BIGINT  REFERENCES users(id),
				   quantity INTEGER NOT NULL DEFAULT 0,
				   state VARCHAR,
				   PRIMARY KEY(itemid, userid, state));
			  '''.format(admin_id=settings.admin)
		self._write(sql)
