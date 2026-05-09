import tkinter as tk
from tkinter import ttk
from logic import determine_nuclei_types, calc_CSP

def update_labels():
    try:
        exp_type = int(exp_var.get())
        nuc1_type, nuc2_type, _, _ = determine_nuclei_types(exp_type)

        label_nuc1_f1.config(text=f"First {nuc1_type} frequency (ppm):")
        label_nuc2_f1.config(text=f"First {nuc2_type} frequency (ppm):")
        label_nuc1_f2.config(text=f"Second {nuc1_type} frequency (ppm):")
        label_nuc2_f2.config(text=f"Second {nuc2_type} frequency (ppm):")
    except:
        pass

def calculate():
    try:
        exp_type = int(exp_var.get())
        nuc1_type, nuc2_type, fact_a, fact_b = determine_nuclei_types(exp_type)

        nuc1_f1 = float(entry_nuc1_f1.get())
        nuc2_f1 = float(entry_nuc2_f1.get())
        nuc1_f2 = float(entry_nuc1_f2.get())
        nuc2_f2 = float(entry_nuc2_f2.get())

        CSP_val = calc_CSP(nuc1_f1, nuc1_f2, nuc2_f1, nuc2_f2, fact_a, fact_b)

        result_label.config(text=f"CSP value: {CSP_val:.3f}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# --- GUI setup ---
root = tk.Tk()
root.title("CSP Calculator")

# Experiment type
tk.Label(root, text="Select experiment type:").grid(row=0, column=0, columnspan=2)

exp_var = tk.StringVar(value="1")

ttk.Radiobutton(root, text="NH HSQC", variable=exp_var, value="1", command=update_labels).grid(row=1, column=0, sticky="w")
ttk.Radiobutton(root, text="Methyl-TROSY/HMQC", variable=exp_var, value="2", command=update_labels).grid(row=1, column=1, sticky="w")

# Input fields
label_nuc1_f1 = tk.Label(root, text="First frequency:")
label_nuc1_f1.grid(row=2, column=0)
entry_nuc1_f1 = tk.Entry(root)
entry_nuc1_f1.grid(row=2, column=1)

label_nuc2_f1 = tk.Label(root, text="Second frequency:")
label_nuc2_f1.grid(row=3, column=0)
entry_nuc2_f1 = tk.Entry(root)
entry_nuc2_f1.grid(row=3, column=1)

label_nuc1_f2 = tk.Label(root, text="Third frequency:")
label_nuc1_f2.grid(row=4, column=0)
entry_nuc1_f2 = tk.Entry(root)
entry_nuc1_f2.grid(row=4, column=1)

label_nuc2_f2 = tk.Label(root, text="Fourth frequency:")
label_nuc2_f2.grid(row=5, column=0)
entry_nuc2_f2 = tk.Entry(root)
entry_nuc2_f2.grid(row=5, column=1)

# Calculate button
tk.Button(root, text="Calculate CSP", command=calculate).grid(row=6, column=0, columnspan=2)

# Result display
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2)

# Initialize labels correctly
update_labels()

root.mainloop()