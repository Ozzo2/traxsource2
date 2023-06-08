from bs4 import BeautifulSoup
import requests

PATH = r"C:\Users\Ozren\Desktop\Python\traxsource\songlist.txt"
LINK = "https://www.traxsource.com/genre/4/house/top"

response = requests.get(LINK)
trax_webpage = response.text

soup = BeautifulSoup(trax_webpage, "html.parser")
title = soup.find_all("div", class_="trk-row")

# input liked song numbers
likedSongs = list(map(int, input("Which songs do you like? (separate with space):").split()))

songs = []
artists = []
version = []

#create lists for songs, artists and versions
for res in title[1:]:
    songName = res.find(class_="title").a.get_text(strip=True)
    songs.append(songName)
    allArtists = []
    for tag in res.find_all(class_="com-artists"):
        allArtists.append(tag.text)
    joinedAllArtists = ", ".join(allArtists)
    artists.append(joinedAllArtists)
    ver = res.find(class_="version").get_text(strip=True)
    version.append(ver)

# print songs to console
for item in likedSongs:
    print(f"Artist: {artists[item-1]} \nSong: {songs[item-1]} \nVersion: {version[item-1]} \n")

# write/append to file (create file if one does not exist in specified directory)
with open(PATH, "a+", encoding="utf-8") as file:
    appendEOL = False
    file.seek(0)
    data = file.read(100)
    if len(data) > 0:
        appendEOL = True
    for item in likedSongs:
        if appendEOL:
            file.write("\n")
        else:
            appendEOL = True
        file.write(f"{artists[item-1]} - {songs[item-1]} ({version[item-1]})")