# Date: 8 March 2019
# Name(s): Christian Lussier, Jordan Wilson, Robert Samuel

# For use with the "python manage.py shell" utility.

# A sample code for pasting into the Django shell.
# Check your notes and slides to learn to use the shell utility.
from film.models import Album
a = Album(mainActor = "Paul Newman", filmTitle = "Slapshot", director = "George Roy Hill", genre = "Sport", album_logo = "http://puckjunk.com/wp-content/uploads/2017/02/Slap_shot.jpg")
b = Album(mainActor = "Tom Hanks", filmTitle = "Forest Gump", director = "Robert Zemeckis", genre = "Drama", album_logo = "https://data.logograph.com/resize/LyricTheatre/multimedia/Image/13421/SOFM%202018%20900x600%20Forrest%20Gump.jpg?width=1500")
c = Album(mainActor = "Leonardo DiCaprio", filmTitle = "Wolf of The Wall Street", director = "Martin Scorsese", genre = "Drama", album_logo = "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg")
d = Album(mainActor = "Samuel L. Jackson", filmTitle = "The Hateful Eight", director = "Quentin Tarantino", genre = "Drama", album_logo = "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/The_Hateful_Eight.jpg/220px-The_Hateful_Eight.jpg")
e = Album(mainActor = "Leonardo DiCaprio", filmTitle = "The Revenant", director = "Alejandro G. Iñárritu", genre = "Action", album_logo = "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg")

# Now save the object and Django will populate the Database!
a.save()
b.save()
c.save()
d.save()
e.save()

# show the ID (primary key)
a.id
b.id
c.id
d.id
e.id
