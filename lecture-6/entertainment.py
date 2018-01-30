import media

# it is a good practice to define a class in one file and use it in another file

# preciso identificar que a classe Movie vem do arquivo media, por isso, media.Movie

# criar instancia toy_story
toy_story = media.Movie("https://www.youtube.com/watch?v=4KPTXpQehio",
                        "Toy Story", 
                        "A boy's toys come to life", 
                        "https://images-na.ssl-images-amazon.com/images/I/51P%2Btt2xIuL._SL500_AC_SS350_.jpg")

# criar instancia avatar, depois desse comentario, self=avatar!
# mais interessante do que isso, name, youtube, poster, storyline, sao todas INSTANCE VARIABLES
avatar = media.Movie("https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "Avatar",
                     "A marine in an allien planet",
                     "https://cdn.traileraddict.com/content/20th-century-fox/avatar-6.jpg")

print (avatar.storyline)
print (toy_story.name)

toy_story.open_trailer()

toy_story.open_image()

print (avatar.name)

avatar.open_trailer()

avatar.open_image()

