import random

#Set number of cycles to complete
interations = 2000

#Set up lists of words
noun = ["Dinosaur", "Ball", "House"]
adverb = ["rapidly", "slowly", "casually"]
adjective = ["smooth", "rough", "gentle"]

#Start writing 
while interations > 0:
    #picks a random number which corrisponds to a word from the list. Use of len function ensure all terms are accessable
    rand1 = random.randrange(0,len(noun),1)
    rand2 = random.randrange(0,len(adverb),1)
    rand3 = random.randrange(0,len(adjective),1)
    print(f"The {noun[rand1]} was {adjective[rand2]} when it {adverb[rand3]} went to school!")
    interations -= 1


