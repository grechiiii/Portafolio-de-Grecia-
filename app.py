import streamlit as st

# CSS personalizado para tonos azules y fondo floral suave
st.markdown(
    """
    <style>
    /* Fondo floral en la parte superior */
    .main > div:first-child {
        background: url('https://www.transparenttextures.com/patterns/flowers.png') repeat;
        background-color: #e3f2fd; /* azul muy claro */
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    
    /* Encabezado principal azul oscuro */
    .stTitle {
        color: #0d47a1 !important; /* azul oscuro */
        font-weight: 700;
    }
    
    /* Subtítulos con iconos y azul medio */
    .subtitle {
        color: #1976d2; /* azul medio */
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.7rem;
    }
    
    /* Texto general */
    .stText {
        color: #0d47a1;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Footer con azul suave */
    footer {
        color: #1565c0 !important;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
   <img src="https://i.imgur.com/Noy3lNI.jpg" width="200" style="border-radius: 20px; border: 3px solid #1976d2;"></a>""",
   "Email": "a20234861@pucp.edu.pe"
}

endorsements = {
    "img1": "https://i.imgur.com/YQx2CP1.jpeg",
    "img2": "https://i.imgur.com/CmdHRw2.jpeg",
    "img3": "https://i.imgur.com/jakXIXZ.jpeg"
}

# Título con clase para aplicar CSS
st.markdown(f'<h1 class="stTitle">Portafolio de {info["Full_Name"]}</h1>', unsafe_allow_html=True)

# Foto y presentación
st.markdown(info["Photo"], unsafe_allow_html=True)
st.subheader(info["Intro"])
st.write(info["About"])

# Contacto con icono
st.markdown('<h3 class="subtitle">📬 Contacto</h3>', unsafe_allow_html=True)
st.write(f"📧 {info['Email']}")
st.write(f"📍 {info['City']}")
st.markdown(f"[🔗 LinkedIn]({info['Medium']})")

# Galería con icono
st.markdown('<h3 class="subtitle">📸 Galería</h3>', unsafe_allow_html=True)
st.image([endorsements["img1"], endorsements["img2"], endorsements["img3"]], width=300)

# Footer opcional
st.markdown("---")
st.write('<p style="color:#1565c0; font-weight: 500;">Creado con ❤️ usando Streamlit</p>', unsafe_allow_html=True)
