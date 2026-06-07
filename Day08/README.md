# Explanation:
This web app is a basic program for calculating the Chemical Shift Perturbations of an NMR peak between two 2D NMR spectra (taken in different conditions). 

The formula for chemical shift perturbations is: CSP = (sqrt(a*(H1-H2)^2 + (b*(N1-N2))^2))/2
with a and b being factors that change depending on the types of nuclei measured (or, to simplify, on experiment type).

This project is a modification of the Day05 assignment into a web application, using Streamlit as the framework. The basic business logic is maintained from Day05, though some cleanup was done in separating the logic from the UI. Test files for both the logic and the web application are added in the tests folder, which can be run with pytest. 

As usual, I also included in the folder two files with example datasets for your convenience (select HN-HSQC for experiment type to run these).

# required installations 
this version requires that you to install the following:
* PANDAS
* matplotlib
* Streamlit

# AI use
I used ChatGPT online for this project. I had a long conversation with the chat, asking it to help me modify my code step-by-step and explaining each change rather than just writing the new code itself. I did this over a few days, and unfortunately a lot of the earlier part of the conversation was not logged in time, so I cannot provide the original prompt - but I learned from this how to make sure it doesn't happen in future!