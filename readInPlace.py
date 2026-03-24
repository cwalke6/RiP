from tkinter import *

# TODO: Make the window a updated set size.

window = Tk()
window.geometry("1280x720")
window.title("(RiP) - Read in Place")

rawTextToRead = """The world is always full of the sound of waves. The little fishes, abandoning themselves to the waves, dance and sing, and play, but who knows the heart of the sea, a hundred feet down? Who knows its depth?"""
splitTextToRead = rawTextToRead.split()

middleLetterIndex = 0
wordIndex = 0

def updateText():
    global wordIndex

    if wordIndex < len(splitTextToRead):
        # Find the middle letter of the word
        middleLetterIndex = len(splitTextToRead[wordIndex]) // 2
        
        firstHalfWord = splitTextToRead[wordIndex][:middleLetterIndex]
        middleLetter = splitTextToRead[wordIndex][middleLetterIndex]
        secondHalfWord = splitTextToRead[wordIndex][middleLetterIndex+1:]


        firstHalfWordToRead.config(text=firstHalfWord.rjust(20))
        middleLetterToRead.config(text=middleLetter)
        secondHalfWordToRead.config(text=secondHalfWord.ljust(20))
        
        wordIndex += 1
        window.after(updateRate, updateText)

firstHalfWordToRead = Label(window, text="Loa".rjust(20), font=("Arial", 48), fg="black")
firstHalfWordToRead.pack(side=LEFT,expand=False, fill=X)

middleLetterToRead = Label(window, text="d", font=("Arial", 48), fg="red")
middleLetterToRead.pack(side=LEFT, expand=False)

secondHalfWordToRead = Label(window, text="ing".ljust(20), font=("Arial", 48), fg="black")
secondHalfWordToRead.pack(side=LEFT, expand=False, fill=X)


updateRate = 150 # milliseconds
wordsPerMinute = 60000 //updateRate # Meaning if we want to go from (WPM -> updateRate): updateRate = 60000 / WPM
wordsPerMinuteLabel = Label(window, text=f"{str(wordsPerMinute)} WPM", font=("Arial", 24))
wordsPerMinuteLabel.place(relx = 0.5, rely = 0.9)

window.after(updateRate, updateText)

window.mainloop()
