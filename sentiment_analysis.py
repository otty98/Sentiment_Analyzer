from textblob import TextBlob
import tkinter as tk
import random

def analyze_sentiment():
    # Button animation 
    analyze_button.config(text="Analyzing...", bg="#FF6B6B", state="disabled")
    window.update()
    
    text = entry.get("1.0", tk.END).strip()
    if not text:
        result_label.config(text="Please enter some text.", fg="#FF6B6B")
        analyze_button.config(text="Analyze", bg="#4ECDC4", state="normal")
        return
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😀"
        color = "#2ECC71"  
        bg_color = "#E8F5E8"
    elif polarity < 0:
        sentiment = "Negative 😠"
        color = "#E74C3C"  
        bg_color = "#FFEBEE"
    else:
        sentiment = "Neutral 😐"
        color = "#F39C12"  

    # Animate result appearance
    result_label.config(text="", bg=bg_color)
    window.update()
    
    # Typewriter effect for result
    full_text = f"Sentiment: {sentiment}\nPolarity Score: {polarity:.2f}"
    for i in range(len(full_text) + 1):
        result_label.config(text=full_text[:i], fg=color)
        window.update()
        window.after(30)  # Small delay for typewriter effect
    
    # Reset button
    analyze_button.config(text="Analyze", bg="#4ECDC4", state="normal")

def animate_button_hover(event):
    colors = ["#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD", "#98D8C8"]
    analyze_button.config(bg=random.choice(colors))

def reset_button_color(event):
    analyze_button.config(bg="#4ECDC4")

def clear_text():
    entry.delete("1.0", tk.END)
    result_label.config(text="", bg="#F8F9FA")

# Create main window
window = tk.Tk()
window.title("✨ Sentiment Analyzer ✨")
window.geometry("500x400")
window.resizable(True, True)
window.configure(bg="#2C3E50")

# GUI Layout - define widgets with colors and styling
title_label = tk.Label(window, text="🎭 SENTIMENT ANALYZER 🎭", 
                      font=("Arial", 16, "bold"), 
                      fg="#ECF0F1", bg="#2C3E50")
title_label.pack(pady=15)

label = tk.Label(window, text="Enter text to analyze:", 
                font=("Arial", 12), 
                fg="#ECF0F1", bg="#2C3E50")
label.pack(pady=5)

# Text entry with styling
entry = tk.Text(window, height=5, width=45, 
               font=("Arial", 11),
               bg="#ECF0F1", fg="#2C3E50",
               relief="flat", bd=5,
               insertbackground="#2C3E50")
entry.pack(pady=10, padx=20)

# Button frame for better layout
button_frame = tk.Frame(window, bg="#2C3E50")
button_frame.pack(pady=10)

# Analyze button with hover effects
analyze_button = tk.Button(button_frame, text="✨ Analyze ✨", 
                          command=analyze_sentiment,
                          font=("Arial", 12, "bold"),
                          bg="#4ECDC4", fg="white",
                          relief="flat", bd=0,
                          padx=20, pady=5,
                          cursor="hand2")
analyze_button.pack(side=tk.LEFT, padx=5)

# Clear button
clear_button = tk.Button(button_frame, text="🗑️ Clear", 
                        command=clear_text,
                        font=("Arial", 12, "bold"),
                        bg="#E74C3C", fg="white",
                        relief="flat", bd=0,
                        padx=20, pady=5,
                        cursor="hand2")
clear_button.pack(side=tk.LEFT, padx=5)

# Bind hover effects
analyze_button.bind("<Enter>", animate_button_hover)
analyze_button.bind("<Leave>", reset_button_color)

# Result label with dynamic background
result_label = tk.Label(window, text="Ready to analyze your text! 🚀", 
                       font=("Arial", 12, "bold"), 
                       wraplength=400,
                       bg="#F8F9FA", fg="#2C3E50",
                       relief="ridge", bd=2,
                       padx=20, pady=15)
result_label.pack(pady=20, padx=20, fill=tk.X)

# Run the GUI loop
if __name__ == "__main__":
    window.mainloop()
