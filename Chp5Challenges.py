#Chapter 5 Challenges from STP

#List of favorite musicians

fav_musicians = ["Porter Robinson", "Above & Beyond", "Bro Safari"]

#List of Tuples, with each containing the longitude and latitude of somwhere
#you've lived or visited

madison = (43.0730517, -89.4012302)
boston = (42.361145, -71.057083)
coventry = (52.405838, -1.512661)

my_cities = []
my_cities.append(madison)
my_cities.append(boston)
my_cities.append(coventry)

#print(my_cities)

#dictionary that contains diff. attributes about me: height, fav color,
#fav author, etc.

my_attributes = {"height":"5 ft. 9 in.", "fav color":"gold",
                "fav author":"Brian Sanderson", "fav activity":"climbing"}

#Program that lets the user ask your height, favorite color, or favorite author
# and returns the result from the dictionary you created in the previous challenge

i = input("Would you like to know: height, fav color, fav author, or fav activity?\n")
if i in my_attributes:
    print(my_attributes[i])
else:
    print("Sorry I didn't understand that.")

# Creat a dict. mapping favorite musicians to a list of your favorite songs by them

porter_robinson_songs = ["Shelter", "Sad Machine", "Divinity"]
above_and_beyond_songs = ["Northern Soul", "On a Good Day", "My Own Hymn"]
bro_safari_songs = ["The Drop", "XL", "Follow - Zomboy Remix"]

song_dict = {}
song_dict["Porter Robinson"] = porter_robinson_songs
song_dict["Above & Beyond"] = above_and_beyond_songs
song_dict["Bro Safari"] = bro_safari_songs
#print(song_dict["Bro Safari"])
