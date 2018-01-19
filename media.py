import webbrowser


class Movie():
    # This class provides movie related information.
    VALID_RATINGS = ["G", "VG", "P", "VP"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This function shows poster on webpage
    def showposter(self):
        webbrowser.open(self.poster_image_url)

    # This function show trailer on youtube
    def showtrailer(self):
        webbrowser.open(self.trailer_youtube_url)
