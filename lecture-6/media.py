import webbrowser

class Movie:

    def __init__(self, youtube, name, storyline, poster):

        self.name = name
        self.poster = poster
        self.youtube = youtube
        self.storyline = storyline


    def open_trailer(self):

        webbrowser.open(self.youtube)

    def open_image(self):

        webbrowser.open(self.poster)
