from logic import determine_nuclei_types, calc_CSP, read_experiment_file

# Experiment type selection
print("experiment type selection")
print("1  -  NH HSQC")
print("2  -  Methyl-TROSY/HMQC")

exp_type = int(input("please select your experiment type:" ))

nuc1_type, nuc2_type, fact_a, fact_b = determine_nuclei_types (exp_type)

# Read files
file1 = input("Enter first experiment filename: ")
file2 = input("Enter second experiment filename: ")

exp1_data = read_experiment_file(file1)
exp2_data = read_experiment_file(file2)

#compare peaks and export results
with open("CSP_results.txt", "w") as outfile:

    outfile.write("peak_name\tCSP\n")

    for peak_name in exp1_data:
        
        #check peak exists in both files
        if peak_name not in exp2_data:
            continue

        nuc1_f1, nuc2_f1 = exp1_data[peak_name]
        nuc1_f2, nuc2_f2 = exp2_data[peak_name]

        CSP_val = calc_CSP(nuc1_f1, nuc1_f2,nuc2_f1,nuc2_f2,fact_a,fact_b)

        outfile.write(f"{peak_name}\t{CSP_val:.3f}\n")