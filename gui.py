import tkinter as tk
from tkinter import ttk
from scorer import evaluate_password

def analyze():
    pwd = pwd_entry.get()
    if not pwd:
        score_label.config(text="Please enter a password", foreground="black")
        feedback_box.delete("1.0", tk.END)
        return
    
    result = evaluate_password(pwd)
    
    rating = result["rating"]
    score = result["score"]
    
    colors = {
        "Weak": "#D9534F",
        "Moderate": "#F0AD4E",
        "Strong": "#5BC0DE",
        "Very Strong": "#5CB85C"
    }
    
    score_label.config(
        text=f"{rating} ({score}/100) | Entropy: {result['entropy']} bits",
        foreground=colors.get(rating, "black")
    )
    
    feedback_box.delete("1.0", tk.END)
    if result["breach_count"] > 0:
        feedback_box.insert(tk.END, f"⚠️ CRITICAL: Found in {result['breach_count']:,} data breaches!\n\n")
        
    if result["feedback"]:
        feedback_box.insert(tk.END, "Recommendations:\n")
        for tip in result["feedback"]:
            feedback_box.insert(tk.END, f"• {tip}\n")
    else:
        feedback_box.insert(tk.END, "✓ Excellent! This password passes all security checks.")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("460x420")
root.resizable(False, False)

title_label = ttk.Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold"))
title_label.pack(pady=12)

frame = ttk.Frame(root, padding=10)
frame.pack(fill="x")

entry_label = ttk.Label(frame, text="Enter Password:")
entry_label.pack(anchor="w")

pwd_entry = ttk.Entry(frame, font=("Helvetica", 12), show="*")
pwd_entry.pack(fill="x", pady=5)

check_btn = ttk.Button(frame, text="Check Strength", command=analyze)
check_btn.pack(pady=8)

score_label = ttk.Label(root, text="Enter a password to begin", font=("Helvetica", 12, "bold"))
score_label.pack(pady=5)

feedback_box = tk.Text(root, height=10, width=50, font=("Helvetica", 10), wrap="word")
feedback_box.pack(pady=10, padx=15)

root.mainloop()
