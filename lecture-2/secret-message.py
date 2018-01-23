import os

lista = os.listdir("prank")

pure_file_names = []

for word in lista:
    
    print (word)

    if word[0].isdigit()==True and word[1].isdigit()==True:
        
        pure_file_names.append(word[2:])

    else:

        pure_file_names.append(word[1:])

print (pure_file_names)
