import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport

st.set_page_config(layout="wide")

st.title("Interactive Data Profiling with Streamlit")

# Option to upload a CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)
    st.write("### Original DataFrame (First 5 rows):")
    st.write(df.head())

    st.write("---")
    st.write("### Generating Profile Report...")

    # Generate the pandas profiling report
    # You can customize the report generation with various options
    # For example, minimal=True for a lighter report, explorative=True for more details
    profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

    # Display the report in Streamlit
    st_profile_report(profile)

else:
    st.info("Please upload a CSV file to generate the data profile report.")
