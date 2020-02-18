# Given the tuple below that represents the Imelda May track,
# "More Mayhem", write code to print the album details, followed by a 
# listing of all the tracks in the album.

# Indent by a single tab stop when printing them (remember that you can
# pass more than one item to the print function, separating them with
# a comma).

# original data
# tuple refactored to include a nested list, to demonstrate that nested
# lists can can be changed, even within a tuple
imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"),
    (4, "Kentish Town Waltz")]
)

# lists nested in a tuple are mutable
imelda[3].append((5, "All For You"))

# tuple unpacking
title, artist, year, tracks = imelda

# nested lists can still have data appended, even after unpacking
tracks.append((6, "Eternity"))

print("Album: {}\nArtist: {}\nYear: {}\nTrack List:"
    .format(title, artist, year))

for song in tracks:
    # You can unpack nested tuples
    track, title = song
    print("\t{}. {}".format(track, title))