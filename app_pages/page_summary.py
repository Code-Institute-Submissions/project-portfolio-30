import streamlit as st
import matplotlib.pyplot as plt

# Credit to to the Code Institute "Malaria Detector" walkthrough project
def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* According to [RHS](https://www.rhs.org.uk/disease/powdery-mildews), Powdery mildew is a fungal disease of the foliage,"
        f"stems and occasionally flowers and fruit where a "
        f"superficial fungal growth covers the surface of the plant.\n"
        f"* A photograph of a cherry leaf is taken and examined. "
        f"Visual criteria are used to detect mildew fungus, as mildew infected "
        f"leaves, will appear to have been dusted with flour.\n"
        f"**Project Dataset**\n"
        f"* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy "
        f"cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. "
        f"The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned "
        f"about supplying the market with a compromised quality product.\n\n"
        )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/StephenB92/project-portfolio-5/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate "
        f"a healthy cherry leaf from one with powdery mildew. \n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )