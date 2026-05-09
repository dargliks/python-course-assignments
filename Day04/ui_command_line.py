import sys
from logic import determine_nuclei_types, calc_CSP

if len(sys.argv)!= 6:
    
    print ("usage: python ui_command_line.py <exp_type> <H1> <N/C1>, <H2> ,<N/C2>")
    print ("<H1> - 1H frequency from the first spectrum")
    print ("<N/C1> - 15N or 13C frequency from the first spectrum")
    print ("<H2> - 1H frequency from the second spectrum")
    print ("<N/C2> - 15N or 13C frequency from the second spectrum")
    print ("<exp_type> - type 1 for HN HSQC or 2 for Methyl-trosy HMQC")
    sys.exit(1)


exp_type = int(sys.argv[1])

_,_,a,b = determine_nuclei_types(exp_type)

nuc1_f1 = float(sys.argv[2])
nuc2_f1 = float(sys.argv[3])
nuc1_f2 = float(sys.argv[4])
nuc2_f2 = float(sys.argv[5])

CSP_val = calc_CSP(nuc1_f1,nuc1_f2,nuc2_f1,nuc2_f2,a,b)

print (f"your CSP value is {CSP_val:.3f}")



