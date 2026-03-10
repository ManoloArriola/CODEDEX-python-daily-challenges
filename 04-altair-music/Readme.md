Homebrew Computer Club 🤓
March 5, 2026
·
12
4

On this day, March 5th, 1975, the legendary Homebrew Computer Club held its very first meeting in a humble garage in Menlo Park, California. A casual gathering of computer hobbysts, they circled around a Altair 8800 and asked questions like "Can regular people really own computers?" Dreaming of what could be.

Most attendees didn't even own a computer yet; they were simply excited by the idea of it.

Among them was Steve Wozniak (aka Woz), who would later be inspired by the club to design the Apple I, kickstarting the personal computer revolution.

image

Here's a little-known fact: There was a music demo at that first meeting – "Dompier Music".

Steve Dompier, a Navy veteran and pilot, used the Altair 8800 to play The Beatles' "Fool on the Hill". He placed a portable weather radio near the computer, creating radio interference at certain frequencies that generated musical notes.

Everyone was transfixed, including Woz. This lil' demo became the spark that ignited the club.

In today's Daily Challenge, your task is to recreate that demo! 📻🎶🎵

The Altair had no keyboard or screen. Programs were entered using toggle switches. To enter a value into memory, you flipped switches up (1) or down (0). For example, 0100000101 is a binary number representing 261, the frequency of a C note.

Given a list/array of text strings representing the front-panel switches on the Altair, convert them from binary numbers to decimal numbers, and return the corresponding music notes.

So "0100000101" to 261 to "C4".

Frequency (Hz)	Note
261	"C4"
294	"D4"
329	"E4"
349	"F4"
392	"G4"
440	"A4"
494	"B4"
523	"C5"
0	"REST"
