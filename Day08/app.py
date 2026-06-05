import streamlit as st

from CSP_calculator import calc_CSP, parse_experiment_data, determine_nuclei_types

st.title ("Protein NMR - CSP calculator")

st.write ("welcome to the chemical shift perturbation calculator!")
st.write ("upload your NMR peak lists and compute CSP values.")

#select experiment type
exp_type = st.radio(
    "Experiment Type",
    options=[1, 2],
    format_func=lambda x: "NH HSQC" if x == 1 else "Methyl-TROSY/HMQC"
)

#upload data files
file1 = st.file_uploader("Experiment File 1")
file2 = st.file_uploader("Experiment File 2")

if st.button("Process Files"):

    if file1 is None or file2 is None:
        st.error("Please upload both files.")
    else:
        #read data files
        text1 = file1.getvalue().decode()
        text2 = file2.getvalue().decode()

        lines1 = text1.splitlines()
        lines2 = text2.splitlines()
        
        lines1 = file1.getvalue().decode().splitlines()
        lines2 = file2.getvalue().decode().splitlines()

        exp1_data = parse_experiment_data(lines1)
        exp2_data = parse_experiment_data(lines2)

        st.success("Files parsed successfully.")

