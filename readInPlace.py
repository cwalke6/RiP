from tkinter import *

window = Tk()
window.geometry("1280x720")
window.title("(RiP) - Read in Place")

rawTextToRead = """This world . . . belongs to the strong, my friend! The ritual of our existence is based on the strong getting stronger by devouring the weak. We must face up to this. No more than right that it should be this way. We must learn to accept it as a law of the natural world. The rabbits accept their role in the ritual and recognize the wolf is the strong. In defense, the rabbit becomes sly and frightened and elusive and he digs holes and hides when the wolf is about. And he endures, he goes on. He knows his place. He most certainly doesn't challenge the wolf to combat. Now, would that be wise? Would it?"""
splitTextToRead = rawTextToRead.split()
wordIndex = 0
updateRate = 500
wordsPerMinute = 60000 // updateRate

# Fixed center point of the window
CENTER_X = 640
CENTER_Y = 360

middleLetterToRead = Label(window, text="d", font=("Arial", 48), fg="red")
middleLetterToRead.place(x=CENTER_X, y=CENTER_Y, anchor="center")  # PINNED - never moves

firstHalfWordToRead = Label(window, text="Loa", font=("Arial", 48), fg="black")
secondHalfWordToRead = Label(window, text="ing", font=("Arial", 48), fg="black")

def updateText():
    global wordIndex
    if wordIndex < len(splitTextToRead):
        word = splitTextToRead[wordIndex]
        middleLetterIndex = len(word) // 2

        firstHalf = word[:middleLetterIndex]
        middleLetter = word[middleLetterIndex]
        secondHalf = word[middleLetterIndex + 1:]

        # Update text
        firstHalfWordToRead.config(text=firstHalf)
        middleLetterToRead.config(text=middleLetter)
        secondHalfWordToRead.config(text=secondHalf)

        # Force tkinter to calculate new label sizes BEFORE repositioning
        window.update_idletasks()

        # Get the middle letter's exact pixel position on screen
        mid_x = middleLetterToRead.winfo_x()
        mid_width = middleLetterToRead.winfo_width()
        mid_y = middleLetterToRead.winfo_y()
        mid_height = middleLetterToRead.winfo_height()

        # Place first half so its RIGHT edge touches the middle letter's LEFT edge
        first_width = firstHalfWordToRead.winfo_width()
        firstHalfWordToRead.place(x=mid_x, y=mid_y + mid_height // 2, anchor="e")

        # Place second half so its LEFT edge touches the middle letter's RIGHT edge
        secondHalfWordToRead.place(x=mid_x + mid_width, y=mid_y + mid_height // 2, anchor="w")

        wordIndex += 1
        window.after(updateRate, updateText)

wordsPerMinuteLabel = Label(window, text=f"{str(wordsPerMinute)} WPM", font=("Arial", 24))
wordsPerMinuteLabel.place(relx=0.45, rely=0.9)

window.after(updateRate, updateText)
window.mainloop()