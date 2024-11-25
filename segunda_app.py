import streamlit as st
import re

# Funciones de validación con regex
def validar_nombre(nombre):
    """Valida nombres que comienzan con mayúscula y contienen solo caracteres alfabéticos."""
    patron = r"^[A-Z][a-zA-Z]*$"
    return bool(re.match(patron, nombre))

def validar_email(email):
    """Valida direcciones de correo electrónico."""
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron, email))

def validar_telefono(telefono):
    """Valida números de teléfono en formato internacional o local."""
    patron = r"^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    return bool(re.match(patron, telefono))

def validar_fecha(fecha):
    """Valida fechas en formato 'YYYY-MM-DD'."""
    patron = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(patron, fecha))

# Interfaz de la aplicación
st.title("Validador de Formularios con Expresiones Regulares")
st.markdown("### Programado por Angel Mazo")

# Entrada de datos del usuario
st.header("Formulario de Validación")
nombre = st.text_input("Nombre:")
email = st.text_input("Correo Electrónico:")
telefono = st.text_input("Número de Teléfono:")
fecha = st.text_input("Fecha (formato YYYY-MM-DD):")

# Botón para validar
if st.button("Validar"):
    st.subheader("Resultados de Validación")
    if validar_nombre(nombre):
        st.success("✔️ Nombre válido.")
    else:
        st.error("❌ Nombre inválido. Debe comenzar con una mayúscula y contener solo letras.")

    if validar_email(email):
        st.success("✔️ Correo electrónico válido.")
    else:
        st.error("❌ Correo electrónico inválido. Ejemplo válido: usuario@dominio.com")

    if validar_telefono(telefono):
        st.success("✔️ Número de teléfono válido.")
    else:
        st.error("❌ Número de teléfono inválido. Ejemplo válido: +123-456-7890")

    if validar_fecha(fecha):
        st.success("✔️ Fecha válida.")
    else:
        st.error("❌ Fecha inválida. Debe estar en el formato YYYY-MM-DD.")

# Información adicional
st.info("Los datos ingresados son validados utilizando expresiones regulares.")
