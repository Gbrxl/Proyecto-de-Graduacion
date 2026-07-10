from flask import Flask, render_template

app = Flask(__name__)

retos = [
    {"dia": 1,  "icono": "💡", "texto": "Apaga las luces que no uses."},
    {"dia": 2,  "icono": "🚰", "texto": "Cierra la llave al cepillarte."},
    {"dia": 3,  "icono": "🧹", "texto": "Recoge basura de una zona cercana."},
    {"dia": 4,  "icono": "🚲", "texto": "Camina o usa bicicleta hoy."},
    {"dia": 5,  "icono": "♻️", "texto": "Separa los residuos reciclables."},
    {"dia": 6,  "icono": "🚿", "texto": "Dúchate en menos de 5 minutos."},
    {"dia": 7,  "icono": "🛍️", "texto": "No uses bolsas plásticas hoy."},
    {"dia": 8,  "icono": "🌱", "texto": "Planta una semilla o cuida una planta."},
    {"dia": 9,  "icono": "🔌", "texto": "Desconecta cargadores sin uso."},
    {"dia": 10, "icono": "🫙", "texto": "Reutiliza un frasco o envase."},
    {"dia": 11, "icono": "🛒", "texto": "Evita comprar algo innecesario."},
    {"dia": 12, "icono": "👜", "texto": "Lleva tu bolsa al mercado."},
    {"dia": 13, "icono": "📄", "texto": "Reduce el uso de papel hoy."},
    {"dia": 14, "icono": "🪴", "texto": "Haz compost con residuos orgánicos."},
    {"dia": 15, "icono": "💬", "texto": "Comparte un consejo ambiental."},
    {"dia": 16, "icono": "🌳", "texto": "Limpia una zona verde cercana."},
    {"dia": 17, "icono": "🍎", "texto": "Consume productos locales hoy."},
    {"dia": 18, "icono": "🥤", "texto": "Evita pitillos o cubiertos plásticos."},
    {"dia": 19, "icono": "🔧", "texto": "Repara algo antes de botarlo."},
    {"dia": 20, "icono": "🍽️", "texto": "Ahorra agua al lavar los platos."},
    {"dia": 21, "icono": "🚌", "texto": "Usa transporte público hoy."},
    {"dia": 22, "icono": "👕", "texto": "Dona ropa que ya no uses."},
    {"dia": 23, "icono": "🍲", "texto": "Haz una comida sin desperdiciar."},
    {"dia": 24, "icono": "🪴", "texto": "Crea una maceta con envase reciclado."},
    {"dia": 25, "icono": "🌿", "texto": "Cuida una planta durante el día."},
    {"dia": 26, "icono": "🖨️", "texto": "Evita imprimir documentos hoy."},
    {"dia": 27, "icono": "📚", "texto": "Aprende sobre el cambio climático."},
    {"dia": 28, "icono": "🗑️", "texto": "Clasifica los residuos en casa."},
    {"dia": 29, "icono": "⚡", "texto": "Reduce el consumo de energía."},
    {"dia": 30, "icono": "🤝", "texto": "Invita a alguien a un reto ecológico."},
]

datos_eco = [
    {
        "titulo": "Temperatura global",
        "valor": "+1.1°C sobre nivel preindustrial",
        "icono": "🌡️",
        "desc": "La temperatura promedio global ha subido "
                "más de 1 grado desde la era industrial."
    },
    {
        "titulo": "Calidad del aire",
        "valor": "7 millones de muertes/año",
        "icono": "💨",
        "desc": "La contaminación del aire causa millones "
                "de muertes prematuras cada año en el mundo."
    },
    {
        "titulo": "CO₂ en la atmósfera",
        "valor": "422 ppm",
        "icono": "🏭",
        "desc": "El nivel de CO₂ es el más alto en "
                "800,000 años de historia del planeta."
    },
    {
        "titulo": "Deforestación",
        "valor": "10 millones de ha/año",
        "icono": "🌳",
        "desc": "Se pierden millones de hectáreas de bosque "
                "cada año por actividad humana."
    },
    {
        "titulo": "Nivel del mar",
        "valor": "+3.7 mm/año",
        "icono": "🌊",
        "desc": "El nivel del mar sube cada año por el "
                "derretimiento de glaciares y hielos polares."
    },
    {
        "titulo": "Especies amenazadas",
        "valor": "40,000+ especies",
        "icono": "🦋",
        "desc": "Más de 40,000 especies están en peligro "
                "de extinción según la Lista Roja de la UICN."
    },
]

estadisticas = [
    {"numero": "1.1°C", "label": "Aumento temperatura global"},
    {"numero": "422",   "label": "PPM de CO₂ en la atmósfera"},
    {"numero": "30",    "label": "Retos para cambiar hábitos"},
    {"numero": "10M",   "label": "Hectáreas de bosque perdidas/año"},
]


def get_nivel(retos_completados):
    if retos_completados == 30:
        return "EcoLeyenda", "nivel-leyenda"
    elif retos_completados >= 25:
        return "EcoHéroe", "nivel-heroe"
    elif retos_completados >= 18:
        return "EcoGuardián", "nivel-guardian"
    elif retos_completados >= 10:
        return "EcoAprendiz", "nivel-aprendiz"
    else:
        return "EcoIniciado", "nivel-iniciado"


ranking_raw = [
    {"nombre": "Sofía Martínez",  "avatar": "🌸", "retos_completados": 30},
    {"nombre": "Carlos Rivera",   "avatar": "🦁", "retos_completados": 28},
    {"nombre": "Valentina Cruz",  "avatar": "🌺", "retos_completados": 26},
    {"nombre": "Andrés López",    "avatar": "🐢", "retos_completados": 24},
    {"nombre": "Isabella Torres", "avatar": "🦋", "retos_completados": 22},
    {"nombre": "Diego Ramírez",   "avatar": "🌵", "retos_completados": 19},
    {"nombre": "Camila Herrera",  "avatar": "🐝", "retos_completados": 16},
    {"nombre": "Mateo Gómez",     "avatar": "🌊", "retos_completados": 13},
    {"nombre": "Lucía Fernández", "avatar": "🍃", "retos_completados": 9},
    {"nombre": "Sebastián Díaz",  "avatar": "🌻", "retos_completados": 5},
]

ranking_data = []
for p in ranking_raw:
    nivel, nivel_css = get_nivel(p["retos_completados"])
    porcentaje = round((p["retos_completados"] / 30) * 100)
    ranking_data.append({
        **p,
        "porcentaje": porcentaje,
        "nivel": nivel,
        "nivel_css": nivel_css,
    })


@app.route("/")
def inicio():
    return render_template(
        "inicio.html",
        estadisticas=estadisticas
    )


@app.route("/retos")
def retos_page():
    return render_template("retos.html", retos=retos)


@app.route("/datos")
def datos_page():
    return render_template("datos.html", datos=datos_eco)


@app.route("/ranking")
def ranking_page():
    return render_template(
        "ranking.html",
        ranking=ranking_data
    )


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


if __name__ == "__main__":
    app.run(debug=True)