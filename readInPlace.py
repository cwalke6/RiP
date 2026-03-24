from tkinter import *

# TODO: Make the window a updated set size.

window = Tk()
window.geometry("1280x720")
window.title("(RiP) - Read in Place")

wordFrame = Frame(window)
wordFrame.pack(expand=True)

rawTextToRead = """He woke at half-past two, an hour which long experience had taught him brings panic intensity to all awkward thoughts. Experience had also taught him that a further waking at the proper hour of eight showed the folly of such panic.""" 
splitTextToRead = rawTextToRead.split()

middleLetterIndex = 0
wordIndex = 0

updateRate = 500 # milliseconds
wordsPerMinute = 60000 //updateRate # Meaning if we want to go from (WPM -> updateRate): updateRate = 60000 / WPM

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


firstHalfWordToRead = Label(wordFrame, text="Loa", font=("Arial", 48), fg="black")
firstHalfWordToRead.pack(side=LEFT)

middleLetterToRead = Label(wordFrame, text="d", font=("Arial", 48), fg="red")
middleLetterToRead.pack(side=LEFT, expand=False)

secondHalfWordToRead = Label(wordFrame, text="ing", font=("Arial", 48), fg="black")
secondHalfWordToRead.pack(side=LEFT, expand=False)


wordsPerMinuteLabel = Label(window, text=f"{str(wordsPerMinute)} WPM", font=("Arial", 24))
wordsPerMinuteLabel.place(relx = 0.5, rely = 0.9)

window.after(updateRate, updateText)

window.mainloop()
