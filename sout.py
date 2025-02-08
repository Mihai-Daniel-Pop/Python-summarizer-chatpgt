import tkinter as tk
from tkinter import scrolledtext
import openai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv(dotenv_path="key.env")
print("Env file loaded:", os.path.isfile("key.env"))  # Check if the file exists
print(f"Loaded API key: {os.getenv('OPENAI_API_KEY')}")
print("Make sure the key above is correct!")

# Set your OpenAI API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure the key matches EXACTLY what's in the .env file


# Function to summarize text
def summarize_text():
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        result_display.delete("1.0", tk.END)
        result_display.insert(tk.END, "⚠️ Please enter some text to summarize.")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" for even better results
            messages=[{"role": "user", "content": f"Summarize the following text:\n\n{input_text}"}],
            max_tokens=1200
        )
        summary = response.choices[0].message.content.strip()
        result_display.delete("1.0", tk.END)
        result_display.insert(tk.END, summary)
    except Exception as e:
        result_display.delete("1.0", tk.END)
        result_display.insert(tk.END, f"❌ Error: {str(e)}")

# Create the Tkinter window
root = tk.Tk()
root.title("Summarizer")
root.geometry("700x600")
root.configure(bg="#1e1e2f")  # Dark modern background color

# Custom Fonts and Colors
label_font = ("Helvetica", 14, "bold")
button_font = ("Helvetica", 12)
text_font = ("Courier New", 12)

# Title Label
tk.Label(root, text="✨ Text Summarizer ✨", font=("Helvetica", 20, "bold"), fg="white", bg="#1e1e2f").pack(pady=10)

# Input text box with label
tk.Label(root, text="📜 Enter Text to Summarize:", font=label_font, fg="white", bg="#1e1e2f").pack(anchor="w", padx=20, pady=5)
text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, font=text_font, bg="#2d2d44", fg="white", insertbackground="white")
text_input.pack(padx=20, pady=10)

# Summarize button
summarize_button = tk.Button(root, text="🔍 Summarize", font=button_font, bg="#3a3f58", fg="white", activebackground="#575c75", activeforeground="white", command=summarize_text, relief="flat", padx=10, pady=5)
summarize_button.pack(pady=20)

# Result display box with label
tk.Label(root, text="📝 Summary:", font=label_font, fg="white", bg="#1e1e2f").pack(anchor="w", padx=20, pady=5)
result_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, font=text_font, bg="#2d2d44", fg="white", insertbackground="white")
result_display.pack(padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()