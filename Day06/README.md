# Protein Structure Analyzer

## Description

The Protein Data Bank (PDB) is a publicly available database that contains three-dimensional structures of biological macromolecules, including proteins, nucleic acids, and protein complexes. The structures are determined using experimental techniques such as X-ray crystallography, solution NMR spectroscopy, and cryo-electron microscopy (cryo-EM). In addition to the atomic coordinates of each structure, the PDB provides metadata such as the protein title, experimental method, authors, deposition information, and structural statistics.

This program connects to the PDB through its web API, downloads information for a user-specified PDB entry, and generates a short report about the structure. The program retrieves metadata from the PDB, downloads the corresponding coordinate file, and processes it to calculate several structural properties.

The report includes:

* PDB ID
* Structure title
* Experimental method
* Resolution (when available)
* Number of chains
* Number of residues
* Number of atoms
* Average number of atoms per residue
* Atom composition by element

## Requirements

The program requires Python 3 and the requests package.

Install the required package with:

pip install requests

## How to Run

Run the program from the command line:

python PDB_analyzer.py

When prompted, enter a valid PDB ID.

### Example input
2LGW

This entry corresponds to a protein structure determined by solution NMR and provides a good example for testing the program.

## AI Contribution

OpenAI's ChatGPT was used as a programming assistant during this assignment. AI assisted in brainstorming the project idea, explaining the PDB API, and helping write and review the Python code and this README. The overall project selection, design decisions, testing, and final code selection were performed by the student.