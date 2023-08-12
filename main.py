import time
import tkinter as tk
from tkinter import messagebox
import random


class SpeedTypingTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "She sells seashells by the seashore.",
            "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
            "Peter Piper picked a peck of pickled peppers.",
            "Sally sells sea shells by the sea shore.",
        ]
        self.current_sentence = ""
        self.correct_words = 0
        self.start_time = 0

        self.label = tk.Label(root, text="Welcome to the Speed Typing Test!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_test, font=("Helvetica", 12))
        self.start_button.pack()

        self.text_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.text_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 12))
        self.entry.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

    def start_test(self):
        self.correct_words = 0
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.current_sentence = random.choice(self.sentences)
        self.text_label.config(text=self.current_sentence)
        self.root.bind('<Return>', self.check_input)

    def check_input(self, event):
        user_input = self.entry.get()
        typed_words = user_input.split()
        original_words = self.current_sentence.split()

        for i in range(min(len(typed_words), len(original_words))):
            if typed_words[i] == original_words[i]:
                self.correct_words += 1

        accuracy = (self.correct_words / len(original_words)) * 100
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        words_per_minute = (len(typed_words) / elapsed_time) * 60

        result_message = f"Time taken: {elapsed_time:.2f} seconds\nAccuracy: {accuracy:.2f}%\nWords per minute: {words_per_minute:.2f} WPM"
        self.result_label.config(text=result_message)

        self.start_button.config(state=tk.NORMAL)
        self.entry.config(state=tk.DISABLED)
        self.root.unbind('<Return>')

        messagebox.showinfo("Test Finished", result_message)


if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTestGUI(root)
    root.mainloop()
