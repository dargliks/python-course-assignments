import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt

from logic import determine_nuclei_types, calc_CSP


# =========================
# Read experiment file
# =========================
def read_experiment_file(filename):

    peaks = {}

    with open(filename, "r") as file:

        # Skip header
        next(file)

        for line_number, line in enumerate(file, start=2):

            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) < 3:
                print(f"Skipping bad line {line_number}")
                continue

            try:
                peak_name = parts[0]
                w1 = float(parts[1])
                w2 = float(parts[2])

                peaks[peak_name] = (w1, w2)

            except ValueError:
                print(f"Non-numeric data on line {line_number}")

    return peaks


# =========================
# Browse for files
# =========================
def browse_file(entry):

    filename = filedialog.askopenfilename(
        filetypes=[("CSV or text files", "*.csv *.txt"), ("All files", "*.*")]
    )

    if filename:
        entry.delete(0, tk.END)
        entry.insert(0, filename)


# =========================
# Main processing function
# =========================
def process_files():

    try:

        file1 = entry_file1.get()
        file2 = entry_file2.get()

        if not file1 or not file2:
            messagebox.showerror("Error", "Please select both input files.")
            return

        exp_type = exp_var.get()

        nuc1_type, nuc2_type, fact_a, fact_b = determine_nuclei_types(exp_type)

        exp1_data = read_experiment_file(file1)
        exp2_data = read_experiment_file(file2)

        results = []

        for peak_name in exp1_data:

            if peak_name not in exp2_data:
                continue

            nuc1_f1, nuc2_f1 = exp1_data[peak_name]
            nuc1_f2, nuc2_f2 = exp2_data[peak_name]

            CSP_val = calc_CSP(
                nuc1_f1,
                nuc1_f2,
                nuc2_f1,
                nuc2_f2,
                fact_a,
                fact_b
            )

            results.append({
                "Peak": peak_name,
                "Exp1_W1": nuc1_f1,
                "Exp1_W2": nuc2_f1,
                "Exp2_W1": nuc1_f2,
                "Exp2_W2": nuc2_f2,
                "CSP": round(CSP_val, 3)
            })

        # Create dataframe
        df = pd.DataFrame(results)

        # Save results
        output_file = "CSP_results.csv"
        df.to_csv(output_file, index=False)

        # Plot CSP values
        plt.figure(figsize=(10, 5))
        plt.bar(df["Peak"], df["CSP"])

        plt.xlabel("Peak")
        plt.ylabel("CSP")
        plt.title("Chemical Shift Perturbation")

        plt.xticks(rotation=90)
        plt.tight_layout()

        # Save plot
        plot_file = "CSP_plot.png"
        plt.savefig(plot_file)

        # Show plot
        plt.show()

        messagebox.showinfo(
            "Success",
            f"Results saved to:\n{output_file}\n\nPlot saved to:\n{plot_file}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================
# GUI
# =========================
root = tk.Tk()
root.title("CSP Calculator")
root.geometry("600x250")


# File 1
tk.Label(root, text="Experiment File 1").grid(row=0, column=0, padx=10, pady=10)

entry_file1 = tk.Entry(root, width=50)
entry_file1.grid(row=0, column=1)

tk.Button(
    root,
    text="Browse",
    command=lambda: browse_file(entry_file1)
).grid(row=0, column=2, padx=5)


# File 2
tk.Label(root, text="Experiment File 2").grid(row=1, column=0, padx=10, pady=10)

entry_file2 = tk.Entry(root, width=50)
entry_file2.grid(row=1, column=1)

tk.Button(
    root,
    text="Browse",
    command=lambda: browse_file(entry_file2)
).grid(row=1, column=2, padx=5)


# Experiment type
tk.Label(root, text="Experiment Type").grid(row=2, column=0, padx=10, pady=10)

exp_var = tk.IntVar(value=1)

tk.Radiobutton(
    root,
    text="NH HSQC",
    variable=exp_var,
    value=1
).grid(row=2, column=1, sticky="w")

tk.Radiobutton(
    root,
    text="Methyl-TROSY/HMQC",
    variable=exp_var,
    value=2
).grid(row=3, column=1, sticky="w")


# Run button
tk.Button(
    root,
    text="Process Files",
    command=process_files,
    bg="lightblue",
    height=2,
    width=20
).grid(row=4, column=1, pady=20)


root.mainloop()