import webbrowser


class Video():
    """Parent class if another child class i.e. Show will be implemented."""
    """Therefore common properties are not defined 2 times"""
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """This class provides a way to store movie related information."""

    def __init__(self, movie_title, duration, movie_storyline,
                 poster_image, trailer_youtube):
        Video.__init__(self, movie_title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens the URL of the trailer in a browser window."""
        webbrowser.open(self.trailer_youtube_url)
