import streamlit as st
import re


def mostrar_sugerencias(sugerencias):
    lista = ""
    for sugerencia in sugerencias:
        lista += "- " + sugerencia + "\n"
    st.markdown(lista)


def evaluar_contrasena(password):
    # Expresión regular para validar una contraseña fuerte
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%#*?&])[A-Za-z\d@$!%#*?&]{8,}$"

    if re.search(regex, password):
        st.write("La contraseña es muy fuerte!")
    else:
        sugerencias = []
        if len(password) < 8:
            sugerencias.append("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r"[a-z]", password):
            sugerencias.append("La contraseña debe incluir al menos una letra minúscula.")
        if not re.search(r"[A-Z]", password):
            sugerencias.append("La contraseña debe de incluir al menos una letra mayuscula")
        if not re.search(r"(?=.*\d)", password):
            sugerencias.append("La contraseña debe de tener al menos un numero")
        if not re.search(r"(?=.*[@$!%#*?&])", password):
            sugerencias.append("La contraseña debe de tener al menos un caracter especial")
        mostrar_sugerencias(sugerencias)


def main():
    st.title("Evaluador de Contraseñas")
    st.markdown("### Programado por Angel Mazo")
    password = st.text_input("Ingrese su contraseña")

    if st.button("Evaluar"):
        evaluar_contrasena(password)


if __name__ == "__main__":
    main()
