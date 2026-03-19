"""
Read in Place - A speed reading application.
Designed to help improve reading speed by keeping the readers focus on a set center point. 
"""

import tkinter as tk
from tkinter import font as tkfont


class ReadInPlaceApp:
    """Main application class for the Read in Place speed reading tool."""
    
    def __init__(self, root):
        """Initialize the application with the given root window."""
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("(RiP) - Read in Place")
        # Prevent window resizing to maintain consistent layout
        self.root.resizable(False, False)
        
        # Application state
        self.word_index = 0
        self.update_rate = 150  # milliseconds between word updates
        self.words_per_minute = 60000 // self.update_rate
        
        # Sample text to display (could be loaded from file or user input)
        self.raw_text = """Generating random paragraphs can be an excellent way for writers to get their creative flow going at the beginning of the day. The writer has no idea what topic the random paragraph will be about when it appears. This forces the writer to use creativity to complete one of three common writing challenges. The writer can use the paragraph as the first one of a short story and build upon it. A second option is to use the random paragraph somewhere in a short story they create. The third option is to have the random paragraph be the ending paragraph in a short story. No matter which of these challenges is undertaken, the writer is forced to use creativity to incorporate the paragraph into their writing."""
        self.split_text = self.raw_text.split()
        
        # Create UI components
        self._create_widgets()
        self._setup_layout()
        
        # Start the word display updates
        self.root.after(self.update_rate, self.update_text)
    
    def _create_widgets(self):
        """Create all UI widgets for the application."""
        # Font configuration - using monospace for consistent character width
        self.word_font = tkfont.Font(family="Courier", size=48)
        self.wpm_font = tkfont.Font(family="Arial", size=24)
        
        # Text display labels with fixed width to prevent layout shifts
        # Using monospace font ensures each character occupies same width
        self.first_half_label = tk.Label(
            self.root, 
            text="Loa", 
            font=("Arial", 48),
            fg="black",
            width=20,  # Fixed width in characters (prevents label width changes)
            anchor="e"  # Align text to right (east) within the fixed-width label
        )
        
        self.middle_letter_label = tk.Label(
            self.root, 
            text="d", 
            font=self.word_font, 
            fg="red",
            width=1,  # Fixed width for single character
            anchor="center"  # Center align
        )
        
        self.second_half_label = tk.Label(
            self.root, 
            text="ing", 
            font=self.word_font, 
            fg="black",
            width=20,  # Fixed width in characters (prevents label width changes)
            anchor="w"  # Align text to left (west) within the fixed-width label
        )
        
        # WPM display - placed in a fixed position at bottom
        # Using a fixed-height container to prevent vertical movement
        self.wpm_label = tk.Label(
            self.root,
            text=f"{self.words_per_minute} WPM",
            font=self.wpm_font
        )
    
    def _setup_layout(self):
        """Arrange widgets in the window using pack geometry manager."""
        # Create a fixed-size frame for the word display to prevent any size changes
        word_display_frame = tk.Frame(
            self.root,
            height=100  # Fixed height to prevent vertical shifts
        )
        word_display_frame.pack(expand=True, pady=50)
        word_display_frame.pack_propagate(False)  # Prevent frame from shrinking to fit contents
        
        # Pack the labels into the fixed frame
        self.first_half_label.pack(in_=word_display_frame, side=tk.LEFT)
        self.middle_letter_label.pack(in_=word_display_frame, side=tk.LEFT)
        self.second_half_label.pack(in_=word_display_frame, side=tk.LEFT)
        
        # Pack WPM label at bottom with fixed position
        # Using side=BOTTOM with no expand/fill keeps it in a fixed position
        self.wpm_label.pack(side=tk.BOTTOM, pady=20)
    
    def update_text(self):
        """Update the displayed text to show the next word with middle letter highlighted."""
        print("---update_text---")
        if self.word_index < len(self.split_text):
            word = self.split_text[self.word_index]
            print(f"---Updated word: {word}")

            # Calculate the middle letter position
            middle_index = len(word) // 2
            
            # Split word into parts for display
            first_half = word[:middle_index]
            middle_letter = word[middle_index]
            second_half = word[middle_index + 1:]
            
            # Update label texts - fixed width labels + monospace font prevent layout shifts
            self.first_half_label.config(text=first_half.rjust(20))
            self.middle_letter_label.config(text=middle_letter)
            self.second_half_label.config(text=second_half.ljust(20))
            
            # Move to next word and schedule next update
            self.word_index += 1
            self.root.after(self.update_rate, self.update_text)


def main():
    """Entry point for the application."""
    root = tk.Tk()
    app = ReadInPlaceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
