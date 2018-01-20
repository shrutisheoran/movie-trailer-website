import webbrowser


class Movie():
    """This class shows specified movie poster and trailer."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # This constructor assign values to class variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This function will show the poster image passed by the object
    def showposter(self):
        webbrowser.open(self.poster_image_url)

    # This function will show the youtube trailer passed by the object
    def showtrailer(self):
        webbrowser.open(self.trailer_youtube_url)
