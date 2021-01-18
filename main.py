from plexapi.myplex import MyPlexAccount
import plexapi
import getpass
import sys
import logging

# Setup output of debug statements
log = logging.getLogger("PlexSmartPlaylistDeduplicator")
handler = logging.StreamHandler(sys.stderr)
if len(sys.argv) >= 2 and sys.argv[1] == "--debug":
    log.setLevel(logging.DEBUG)
    handler.setLevel(logging.DEBUG)
log.addHandler(handler)

# Authenticate with Plex
username = input("Enter your username for Plex: ")
pw = getpass.getpass()
account = MyPlexAccount(username, pw)
server = input("Enter the server identifier: ") # Also called the "Friendly name" in Plex settings.
plex = account.resource(server).connect()  # returns a PlexServer instance

# Get the playlist to remove duplicates from
playlistName = input("Enter the name of the playlist to remove duplicates from: ")
playlist = plex.playlist(playlistName)

uniqueTracks = [] # List with unique tracks
duplicateTracks = [] #List with duplicates

# Check all items in playlist if they have been met before in the search, if yes then add to duplicate, otherwise add to unique.
for track in playlist.items():
    if(any(t.guid == track.guid for t in uniqueTracks)):
        duplicateTracks.append(track)
    else:
        uniqueTracks.append(track)

log.debug("Unique tracks:")
for track in uniqueTracks:
    log.debug(f'{track.title} - {track.parentTitle} - {track.grandparentTitle} - {track.guid}')

log.debug("Duplicate tracks:")
for track in duplicateTracks:
    log.debug(f'{track.title} - {track.parentTitle} - {track.grandparentTitle} - {track.guid}')


print("Applying mood to duplicates...")
for track in duplicateTracks:
    print(f'{track.title} - {track.parentTitle} - {track.grandparentTitle} - {track.guid}')
    data = {}
    count = 0
    data["mood.locked"] = 1
    for mood in track.moods:
            data["mood[" + str(count) + "].tag.tag"] = mood.tag
            count += 1
    data["mood[" + str(count) + "].tag.tag"] = "Duplicate"
    track.edit(**data)
    track.reload()
