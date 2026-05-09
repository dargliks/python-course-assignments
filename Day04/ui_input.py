from logic import determine_nuclei_types, calc_CSP

print("experiment type selection")
print("1  -  NH HSQC")
print("2  -  Methyl-TROSY/HMQC")

exp_type = int(input("please select your experiment type:" ))

nuc1_type, nuc2_type, fact_a, fact_b = determine_nuclei_types (exp_type)

nuc1_f1 = float(input(f"please insert the first {nuc1_type} frequency (in ppm):"))
nuc2_f1 = float(input(f"please insert the first {nuc2_type} frequency (in ppm):"))
nuc1_f2 = float(input(f"please insert the second {nuc1_type} frequency (in ppm):"))
nuc2_f2 = float(input(f"please insert the second {nuc2_type} frequency (in ppm):"))

CSP_val = calc_CSP(nuc1_f1,nuc1_f2,nuc2_f1,nuc2_f2,fact_a,fact_b)

print (f"your CSP value is {CSP_val:.3f}")