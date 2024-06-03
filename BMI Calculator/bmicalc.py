import tkinter as tk
from tkinter import messagebox

def feet_and_inches_to_meters(feet, inches):
    meters_from_feet = feet * 0.3048
    meters_from_inches = inches * 0.0254
    return meters_from_feet + meters_from_inches

def calculate_bmi(weight_kg, height_meters):
    return weight_kg / (height_meters * height_meters)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"

def on_calculate():
    try:
        feet = float(entry_feet.get())
        inches = float(entry_inches.get())
        weight_kg = float(entry_weight.get())

        height_meters = feet_and_inches_to_meters(feet, inches)
        bmi = calculate_bmi(weight_kg, height_meters)
        classification = classify_bmi(bmi)

        result_label.config(text=f"BMI: {bmi:.2f}\nClassification: {classification}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for feet, inches, and weight.")


root = tk.Tk()
root.title("BMI Calculator")


tk.Label(root, text="Height (feet):").grid(row=0, column=0, padx=10, pady=5)
entry_feet = tk.Entry(root)
entry_feet.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Height (inches):").grid(row=1, column=0, padx=10, pady=5)
entry_inches = tk.Entry(root)
entry_inches.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Weight (kg):").grid(row=2, column=0, padx=10, pady=5)
entry_weight = tk.Entry(root)
entry_weight.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Calculate BMI", command=on_calculate)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()