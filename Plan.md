# Read in Place - Development Plan

## Code Quality Improvements
1. **Eliminate global variables** - Convert to a class-based structure encapsulating `wordIndex`, `updateRate`, etc.
2. **Add type hints** - Improve code maintainability
3. **Separate concerns** - Distinguish UI code from business logic

## Features to Add
1. **User input** - Allow custom text input or file loading
2. **Playback controls** - Play/Pause/Stop buttons
3. **Speed adjustment** - Slider or buttons to change WPM dynamically
4. **Keyboard shortcuts** - Space for pause, arrows for navigation
5. **Progress indicator** - Show current position in text

## Bugs to Fix
1. **WPM label position** - Use fixed width or anchor to prevent movement
2. **Single-letter words** - Handle edge case where `middleLetterIndex+1` exceeds string bounds

## Future Enhancements
- CLI argument parsing for file input
- Settings persistence
- Theme support
