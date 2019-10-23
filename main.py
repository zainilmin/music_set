import os
import argparse
from dataset import insert_shs_data, insert_artist
from schema import create_connection, create_table, query_song_by_artist

# data set files and database name
shs_file_name = 'shs_dataset_train.txt'
artist_file_name = 'unique_artists.txt'
database_path = '.\db\sqlite.db'


def main():
    example_text = """Example:
        python main.py -a Antonio Carlos Jobim --create_db                
        python main.py -a Antonio Carlos Jobim
        python main.py -a The Bristols"""
    parser = argparse.ArgumentParser(
        description='Process music data set and query',
        epilog=example_text,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-a",
        dest="artist",
        help="Provide Artist name",
        nargs='+'
    )
    parser.add_argument(
        "-c",
        "--create_db",
        action='store_true',
        default=False,
        help='Create new Sqlite database'
    )
    args = parser.parse_args()

    if args.create_db:
        if os.path.exists(database_path):
            os.remove(database_path)
        conn = create_connection(database_path)
        create_table(conn)
        insert_artist(conn, artist_file_name)
        insert_shs_data(conn, shs_file_name)
    else:
        conn = create_connection(database_path)

    artist_name = ' '.join(args.artist)
    artist_songs = query_song_by_artist(conn, artist_name)
    if artist_songs:
        print("The following are the songs for {} in the database:".format(
              artist_name))
        for song in artist_songs:
            print(song[0])
    else:
        print("There are no songs for {} in database".format(artist_name))
    conn.close()


if __name__ == '__main__':
    main()
