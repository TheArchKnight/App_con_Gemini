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

# Función para procesar el archivo y generar un archivo XLSX
def process_file(uploaded_file):
    # Leer el archivo CSV
    data = uploaded_file.getvalue().decode("utf-8").splitlines()

    # Patrones de las expresiones regulares
    patterns = {
        "emails": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        "dates": r'\b(?:[1-9]|0[1-9]|1[0-9]|2[0-9]|3[01])/(?:[1-9]|0[1-9]|1[012])/(?:19|20)\d{2}\b',
        "urls": r'https?:\/\/(?:www\.)?[^\s]+',
        "ips": r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
        "phones": r'\b\d{3}-\d{3}-\d{4}\b',
        "hashtags": r'\B#\w+\b',
        "mentions": r'@\w+',
        "uppercase_words": r'\b[A-Z]{2,}\b',  # Palabras en mayúsculas (mínimo 2 letras)
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
    st.title("Procesamiento de Datos con Regex")
    st.markdown("### Programada por Angel Mazo")

    st.write("Sube un archivo CSV para extraer información como emails, fechas, IPs, teléfonos, palabras en mayúsculas, etc.")

    uploaded_file = st.file_uploader("Selecciona un archivo CSV", type="csv")

    if uploaded_file is not None:
        st.write("Archivo cargado con éxito. Procesando...")

        # Procesar el archivo y obtener el archivo Excel generado
        xlsx_file = process_file(uploaded_file)

        # Botón para descargar el archivo XLSX
        st.download_button(
            label="Descargar archivo Excel",
            data=xlsx_file,
            file_name="datos_extraidos.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    main()
