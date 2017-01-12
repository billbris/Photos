import photos

all_assets = photos.get_assets()

print ("Asset count: {}".format(len(all_assets)))

smart_albums = photos.get_smart_albums()

other_albums = photos.get_albums()

print ("Smart albums count: {}".format(len(smart_albums)))
for album in smart_albums:
	print("\tTitle: {}. Type:{} Count:{}".format(album.title, album.type, len(album.assets)))
print ("\nOther albums count: {}".format(len(other_albums)))
for album in other_albums:
	print("\tTitle: {}. Type:{} Count:{}".format(album.title, album.type, len(album.assets)))
a = 25

