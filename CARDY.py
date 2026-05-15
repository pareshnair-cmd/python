class flashcards:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'[ '+self.meaning+' ]'   
flash = []
print("welcome to flashcard time [:D]")
while (True):
    word = input("[add your special word on this side]")
    meaning = input("[add that meaning to your special word]")
    flash.append(flashcards(word,meaning))
    option = int(input("[Type 0 to add more and to discontinue type 1]"))
    if option == 1:
        break
    print ("\nYour flashcards")
    for i in range:
        print("<",i) 
