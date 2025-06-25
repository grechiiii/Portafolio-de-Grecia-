import streamlit as st

# Color azul para títulos y textos importantes
azul = "#1E90FF"  # Dodger Blue

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
   <img src="https://i.imgur.com/Noy3lNI.jpg" width="200" style="border-radius: 50%;"></a>""",
   "Email": "a20234861@pucp.edu.pe"
}

endorsements = {
    "img1": "https://i.imgur.com/YQx2CP1.jpeg",
    "img2": "https://i.imgur.com/CmdHRw2.jpeg",
    "img3": "https://i.imgur.com/jakXIXZ.jpeg"
}

# --- Título principal ---
st.markdown(f"<h1 style='color:{azul}; text-align:center;'>Portafolio de {info['Full_Name']}</h1>", unsafe_allow_html=True)

# --- Foto y presentación con columnas ---
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown(info["Photo"], unsafe_allow_html=True)
with col2:
    st.markdown(f"<h3 style='color:{azul};'>{info['Intro']}</h3>", unsafe_allow_html=True)
    st.write(info["About"])

# --- Contacto ---
st.markdown(f"<hr style='border:2px solid {azul};'>", unsafe_allow_html=True)
st.markdown(f"<h2 style='color:{azul};'>📬 Contacto</h2>", unsafe_allow_html=True)
st.write(f"📧 **Email:** {info['Email']}")
st.write(f"📍 **Locación:** {info['City']}")
st.markdown(f"[🔗 LinkedIn]({info['Medium']})")

# --- Galería ---
st.markdown(f"<hr style='border:2px solid {azul};'>", unsafe_allow_html=True)
st.markdown(f"<h2 style='color:{azul};'>📸 Galería</h2>", unsafe_allow_html=True)
st.image([endorsements["img1"], endorsements["img2"], endorsements["img3"]], width=300)

# --- Sobre Grecia ---
st.markdown(f"<hr style='border:2px solid {azul};'>", unsafe_allow_html=True)
st.markdown(f"<h2 style='color:{azul};'>Sobre Grecia</h2>", unsafe_allow_html=True)
st.write("""
Grecia García Hoyos es estudiante de Publicidad en la PUCP, apasionada por la comunicación creativa con impacto social.  
Se destaca por ser productiva, puntual y poseer habilidades de liderazgo y organización.
""")

# --- Experiencia y Metas en dos columnas ---
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<h3 style='color:{azul};'>Experiencia de trabajo</h3>", unsafe_allow_html=True)
    st.write("""
    - Participó en dos voluntariados: uno ambiental en el colegio y otro en CATO como coordinadora de redes sociales de Huellitas PUCP, organización animalista.
    - Fortaleció creatividad, comunicación digital y trabajo en equipo.
    """)
with col2:
    st.markdown(f"<h3 style='color:{azul};'>Metas de carrera</h3>", unsafe_allow_html=True)
    st.write("""
    Grecia busca desarrollarse profesionalmente en comunicación y publicidad,  
    creando proyectos con impacto social que inspiren y conecten con las personas.
    """)

# --- Habilidades y Certificaciones ---
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<h3 style='color:{azul};'>Habilidades</h3>", unsafe_allow_html=True)
    st.write("""
    - Edición de video con CapCut  
    - Diseño gráfico con Canva  
    - Comunicación digital  
    - Liderazgo  
    - Trabajo en equipo  
    - Creatividad  
    - Inglés nivel C1 certificado por PUCP
    """)
with col2:
    st.markdown(f"<h3 style='color:{azul};'>Certificaciones</h3>", unsafe_allow_html=True)
    st.write("Inglés nivel C1 certificado por Idiomas PUCP.")

# --- Logros ---
st.markdown(f"<hr style='border:2px solid {azul};'>", unsafe_allow_html=True)
st.markdown(f"<h2 style='color:{azul};'>🏆 Logros</h2>", unsafe_allow_html=True)
st.write("""
Ganadora del Concurso de Investigación Académica de Estudios Generales Letras 2024-1,  
con monografía publicada en:  
[https://estudios-generales-letras.pucp.edu.pe/investigacion-academica-2024-1-monografias-ganadoras/](https://estudios-generales-letras.pucp.edu.pe/investigacion-academica-2024-1-monografias-ganadoras/)
""")

# --- Línea de tiempo con estilo ---
st.markdown(f"<hr style='border:2px solid {azul};'>", unsafe_allow_html=True)
st.markdown(f"<h2 style='color:{azul}; text-align:center;'>🕒 Mi trayectoria</h2>", unsafe_allow_html=True)

timeline_events = [
    {"year": "2022", "title": "Egresé del colegio", "description": "Terminé mis estudios escolares en el Colegio Cristo Rey."},
    {"year": "2023", "title": "Inicio en CATO", "description": "Comencé a estudiar Publicidad en la PUCP (CATO), siendo primer puesto hasta la fecha."},
    {"year": "2024", "title": "Diseñadora en Huellitas PUCP", "description": "Me uní al voluntariado animalista Huellitas PUCP como diseñadora audiovisual."},
    {"year": "2025", "title": "Coordinadora de Huellitas PUCP", "description": "Asumí el rol de coordinadora de redes sociales en Huellitas PUCP."},
    {"year": "2025", "title": "Ganadora del Concurso de Investigación", "description": "Fui ganadora del concurso de investigación académica de EE.GG.LL. con una monografía publicada en la web oficial."},
]

for event in timeline_events:
    st.markdown(f"<h4 style='color:{azul}; margin-bottom: 2px;'>{event['year']} - {event['title']}</h4>", unsafe_allow_html=True)
    st.write(event["description"])
    st.markdown("<br>", unsafe_allow_html=True)

# --- Footer ---
st.markdown(f"<hr style='border:2px solid {azul};'>", unsafe_allow_html=True)
st.write("Creado con ❤️ usando Streamlit")
