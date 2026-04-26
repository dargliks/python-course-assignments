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
        type1 = "1H"
        type2 = "13C"
        factor_a = 1
        factor_b = 5

    return (type1, type2, factor_a, factor_b)