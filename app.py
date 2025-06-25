import streamlit as st

# Tu información personal
info = {
   "Pronoun": "ella", 
   "Name": "Grecia",
   "Full_Name": "Grecia García Hoyos",
   "Intro": "Estudiante de Publicidad y apasionada por la comunicación creativa con impacto social",
   "About": """Hola, soy Grecia García Hoyos, estudiante de Publicidad en la PUCP. Me destaco por ser una persona productiva, puntual y con habilidades de liderazgo y organización. 
Siempre busco aprender, colaborar y crear impacto desde la comunicación.""",
   "Tableau": "",
   "Medium": "https://www.linkedin.com/in/grecia-garcia-hoyos-44997933a/",
   "City": "Lima, Perú",
"Photo": """<a href="https://www.linkedin.com/in/grecia-garcia-hoyos-44997933a/">
<img src="https://i.imgur.com/Noy3lNI.jpg" width="200"></a>"""
   "Email": "a20234861@pucp.edu.pe"
}

endorsements = {
    "img1": "https://i.imgur.com/YQx2CP1.jpeg",
    "img2": "https://i.imgur.com/CmdHRw2.jpeg",
    "img3": "https://i.imgur.com/jakXIXZ.jpeg"
}

# Título
st.title(f"Portafolio de {info['Full_Name']}")

# Foto y presentación
st.markdown(info["Photo"], unsafe_allow_html=True)
st.subheader(info["Intro"])
st.write(info["About"])

# Contacto
st.markdown("### 📬 Contacto")
st.write(f"📧 {info['Email']}")
st.write(f"📍 {info['City']}")
st.markdown(f"[🔗 LinkedIn]({info['Medium']})")

# Galería (Endorsements)
st.markdown("### 📸 Galería")
st.image([endorsements["img1"], endorsements["img2"], endorsements["img3"]], width=300)

# Footer opcional
st.markdown("---")
st.write("Creado con ❤️ usando Streamlit")

endorsements = {
    "img1": "https://i.imgur.com/YQx2CP1.jpeg",
    "img2": "https://i.imgur.com/CmdHRw2.jpeg",
    "img3": "https://i.imgur.com/jakXIXZ.jpeg"
}
