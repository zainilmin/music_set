"""
Read data set from two different files
unique_artists.txt
shs_dataset_train.txt

"""


def insert_shs_data(conn, file_name):
    """
    Insert shs data set in two tables:
    clique and clique_group
    :param conn:
    :param file_name:
    :return:
    """
    c = conn.cursor()
    row_id = ''
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            if '#' not in line:
                if '%' in line:
                    line = line.replace('%', '').strip()
                    # Some rows contain more than 3 work numbers
                    # Assuming that we will only extract 3 work (a, b, c)
                    work_list = [-1, -1, -1]
                    for i, item in enumerate(line.split(',')):
                        if item.lstrip('-').isdigit() and i < 3:
                            work_list[i] = item
                        if not item.lstrip('-').isdigit():
                            work_list.append(item.strip())
                    # insert into clique table
                    c.execute(
                        'INSERT INTO clique(a_work, b_work, c_work, title)'
                        ' VALUES(?, ?, ?, ?);',
                        tuple(work_list)
                    )
                    row_id = c.lastrowid
                    conn.commit()
                else:
                    line = line.strip()
                    group_list = [x.strip() for x in line.split('<SEP>')]
                    group_list.append(row_id)
                    # insert into clique_group table
                    c.execute(
                        'INSERT INTO clique_group'
                        '(track_id, artist_id, perf, clique_id)'
                        ' VALUES(?, ?, ?, ?);',
                        tuple(group_list)
                    )
                    conn.commit()


def insert_artist(conn, file_name):
    """
    Insert artist data into artist table
    :param conn:
    :param file_name:
    :return:
    """
    artist_list = []
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            artist_list.append([x.strip() for x in line.split('<SEP>')])
    c = conn.cursor()
    c.executemany(
        'INSERT INTO artist '
        'VALUES(?, ?, ?, ?);',
        [tuple(item) for item in artist_list]
    )
    conn.commit()
