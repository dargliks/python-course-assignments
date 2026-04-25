H1 = float(input("Spectrum 1 proton frequency (in ppm): "))
N1 = float(input("Spectrum 1 nitrogen frequency (in ppm): "))
H2 = float(input("Spectrum 2 proton frequency (in ppm): "))
N2 = float(input("Spectrum 2 nitrogen frequency (in ppm): "))

H_CSP = H1-H2
N_CSP = N1-N2

CSP_val = (((H_CSP **2) + ((N_CSP *0.2) **2)) **0.5)/2

print ("Chemical Shift perturbation for this peak is: ", CSP_val)