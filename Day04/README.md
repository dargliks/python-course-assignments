# Explanation:
This is a basic program for calculating the Chemical Shift Perturbations of an NMR peak between two 2D NMR spectra (taken in different conditions). 
The "logic" file includes 2 modules:
1. a module for determining the coefficients for the calculation based on the experiment type (currently 2 types are supported - which are the main ones used in our lab) 
1. a module for calculating the CSPs for that experiment type. 

The formula for chemical shift perturbations is: CSP = (sqrt(a*(H1-H2)^2 + (b*(N1-N2))^2))/2

The CSP_calculator_from_datafiles file is the new feature that I added this week, which enables the prpgram to read a text file with real experimental data (which can contain a large amount of peaks in each experiment), do the calculation for each peak, and return a text file with the CSP calcuation for each peak next to its name. This is something I planned to do since the start, and was also suggested in the peer review. 

I included two files with example datasets for your convenience (select 1 for experiment type to run these).

NOTE: Still no proper test file, sorry! I'm still trying to catch up with everything I missed last week.

# AI usage:
I used ChatGPT, which helped in writing the code for reading the text files. It also suggested including the verifications for empty lines, corrupted lines, and mismatched lines. 

# peer review:
I submitted issues for Alona and Stav, and suggested features they could add to their codes.
* for Alona: I suggested adding a translation feature to her DNA analysis tool
* for Stav: I suggested making to add to her dilution calculator the ability to calculate the required stock volume to reach a desired final volume. 
