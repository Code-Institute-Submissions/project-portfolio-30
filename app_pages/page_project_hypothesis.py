import streamlit as st
import matplotlib.pyplot as plt

# Credit to to the Code Institute "Malaria Detector" walkthrough project
def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* I suspect that leaves affected by powdery mildew will show clear marks/signs. "
        f"An Image Montage shows that typically, leaves infected with mildew will have clear powdery patches of fungus,"
        f"thereby making the leaves appear as if they have been dusted with flour.\n\n"
        f"* Whereas healthy leaves will be light green in colour."
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )
