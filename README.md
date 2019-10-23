# shs_project

Process music data set and query using artist name

## Getting Started

Usage:
```
usage: main.py [-h] [-a ARTIST [ARTIST ...]] [-c]

Process music data set and query

optional arguments:
  -h, --help            show this help message and exit
  -a ARTIST [ARTIST ...]
                        Provide Artist name
  -c, --create_db       Create new Sqlite database

Example:
        -> First command to run if db not present
        python main.py -a Antonio Carlos Jobim --create_db
        -> Query the db
        python main.py -a Antonio Carlos Jobim
        python main.py -a The Bristols
```

Example:
```
python main.py -a Antonio Carlos Jobim --create_db
python main.py -a Antonio Carlos Jobim

```

Output:
```
The following are the songs for Antonio Carlos Jobim in the database:
Água De Beber
The Girl From Ipanema
Berimbau
Dindi
Desafinado
Waters Of March (LP Version)
Wave
```
