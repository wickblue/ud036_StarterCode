import webbrowser


# define the class for the movie-related objects
class Movie():
    """ This class provides a way to store movie related information """

    # initializes Movie object with title, storyline, image and trailer       
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # opens up trailer in web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)




