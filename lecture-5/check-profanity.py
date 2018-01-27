import urllib

def read_text():

    quotes = open("/home/pedro/udacity-py/lecture-5/movie_quotes.txt")
    
    words = [] 

    for line in quotes:
            
        words_line = line.split()
    
        words = words + words_line
    
    #print (words)

    for word in words:
        
        #print (word) 

        connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+str(word))

        outcome = connection.read()
        
        #print (outcome)

        if outcome=="true":
           
           return "Profatiny detected cursed word: "+word
        
        # importante fechar a connection, se n fica rodando, tipo num loop sem fim
        connection.close()


    else:
        
        return "Text is clean"

print (read_text())

