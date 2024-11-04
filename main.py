import streamlit as st
from fpdf import FPDF
import os

# Ensure the 'assets' directory exists
assets_folder = "assets"
os.makedirs(assets_folder, exist_ok=True)

# Function to create a PDF with personal and user inputs
def create_pdf(answers):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Logo Design Questionnaire", 0, 1, "C")
    pdf.ln(5)

    # Add questions and answers
    for question, answer in answers.items():
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(0, 10, question)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 10, answer if answer else "No answer provided")
        pdf.ln(5)

    output_filename = os.path.join(assets_folder, "logo_questionnaire_filled.pdf")
    pdf.output(output_filename)
    return output_filename

# Streamlit web app
st.title("Logo Design Questionnaire")
st.write("**Welcome!** Please fill out the questionnaire to help us understand your logo design needs. Our services include professional logo design, branding, and the Complete Solution for Printing & Packaging Services.")

# Questions for the form
questions = [
    "1. What is the name of your company?",
    "2. Do you have a tagline that should be included in the logo?",
    "3. What is your industry or field of work?",
    "4. Who is your target audience?",
    "5. Do you prefer a modern, classic, playful, or elegant design?",
    "6. Are there specific colors you want to be included and if, please mention the hex code?",
    "7. Are there existing logos you like and why?",
    "8. Who are your competitors?",
    "9. Where will the logo be used (e.g., website, business cards, merchandise)?",
    "10. What message or emotions should the logo convey?",
    "11. Are there any specific shapes or symbols you associate with your brand?",
    "12. What is your brand's personality (e.g., friendly, corporate, innovative)?",
    "13. How soon do you need the logo?",
    "14. Do you have any fonts or typography preferences?",
    "15. What type of logo are you envisioning (e.g., wordmark, icon-based, combination)?",
    "16. Are there any specific design trends you want to avoid?",
    "17. Any other relevant information or preferences?",
]

# Collect answers
answers = {question: st.text_input(question) for question in questions}

# Generate PDF button
if st.button("Generate PDF"):
    try:
        pdf_path = create_pdf(answers)
        st.success("PDF created successfully!")
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="Download PDF",
                data=pdf_file.read(),
                file_name="logo_questionnaire_filled.pdf",
                mime="application/pdf"
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")


