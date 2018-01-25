import os 

current_dir = os.getcwd() 

lista = os.listdir(current_dir)

pure_file_names = []

print(current_dir)

for word in lista:
    
    print (word)

    if word[0].isdigit()==True and word[1].isdigit()==True:
        
        new_word = word[2:]
        
        print (word,new_word)

        os.renames(word, new_word)

    elif word=="secret-message.py":

        None

    else:
        
        new_word = word[1:]
        
        os.renames(word,new_word)



