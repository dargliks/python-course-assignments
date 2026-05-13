# Explanation:
This is a basic program for calculating the Chemical Shift Perturbations of an NMR peak between two 2D NMR spectra (taken in different conditions). 
The "logic" file includes 2 modules - one for determining the coefficients for the calculation based on the experiment type (currently 2 types are supported - which are the main ones used in our lab), and the second to calculate the CSPs for that experiment type. 

The formula for chemical shift perturbations is: CSP = (sqrt(a*(H1-H2)^2 + (b*(N1-N2))^2))/2

NOTE: due to being sick for a lot of this week, I did not manage to fininsh and specifically did not create the test file for this assignment. I apologize for that. If it is acceptable, I will attempt to make it up at a later time.

## Sample input and output:

Choose "1" for experiment type
H1 = 7.22 N1 = 112.64 H2 = 7.556 N2 = 117.593

output CSP should start with 0.523

# AI use:

ChatGPT online

## prompts:

1. "in python, if a function returns more than one variable as output, how do I ask for a specific one of thoes?"

1. "in python, can I insert a string variable into a code line that also requests input?"

1. "I wrote a python code that recieves user input (via the "input" command), calls a couple of modules to run on the input then return an output value. If I show you this code, can you write me a new code that will do the same via a tkinter gui?"



