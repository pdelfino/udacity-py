import webbrowser

class Movie:

    def __init__(self, trailer_youtube_url, title, storyline, poster_image_url):

        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline


    def open_trailer(self):

        webbrowser.open(self.trailer_youtube_url)

    def open_image(self):

        webbrowser.open(self.poster_image_url)
