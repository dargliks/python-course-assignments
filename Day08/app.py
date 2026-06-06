import streamlit as st
import CSP_calculator as cc

from io import BytesIO

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

        #parse data files
        exp1_data = cc.parse_experiment_data(lines1)
        exp2_data = cc.parse_experiment_data(lines2)

        #run calculation
        df,fig = cc.calculate_csp_results(exp_type, exp1_data, exp2_data)

        st.session_state.df = df
        st.session_state.fig = fig


if "df" in st.session_state:

    #display results
    st.subheader("Results Table")
    st.dataframe(st.session_state.df)

    csv_data = st.session_state.df.to_csv(index=False)

    #download results
    st.download_button(
        label="Download Results CSV",
        data=csv_data,
        file_name="csp_results.csv",
        mime="text/csv"
    )

if "fig" in st.session_state:
    #display plot
    st.subheader("CSP Plot")
    st.pyplot(st.session_state.fig)

    #download plot
    png_buffer = BytesIO()
    st.session_state.fig.savefig(png_buffer, format="png")
    png_buffer.seek(0)

    svg_buffer = BytesIO()
    st.session_state.fig.savefig(svg_buffer, format="svg")
    svg_buffer.seek(0)
        
    st.download_button(
        label="Download Plot PNG",
        data=png_buffer,
        file_name="csp_plot.png",
        mime="image/png"
    )

    st.download_button(
    label="Download Plot SVG",
    data=svg_buffer,
    file_name="csp_plot.svg",
    mime="image/svg+xml"
)

