import streamlit as st
import random
import time

st.set_page_config(
    page_title="Mercadito Zapatito",
    page_icon="👟",
    layout="wide"
)

# =========================
# ESTILOS PERSONALIZADOS
# =========================
st.markdown("""
<style>

/* Fondo general */
.stApp {
    background: linear-gradient(
        135deg,
        #f9d423,
        #ff4e50
    );
}

/* Título principal */
h1 {
    text-align: center;
    color: white !important;
    font-size: 60px !important;
    text-shadow: 3px 3px 10px black;
}

/* Subtítulos */
h2, h3 {
    color: white !important;
}

/* Botón */
.stButton > button {
    background-color: #00c853;
    color: white;
    font-size: 22px;
    font-weight: bold;
    border-radius: 15px;
    border: none;
    padding: 10px 25px;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #00e676;
    transform: scale(1.05);
}

/* Tarjetas de métricas */
[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.90);
    border-radius: 15px;
    padding: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

/* Texto general */
p, label {
    color: white !important;
    font-size: 18px;
}

/* Bloques de código */
pre {
    border-radius: 15px !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# ENCABEZADO
# =========================
st.title("👟 MERCADITO ZAPATITO")

st.image(
    "https://images.unsplash.com/photo-1542291026-7eec264c27ff",
    use_container_width=True
)

st.markdown("---")

st.subheader("Sistema de Atención de Clientes")

# =========================
# BOTÓN DE INICIO
# =========================
if st.button("▶ Iniciar Simulación"):

    clientes = [
        "Juanito Pérez",
        "Anita López",
        "Luisito García",
        "Pedrito Ramírez",
        "Lupita Hernández",
        "Carlitos Martínez",
        "Rosita Torres",
        "Dieguito Sánchez",
        "Elenita Flores",
        "Miguelito Vargas"
    ]

    random.shuffle(clientes)

    cola = []

    for i, cliente in enumerate(clientes, start=1):

        cola.append({
            "numero": i,
            "nombre": cliente,
            "zapatitos": random.randint(1, 5)
        })

    historial = []

    total_clientes = len(cola)

    m1, m2, m3 = st.columns(3)

    clientes_restantes = m1.empty()
    clientes_atendidos = m2.empty()
    progreso = m3.empty()

    st.markdown("---")

    col1, col2 = st.columns(2)

    caja_blanco = col1.empty()
    caja_azul = col2.empty()

    st.markdown("---")

    cola_visual = st.empty()
    historial_visual = st.empty()

    barra = st.progress(0)

    turno = 0

    while cola:

        atendidos = len(historial)

        clientes_restantes.metric(
            "Clientes en Espera",
            len(cola)
        )

        clientes_atendidos.metric(
            "Clientes Atendidos",
            atendidos
        )

        progreso.metric(
            "Avance",
            f"{int((atendidos / total_clientes) * 100)}%"
        )

        cola_visual.subheader("🛒 Cola de Clientes")

        cola_texto = ""

        for c in cola:
            cola_texto += (
                f"Cliente #{c['numero']} | "
                f"{c['nombre']} | "
                f"{c['zapatitos']} zapatitos\n"
            )

        cola_visual.code(cola_texto)

        cliente = cola.pop(0)

        if turno % 2 == 0:

            caja_blanco.markdown(f"""
            <div style="
            background:white;
            padding:20px;
            border-radius:20px;
            box-shadow:0 0 15px black;
            color:black;
            ">

            <h4 style="
            color:black !important;
            font-size:24px;
            margin-bottom:15px;
            font-weight:bold;
            ">
            👟 CAJITA ZAPATITO BLANCO
            </h4>

            <div style="
            color:black !important;
            font-size:18px;
            ">
            <b>Cliente #{cliente['numero']}</b><br><br>
            {cliente['nombre']}<br><br>
            Compra: {cliente['zapatitos']} zapatitos
            </div>

            </div>
            """, unsafe_allow_html=True)

        else:

            caja_azul.markdown(f"""
            <div style="
            background:#2196f3;
            color:white;
            padding:20px;
            border-radius:20px;
            box-shadow:0 0 15px black;
            ">
            <h3 style="color:white !important;">
            👟 CAJITA ZAPATITO AZUL
            </h3>

            <p style="color:white !important;">
            <b>Cliente #{cliente['numero']}</b>
            </p>

            <p style="color:white !important;">
            {cliente['nombre']}
            </p>

            <p style="color:white !important;">
            Compra: {cliente['zapatitos']} zapatitos
            </p>

            </div>
            """, unsafe_allow_html=True)

        time.sleep(1)

        historial.append(cliente)

        historial_visual.subheader("📋 Historial")

        historial_texto = ""

        for h in historial:

            historial_texto += (
                f"Cliente #{h['numero']} | "
                f"{h['nombre']} | "
                f"{h['zapatitos']} zapatitos\n"
            )

        historial_visual.code(historial_texto)

        barra.progress(len(historial) / total_clientes)

        turno += 1

    st.balloons()

    st.success(
        "🎉 Todos los clientes fueron atendidos correctamente."
    )