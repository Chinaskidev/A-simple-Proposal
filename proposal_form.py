import streamlit as st
import pandas as pd
from datetime import datetime

# aca vamos a guardar las propuestas
def save_proposal(data, filename='proposals.csv'):
    df = pd.DataFrame([data])
    df.to_csv(filename, mode='a', header=False, index=False)


# estilos de la pagina
st.set_page_config(page_title="The Haberdashery Working Proposal", layout="centered")

# Mostrar imagen
st.image("haber.png", caption="The Haberdashery", use_column_width=80 )
st.title("The Haberdashery Working Proposal")
st.write("Propose new ideas for operations, treasury management, initiatives, and more.")

# Crear formulario para propuestas
with st.form("proposal_form"):
    # Proposal Title
    title = st.text_input("Proposal Title", help="Enter the title of your proposal")

    # Categoria
    category = st.selectbox(
        "Category",
        ["Operations", "Treasury Management", "New Initiative", "Other"],
        help="Select the category that best fits your proposal"
    )

    # Descripcion
    description = st.text_area(
        "Proposal Description",
        help="Provide a detailed description of your proposal"
    )

    # Adicional  detalles
    additional_details = st.text_area(
        "Additional Details (Optional)",
        help="Any additional information, budget requirements, timeline, etc."
    )

    # boton de enviar
    submitted = st.form_submit_button("Submit Proposal")

    if submitted:
        if title and category and description:
            # Prepare data
            proposal_data = {
                "title": title,
                "category": category,
                "description": description,
                "additional_details": additional_details,
                "submission_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Save the proposal
            save_proposal(proposal_data, filename='proposals.csv')


            # Show success message
            st.success("Your proposal has been successfully submitted for review.")

            # Clear the form
            st.empty()
        else:
            st.error("Please fill out all required fields.")

# Mostrar propuestas existentes
if st.checkbox("Show existing proposals"):
    try:
        proposals_df = pd.read_csv('proposals_test.csv')
        st.dataframe(proposals_df)
    except FileNotFoundError:
        st.info("No proposals submitted yet.") 