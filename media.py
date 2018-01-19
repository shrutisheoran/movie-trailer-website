import webbrowser


class Movie():
    """This class provides movie related information."""
    VALID_RATINGS = ["G", "VG", "P", "VP"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_yout
                 ube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def showposter(self):
        webbrowser.open(self.poster_image_url)

    def showtrailer(self):
        webbrowser.open(self.trailer_youtube_url)
