import streamlit as st
import pandas as pd
import re
from io import BytesIO

# Función para extraer datos con expresiones regulares
def extract_by_regex(pattern, data):
    matches = []
    for line in data:
        matches.extend(re.findall(pattern, line))
    return matches

# Función para procesar el texto y generar un archivo XLSX
def process_text(uploaded_file):
    # Leer el archivo como texto
    data = uploaded_file.getvalue().decode("utf-8").splitlines()

    # Patrones de las expresiones regulares
    patterns = {
        "emails": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        "phones": r'\b\d{3}-\d{3}-\d{4}\b',
        "urls": r'https?:\/\/(?:www\.)?[^\s]+',
        "years_experience": r'\b\d+\s+(?:años|años de experiencia)\b',
        "skills": r'\b(?:Python|Django|Machine Learning|SQL|JavaScript|React|AWS|Docker)\b',
    }

    # Extraer los datos utilizando las expresiones regulares
    extracted_data = {key: extract_by_regex(pattern, data) for key, pattern in patterns.items()}

    # Crear un DataFrame de pandas con los datos extraídos
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in extracted_data.items()]))

    # Guardar el DataFrame en un archivo Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="Extracted Data")
    output.seek(0)
    return output

# Interfaz de usuario de Streamlit
def main():
    st.title("Extractor de Información de Currículums")
    st.markdown("### Programada por Angel Mazo")
    st.write(
        """
        Sube un archivo de texto con información relacionada con currículums o perfiles profesionales.
        Esta herramienta extraerá información como:
        - Correos electrónicos.
        - Números de teléfono.
        - URLs.
        - Años de experiencia.
        - Habilidades técnicas específicas.
        """
    )

    uploaded_file = st.file_uploader("Sube un archivo de texto", type="txt")

    if uploaded_file is not None:
        st.write("Archivo cargado con éxito. Procesando...")

        # Procesar el archivo y obtener el archivo Excel generado
        xlsx_file = process_text(uploaded_file)

        # Botón para descargar el archivo XLSX
        st.download_button(
            label="Descargar archivo Excel",
            data=xlsx_file,
            file_name="curriculum_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    main()

