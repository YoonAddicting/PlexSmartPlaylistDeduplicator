# Plex Smart Playlist Deduplicator
This is a python script to remove any duplicate songs in a smart playlist using the workaround with setting the mood on duplicate songs, and then excluding those songs from the smart playlist.

## Requirements
- [Python 3](https://www.python.org/) (Tested with 3.9)
- [plexapi](https://github.com/pkkid/python-plexapi) (Tested with 4.2.0)

## How it works
The script works by getting the name of the playlist you wish to remove duplicate songs from, and thereafter appending the mood "Duplicate" to any of the songs found as duplicates.  
Inside Plex you will have to modify your smart playlist with the filter: `Track mood is not Duplicate`.

## How to run
Simply execute the python file `main.py` and follow the instructions to enter your credentials and server name as well as playlist name, and watch the magic.
To see a list of found songs as unique and duplicate add the flag `--debug` when executing the script.
