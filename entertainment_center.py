import fresh_tomatoes
# Import of our own classes which hold data about specific movies.
import media

# Creating six instances of the Movie class for six different movies.
toy_story = media.Movie("Toy Story", "Useless movie", 180,
                        "https://goo.gl/v2A26K",
                        "https://www.youtube.com/watch?v=azyK_k52R1w")

avatar = media.Movie("Avatar", "A marine on an alien planet", 125,
                     "https://goo.gl/5gCvn6",
                     "https://www.youtube.com/watch?v=8TNlvM4cN6U")

star_trek = media.Movie("Star Trek", "A lot of space vessels and phaser.", 160,
                        "https://goo.gl/o5JTL6",
                        "https://www.youtube.com/watch?v=6VEnT11mTnI")

fluch_der_karibik = media.Movie("Fluch der Karibik", "Pirates on a ship", 200,
                                "https://goo.gl/g1mNHE",
                                "https://www.youtube.com/watch?v=MefeqhnjNvI")

battlestar = media.Movie("Battlestar Galactica - Blood and Chrome",
                         "Battlestar movie", 115,
                         "https://goo.gl/anRQwU",
                         "https://www.youtube.com/watch?v=Qj50xJhWdcM")

star_wars = media.Movie("Star Wars - Rough One", "Star Wars SuicideSquad", 120,
                        "https://goo.gl/UNCKuT",
                        "https://www.youtube.com/watch?v=sC9abcLLQpI")

# Storing the movies in an array to hand it over to 'fresh_tomatoes'
movies = [toy_story,
          avatar,
          star_trek,
          fluch_der_karibik,
          battlestar,
          star_wars]

# Create a HTML page to show our movies
fresh_tomatoes.open_movies_page(movies)
