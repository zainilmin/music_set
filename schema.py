"""
Schema file contains create_connection & create_table functions

"""
import sqlite3
from sqlite3 import Error

clique_table = """ CREATE TABLE IF NOT EXISTS clique (
                       id integer primary key autoincrement,
                       a_work integer,
                       b_work integer,
                       c_work integer,
                       title varchar(100) 
               );"""
clique_group_table = """ CREATE TABLE IF NOT EXISTS clique_group (
                             id integer primary key autoincrement,
                             track_id varchar(50), 
                             artist_id varchar(50),
                             perf integer,
                             clique_id integer,
                             FOREIGN KEY (clique_id) REFERENCES clique (id) 
                     );"""
artist_table = """ CREATE TABLE IF NOT EXISTS artist (
                       artist_id varchar(50) primary key,
                       artist_mbid varchar(50),
                       track_id varchar(50),
                       artist_name varchar(100) 
               );"""

table_list = [clique_table, clique_group_table, artist_table]


def create_connection(db_file):
    """
    Create Connection
    :param db_file:
    :return: conn
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn):
    """
    Create Table
    :param conn:
    :return:
    """
    for table in table_list:
        try:
            c = conn.cursor()
            c.execute(table)
        except Error as e:
            print(e)


def query_song_by_artist(conn, artist_name):
    """
    Query songs by artist
    Joining artist and clique group table to get clique_id and using ids to
    query clique table to get song title
    :param conn:
    :param artist_name:
    :return: query result
    """
    query_result = []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT clique.title FROM clique WHERE clique.id IN ("
                       "SELECT clique_group.clique_id "
                       "FROM artist join clique_group "
                       "on artist.artist_id = clique_group.artist_id"
                       " WHERE artist.artist_name = '" + artist_name + "');")
        query_result = cursor.fetchall()
    except Error as e:
        print(e)
    return query_result
