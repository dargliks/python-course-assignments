import pandas as pd
import matplotlib.pyplot as plt


def calc_CSP(nuc1_f1, nuc1_f2, nuc2_f1, nuc2_f2, a, b):
    
    #calculate shift for each dimention individually:
    nuc1_shift = nuc1_f1-nuc1_f2
    nuc2_shift = nuc2_f1-nuc2_f2

    #normalize by factors depending on nucleus type
    nuc1_norm = a * nuc1_shift
    nuc2_norm = b * nuc2_shift

    #calculate total chemical shift perturbation
    CSP_tot = (((nuc1_norm **2) + (nuc2_norm **2)) **0.5)/2

    #if __name__ == "__main__"

    return CSP_tot


def determine_nuclei_types(exp_type):

    if exp_type == 1:
        type1 = "1H"
        type2 = "15N"
        factor_a = 1
        factor_b = 0.2

    if exp_type == 2:
        type1 = "13C"
        type2 = "1H"
        factor_a = 1
        factor_b = 5


    return (type1, type2, factor_a, factor_b)


def parse_experiment_data(lines):

    peaks = {}


    # Skip header
    lines = lines[1:]

    for line_number, line in enumerate(lines, start=2):

        line = line.strip()

        #test that line is valid
        if not line:
            continue

        #split line into parts and verify that all needed data is in the line
        parts = line.split()

        if len(parts) < 3:
            print(f"Skipping bad line {line_number}")
            continue

        #collect data from lines
        try:
            peak_name = parts[0]
            w1 = float(parts[1])
            w2 = float(parts[2])

            peaks[peak_name] = (w1, w2)

        except ValueError:
            print(f"Non-numeric data on line {line_number}")

    return peaks

def calculate_csp_results (exp_type, exp1_data, exp2_data):

    nuc1_type, nuc2_type, fact_a, fact_b = determine_nuclei_types(exp_type)

    results = []

    for peak_name in exp1_data:

        if peak_name not in exp2_data:
            #missing_peaks.append(peak_name)
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

    #plot results
    plt.figure(figsize=(10, 5))
    plt.bar(df["Peak"], df["CSP"])

    plt.xlabel("Peak")
    plt.ylabel("CSP")
    plt.title("Chemical Shift Perturbation")

    plt.xticks(rotation=90)
    plt.tight_layout()

    fig = plt.gcf()

    return df, fig


    