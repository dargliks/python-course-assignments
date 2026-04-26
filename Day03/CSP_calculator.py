#this is a simple program that calculates the chemical shift perturbations of a peak from two NMR spectra
#currently designed for H-N 2D HSQC experiments (future goal: expand to further types of spectra)
#currently requires manually entering the frequencies for a single peak (future goal: load frequencies from a file, to calculate multiple peaks simultaniously)

#created by Dar Gliksberg, 25/04/26

#input
H1 = float(input("Spectrum 1 proton frequency (in ppm): "))
N1 = float(input("Spectrum 1 nitrogen frequency (in ppm): "))
H2 = float(input("Spectrum 2 proton frequency (in ppm): "))
N2 = float(input("Spectrum 2 nitrogen frequency (in ppm): "))

#calculations
H_CSP = H1-H2
N_CSP = N1-N2

CSP_val = (((H_CSP **2) + ((N_CSP *0.2) **2)) **0.5)/2

#print the output
print ("Chemical Shift perturbation for this peak is: ", CSP_val)