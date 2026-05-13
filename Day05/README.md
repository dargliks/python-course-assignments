# Explanation:
This is a basic program for calculating the Chemical Shift Perturbations of an NMR peak between two 2D NMR spectra (taken in different conditions). 
The "logic" file includes 2 modules:
1. a module for determining the coefficients for the calculation based on the experiment type (currently 2 types are supported - which are the main ones used in our lab) 
1. a module for calculating the CSPs for that experiment type. 

The formula for chemical shift perturbations is: CSP = (sqrt(a*(H1-H2)^2 + (b*(N1-N2))^2))/2

This is an improved version of the read from file calculator from last week:
* A simple GUI for file selection is now implemented
* The output is now a CSV file instead of a text, and it includes the raw data next to the results (for manual examination which is sometimes needed for our data). 
* the resulting CSPs are plotted in a bar plot by the residue name (this is the preferred way to present such data in our lab).


I included two files with example datasets for your convenience (select HN-HSQC for experiment type to run these).

# required installations 
this version requires that you to install the following:
* PANDAS
* matplotlib