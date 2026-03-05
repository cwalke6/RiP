from tkinter import *

# TODO LIST
# TODO: Create a pause button
# TODO: fix WPM text at the bottom moving around

window = Tk()
window.geometry("700x500")
window.title("Read in Place")

rawTextToRead = """Generating random paragraphs can be an excellent way for writers to get their creative flow going at the beginning of the day. The writer has no idea what topic the random paragraph will be about when it appears. This forces the writer to use creativity to complete one of three common writing challenges. The writer can use the paragraph as the first one of a short story and build upon it. A second option is to use the random paragraph somewhere in a short story they create. The third option is to have the random paragraph be the ending paragraph in a short story. No matter which of these challenges is undertaken, the writer is forced to use creativity to incorporate the paragraph into their writing."""
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
wordsPerMinuteLabel = Label(window, text=f"{str(wordsPerMinute)} WPM", font=("Arial", 12))
wordsPerMinuteLabel.pack(side=BOTTOM)

window.after(updateRate, updateText)

window.mainloop()
