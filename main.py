
import time
phrase = "Tu dois recopier ça"
start = time.time()
find = False
while find == False:
    response = input(phrase + "\n")
    if response == phrase:
        end = time.time()
        print(end - start)
        find = True
    else:
        print("erreur\n")
