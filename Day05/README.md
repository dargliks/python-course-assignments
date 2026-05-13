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


I included two files with example datasets for your convenience (select HN-HSQC for experiment type to run these. Note that you may need to select "all file types" in the file selector to see them).

# required installations 
this version requires that you to install the following:
* PANDAS
* matplotlib

# AI use
I used ChatGPT online, using this prompt:

"Hi! I have a python code that reads two CSV files, performs a calculation on the data from them, and then exports the results into another file. can you help me improve it a bit? I want to have a GUI (using tkinter) for selecting the input files, and I want the output file to include the raw data for each row next to the calculation result, and also to plot the calculation results. can you do these things?"

(I later corrected myself to state that the code is meant for text files as input instead of CSVs, which the chat also noticed).