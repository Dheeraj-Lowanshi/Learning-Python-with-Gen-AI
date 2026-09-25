
album="Aashiqui 2",2013,"Arjit Singh",((1,"Tum hi ho"),(2,"Chahun Main Ya Na"),(3,"Meri Aashiqui"),(4,"Aasan Nahin Yahaan"))

movie_name,yer,singer,songs=album

print("Title:",movie_name)
print("Year:",yer)
print("Singer:",singer)
for song in songs:
    song_no,song_name=song
    print("Song Number:",song_no,"Song Name:",song_name)