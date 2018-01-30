import webbrowser

class Movie:

    """ This Class provides a way to store movie related information """
    
    #VALIR_RATINGS: a class variable
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    # instance variables embaixo e parametros acima
    def __init__(self, trailer_youtube_url, title, storyline, poster_image_url):

        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline

    # instance method
    def open_trailer(self):

        webbrowser.open(self.trailer_youtube_url)

    def open_image(self):

        webbrowser.open(self.poster_image_url)
