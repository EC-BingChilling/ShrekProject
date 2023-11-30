import pygame
import tkinter as tk
from tkinter import ttk
from pydub import AudioSegment

class PianoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Piano App")

        self.initialize_piano()
        self.initialize_sound()

    def initialize_piano(self):
        piano_frame = ttk.Frame(self.root)
        piano_frame.grid(row=0, column=0, padx=10, pady=10)

        notes = ["C", "D", "E", "F", "G"]

        for i, note in enumerate(notes):
            button = ttk.Button(piano_frame, text=note, command=lambda n=note: self.play_sound(n))
            button.grid(row=0, column=i, padx=5, pady=5)

    def initialize_sound(self):
        pygame.mixer.init()

    def play_sound(self, note):
        base_sound = AudioSegment.from_file("noo.mp3", format="mp3")
        pitch_shift = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7}
        shifted_sound = base_sound._spawn(base_sound.raw_data, overrides={
            "frame_rate": int(base_sound.frame_rate * (2 ** (pitch_shift[note] / 12.0)))
        })

        shifted_sound.export("temp.wav", format="wav")
        pygame.mixer.music.load("temp.wav")
        pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    app = PianoApp(root)
    root.mainloop()
