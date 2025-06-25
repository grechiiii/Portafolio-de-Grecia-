import streamlit as st

# Definimos una paleta de azules y celestes
azul_oscuro = "#0D47A1"
azul_medio = "#1976D2"
azul_claro = "#42A5F5"
celeste = "#90CAF9"
celeste_suave = "#E3F2FD"

# CSS para diseño moderno con degradados, bordes, sombras y fondo floral sutil
st.markdown(
    f"""
    <style>
    /* Fondo floral suave en la cabecera */
    .cabecera {{
        background: linear-gradient(135deg, {celeste_suave} 0%, {celeste} 100%);
        background-image: url('https://www.transparenttextures.com/patterns/flowers.png');
        background-repeat: repeat;
        border-radius: 15px;
        padding: 2.5rem 2rem;
        margin-bottom: 2.5rem;
        box-shadow: 0 8px 15px rgba(25, 118, 210, 0.3);
        text-align: center;
    }}

    /* Título principal con degradado y sombra */
    .titulo-principal {{
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(90deg, {azul_oscuro}, {azul_medio});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }}

    /* Foto con borde celeste y sombra */
    .foto-perfil {{
        border-radius: 50%;
        border: 5px solid {celeste};
        box-shadow: 0 4px 12px rgba(25, 118, 210, 0.4);
        max-width: 220px;
        margin: 0 auto 1rem auto;
        display: block;
    }}

    /* Subtítulos con iconos y color */
    h2 {{
        color: {azul_medio};
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid {celeste};
        padding-bottom: 0.25rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}

    /* Contenedor de secciones con sombra y fondo blanco */
    .seccion {{
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(25, 118, 210, 0.1);
        padding: 1.5rem 2rem;
        margin-bottom: 2rem;
    }}

    /* Texto de parrafos */
    p, li {{
        color: {azul_oscuro};
        font-size: 1.1rem;
        line-height: 1.5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}

    /* Footer estilizado */
    footer {{
        text-align: center;
        color: {azul_medio} !important;
        margin-top: 3rem;
        font-weight: 600;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}

    /* Imágenes galería con borde y sombra */
    .galeria img {{
        border-radius: 12px;
        box-shadow: 0 6px 15px rgba(25, 118, 210, 0.2);
        margin-right: 15px;
        margin-bottom: 15px;
        max-width: 300px;
        transition: transform 0.3s ease;
    }}

    .galeria img:hover {{
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(25, 118, 210, 0.4);
    }}

    /* Timeline eventos */
    .evento-timeline {{
        border-left: 4px solid {azul_medio};
        padding-left: 1rem;
        margin-bottom: 1.2rem;
    }}

    .evento-timeline h4 {{
        margin-bottom: 0.2rem;
        color: {azul_oscuro};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Información personal
info = {
    "Full_Name": "Grecia García Hoyos",
    "Intro": "Estudiante de Publicidad y apasionada por la comunicación creativa con impacto social",
    "About": """Hola, soy Grecia García Hoyos, estudiante de Publicidad en la PUCP. Me destaco por ser una persona productiva, puntual y con habilidades de liderazgo y organización. 
Siempre busco aprender, colaborar y crear impacto desde la comunicación.""",
    "Medium": "https://www.linkedin.com/in/grecia-garcia-hoyos-44997933a/",
    "City": "Lima, Perú",
    "Photo": "https://i.imgur.com/Noy3lNI.jpg",
    "Email": "a20234861@pucp.edu.pe"
}

endorsements = {
    "img1": "https://i.imgur.com/YQx2CP1.jpeg",
    "img2": "https://i.imgur.com/CmdHRw2.jpeg",
    "img3": "https://i.imgur.com/jakXIXZ.jpeg"
}

# Cabecera con fondo floral y título
st.markdown(f'<div class="cabecera">', unsafe_allow_html=True)
st.markdown(f'<img src="{info["Photo"]}" alt="Foto de perfil" class="foto-perfil">', unsafe_allow_html=True)
st.markdown(f'<h1 class="titulo-principal">Portafolio de {info["Full_Name"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<h3 style="color:{azul_oscuro}; margin-top:0;">{info["Intro"]}</h3>', unsafe_allow_html=True)
st.markdown(f'<p style="max-width:700px; margin: 0 auto;">{info["About"]}</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Sección Contacto
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('📬 <h2>Contacto</h2>', unsafe_allow_html=True)
st.markdown(f'<p>📧 <b>Email:</b> {info["Email"]}</p>', unsafe_allow_html=True)
st.markdown(f'<p>📍 <b>Locación:</b> {info["City"]}</p>', unsafe_allow_html=True)
st.markdown(f'<p>🔗 <a href="{info["Medium"]}" target="_blank">LinkedIn</a></p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Galería
st.markdown('<div class="seccion galeria">', unsafe_allow_html=True)
st.markdown('📸 <h2>Galería</h2>', unsafe_allow_html=True)
st.image([endorsements["img1"], endorsements["img2"], endorsements["img3"]], width=300)
st.markdown('</div>', unsafe_allow_html=True)

# Sobre Grecia
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('🌟 <h2>Sobre Grecia</h2>', unsafe_allow_html=True)
st.markdown(f'<p>Grecia García Hoyos es estudiante de Publicidad en la PUCP, apasionada por la comunicación creativa con impacto social. Se destaca por ser productiva, puntual y poseer habilidades de liderazgo y organización.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Experiencia y Metas en columnas
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('💼 <h2>Experiencia de trabajo</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul>
    <li>Participó en dos voluntariados: uno ambiental en el colegio y otro en CATO como coordinadora de redes sociales de Huellitas PUCP, organización animalista.</li>
    <li>Fortaleció creatividad, comunicación digital y trabajo en equipo.</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('🎯 <h2>Metas de carrera</h2>', unsafe_allow_html=True)
    st.markdown("""
    <p>Grecia busca desarrollarse profesionalmente en comunicación y publicidad, creando proyectos con impacto social que inspiren y conecten con las personas.</p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Habilidades y Certificaciones en columnas
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('🛠️ <h2>Habilidades</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul>
    <li>Edición de video con CapCut</li>
    <li>Diseño gráfico con Canva</li>
    <li>Comunicación digital</li>
    <li>Liderazgo</li>
    <li>Trabajo en equipo</li>
    <li>Creatividad</li>
    <li>Inglés nivel C1 certificado por PUCP</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('📜 <h2>Certificaciones</h2>', unsafe_allow_html=True)
    st.markdown('<p>Inglés nivel C1 certificado por Idiomas PUCP.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Logros
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('🏆 <h2>Logros</h2>', unsafe_allow_html=True)
st.markdown("""
<p>Ganadora del Concurso de Investigación Académica de Estudios Generales Letras 2024-1, con monografía publicada en:
<a href="https://estudios-generales-letras.pucp.edu.pe/investigacion-academica-2024-1-monografias-ganadoras/" target="_blank">
https://estudios-generales-letras.pucp.edu.pe/investigacion-academica-2024-1-monografias-ganadoras/
</a>
</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Línea de tiempo con estilo
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('🕒 <h2>Mi trayectoria</h2>', unsafe_allow_html=True)

timeline_events = [
    {"year": "2022", "title": "Egresé del colegio", "description": "Terminé mis estudios escolares en el Colegio Cristo Rey."},
    {"year": "2023", "title": "Inicio en CATO", "description": "Comencé a estudiar Publicidad en la PUCP (CATO), siendo primer puesto hasta la fecha."},
    {"year": "2024", "title": "Diseñadora en Huellitas PUCP", "description": "Me uní al voluntariado animalista Huellitas PUCP como diseñadora audiovisual."},
    {"year": "2025", "title": "Coordinadora de Huellitas PUCP", "description": "Asumí el rol de coordinadora de redes sociales en Huellitas PUCP."},
    {"year": "2025", "title": "Ganadora del Concurso de Investigación", "description": "Fui ganadora del concurso de investigación académica de EE.GG.LL. con una monografía publicada en la web oficial."},
]

for event in timeline_events:
    st.markdown(f'''
        <div class="evento-timeline">
            <h4>{event["year"]} - {event["title"]}</h4>
            <p>{event["description"]}</p>
        </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer estilizado
st.markdown('<footer>Creado con ❤️ usando Streamlit</footer>', unsafe_allow_html=True)
