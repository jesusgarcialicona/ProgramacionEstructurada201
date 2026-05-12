#!/usr/bin/env python3
"""
========================================================
  APOYO ESTUDIANTIL — Calidad de vida en secundaria
  Orientación para adolescentes — Sin internet requerido
========================================================
"""

import os
import sys
import textwrap
import random
from datetime import datetime

# ── Colores ANSI ─────────────────────────────────────
R   = "\033[0m"
B   = "\033[1m"
C   = "\033[36m"
G   = "\033[32m"
Y   = "\033[33m"
M   = "\033[35m"
RE  = "\033[31m"
BL  = "\033[34m"
DIM = "\033[2m"

WIDTH = 70

# ── Perfil del estudiante ─────────────────────────────
perfil = {
    "grado": "",
    "economia": "",
    "familia": "",
    "internet": "",
    "preocupaciones": []
}

# ═══════════════════════════════════════════════════════
#  BASE DE CONSEJOS
# ═══════════════════════════════════════════════════════

CONSEJOS = {
    "adicciones": {
        "general": [
            "Las adicciones no son debilidad — son un proceso que le puede pasar a cualquiera. Conocerlas es la mejor prevención.",
            "• El alcohol, cigarro, vaping y drogas afectan especialmente el cerebro adolescente, que todavía se desarrolla hasta los 25 años.",
            "• Si alguien te ofrece algo y no quieres, puedes decir: 'No gracias, no es lo mío' sin dar más explicaciones.",
            "• Si un amigo tiene un problema, no es tu responsabilidad resolverlo, pero sí puedes orientarle a pedir ayuda.",
            "• CIJ (Centros de Integración Juvenil): orientación gratuita y confidencial. Busca el más cercano en cij.gob.mx",
            "• Línea CONADIC (gratuita y anónima): 800 911-2000, disponible 24 horas.",
        ],
        "muy_limitada": [
            "• El estrés por falta de dinero puede llevar a buscar 'escapar' con sustancias. Es comprensible, pero existen otras salidas.",
            "• Hablar con tu orientador escolar es completamente gratuito y confidencial.",
        ],
        "limitada": [
            "• Si el ambiente en casa es difícil, hablar con el orientador de tu escuela puede ayudarte sin costo.",
        ],
    },
    "redes_sociales": {
        "general": [
            "Las redes sociales no son malas por sí solas — el problema es cuando afectan el sueño, la escuela o tus relaciones reales.",
            "• Señales de uso problemático: revisar el celular al despertar, sentirte mal sin señal, compararte constantemente con otros.",
            "• Activa el temporizador de pantalla en tu celular — la mayoría de los celulares lo tienen en Configuración.",
            "• Lo que ves en redes es una versión editada de la vida de otros. Nadie publica sus días malos.",
            "• Si alguien te acosa por redes (cyberbullying): guarda capturas, bloquéalo y cuéntaselo a un adulto de confianza.",
            "• Intenta tener al menos 1 hora sin pantallas antes de dormir — mejora mucho el descanso.",
        ],
        "sin_internet": [
            "• No tener redes sociales constantes puede ser una ventaja: menos comparaciones y más tiempo para ti.",
        ],
        "con_internet": [
            "• Desactiva las notificaciones de apps que no sean urgentes — cada notificación interrumpe tu concentración.",
            "• Usa el modo 'no molestar' mientras estudias o intentas dormir.",
        ],
    },
    "economia": {
        "muy_limitada": [
            "Vivir con recursos muy limitados es difícil, y es válido que eso te pese. Aquí van opciones concretas:",
            "• Beca Benito Juárez: apoyo económico mensual para estudiantes de secundaria. Pregunta en tu escuela si estás registrado.",
            "• Desayunos DIF: muchas escuelas tienen este programa. Pregunta a tu orientador o directora.",
            "• LICONSA: leche subsidiada para familias de bajos recursos. Busca la lechería más cercana.",
            "• Para comer mejor con poco: frijoles, arroz, avena, huevo y tortilla son muy nutritivos y económicos.",
            "• Si hay días que no puedes comer, cuéntaselo a tu orientador o un maestro de confianza. Hay apoyos.",
        ],
        "limitada": [
            "• La Beca Benito Juárez da apoyo mensual a estudiantes de secundaria. Pregunta en tu escuela.",
            "• Para estudiar sin costo: Khan Academy en español (khanacademy.org/es) tiene todas las materias.",
        ],
        "media": [
            "• Khan Academy en español es completamente gratuita para reforzar cualquier materia.",
        ],
        "sin_internet": [
            "• Sin internet, la biblioteca de tu escuela o la pública más cercana son recursos valiosos y gratuitos.",
            "• Pedir apoyo a compañeros para estudiar en equipo no cuesta nada y es muy efectivo.",
        ],
    },
    "bullying": {
        "general": [
            "El bullying no es normal ni debes aguantarlo. Nadie merece ser maltratado.",
            "• No estás solo. Esto tiene solución con el apoyo correcto.",
            "• Cuéntaselo a un adulto de confianza: familiar, maestro, orientador o prefecto. No es 'chismear' — es protegerte.",
            "• Guarda evidencia: si hay mensajes o fotos, toma capturas de pantalla con fecha.",
            "• Evita confrontar solo al agresor — es más seguro actuar con apoyo de adultos.",
            "• Tu orientador escolar está obligado a actuar ante casos de bullying. Puedes pedir confidencialidad.",
            "• SAPTEL: 55 5259-8121 — puedes llamar si necesitas hablar de forma anónima.",
        ],
    },
    "salud_mental": {
        "general": [
            "Cuidar tu salud mental es igual de importante que cuidar tu salud física.",
            "• Es normal sentir ansiedad, tristeza o estrés a veces. No significa que estés 'loco/a'.",
            "• Señales de que algo necesita atención: tristeza que dura más de 2 semanas, no poder dormir, dejar de hacer cosas que antes disfrutabas.",
            "• Si tienes pensamientos de hacerte daño, llama a SAPTEL ahora: 55 5259-8121. Es gratis, anónimo y 24/7.",
            "• Técnica de respiración para la ansiedad: inhala 4 segundos, mantén 4, exhala 4. Repite 5 veces.",
            "• Tu orientador escolar puede canalizarte a atención psicológica gratuita si lo necesitas.",
        ],
        "muy_limitada": [
            "• El estrés económico afecta la salud mental. No es tu culpa y no tienes que cargarlo solo.",
            "• El orientador de tu escuela puede ayudarte sin costo y de forma confidencial.",
        ],
    },
    "presion_de_grupo": {
        "general": [
            "La presión de grupo es muy real en la secundaria. Aquí van estrategias concretas:",
            "• Frase que funciona: 'No gracias, no quiero' — no necesitas dar explicaciones.",
            "• Si insisten: 'Ya les dije que no. Si siguen, me voy.'",
            "• Los amigos de verdad respetan tu decisión sin presionarte.",
            "• Practica decir 'no' en casa frente al espejo — suena raro pero funciona para ganar seguridad.",
            "• Si el grupo te incomoda constantemente, busca otros espacios: clubes, deporte, grupos de interés en la escuela.",
        ],
    },
    "estres_escolar": {
        "general": [
            "El estrés escolar es muy común pero tiene solución con las estrategias correctas.",
            "• Organiza tus tareas por urgencia: ¿qué entrego mañana? ¿qué es para después? Empieza por lo urgente.",
            "• Estudia en bloques de 25 minutos con 5 de descanso (técnica Pomodoro) — es más efectivo que horas seguidas.",
            "• Si no entiendes algo, pregunta al maestro después de clase. La mayoría agradece el interés.",
            "• Dormir bien es parte de estudiar: sin descanso el cerebro no retiene información.",
        ],
        "sin_internet": [
            "• Sin internet, aprovecha la biblioteca de tu escuela o la pública más cercana.",
            "• Estudiar en equipo con compañeros no cuesta nada y ayuda mucho.",
        ],
        "con_internet": [
            "• YouTube tiene explicaciones gratuitas de prácticamente cualquier tema de secundaria.",
            "• Khan Academy en español (khanacademy.org/es) tiene ejercicios con retroalimentación inmediata.",
        ],
    },
    "familia": {
        "general": [
            "Los problemas familiares son de los más difíciles de cargar, especialmente en la escuela.",
            "• No eres responsable de resolver los problemas de los adultos en tu casa.",
            "• Busca un espacio propio aunque sea pequeño donde puedas descansar mentalmente.",
            "• Hablar con tu orientador escolar es confidencial y puede ayudarte a manejar la situación.",
            "• Si hay violencia en casa, puedes llamar a SAPTEL (55 5259-8121) para orientación.",
        ],
        "madre": [
            "• Vivir solo con tu mamá puede tener presiones económicas y emocionales extras. Es válido que te afecte.",
        ],
        "padre": [
            "• Vivir solo con tu papá tiene sus propios retos. No dudes en buscar apoyo externo si lo necesitas.",
        ],
        "abuelos": [
            "• Vivir con abuelos u otros familiares puede generar sus propias tensiones. Tu orientador puede ayudarte.",
        ],
    },
    "soledad": {
        "general": [
            "Sentirse solo es una de las cosas más difíciles, y muchos estudiantes lo sienten aunque no lo digan.",
            "• La soledad no significa que algo esté mal contigo — muchas veces es situacional y cambia.",
            "• Los clubes y actividades extracurriculares son los mejores lugares para hacer amistades porque ya tienen algo en común.",
            "• Empieza pequeño: un 'hola' o un comentario en clase puede ser el inicio de una amistad.",
            "• Tener pocos amigos pero de calidad es mejor que muchos conocidos superficiales.",
            "• Si la soledad es profunda o prolongada, habla con tu orientador — puede ayudarte.",
        ],
    },
    "identidad": {
        "general": [
            "La adolescencia es el momento con más preguntas sobre quién eres — es completamente normal.",
            "• Tu identidad no tiene que estar definida ahora. Tienes tiempo para explorar qué te gusta y cómo eres.",
            "• La autoestima se construye con acciones pequeñas: cumplir lo que te propones, aprender algo nuevo.",
            "• No tienes que ser como todos los demás. Ser diferente no está mal.",
            "• Si sientes confusión sobre tu identidad, es válido explorar eso a tu ritmo, sin prisa.",
            "• Hablar con un adulto de confianza o tu orientador puede ayudarte a procesar estas preguntas.",
        ],
    },
}

FRASES_ALIENTO = [
    "Recuerda: pedir ayuda es una señal de fortaleza, no de debilidad. 💙",
    "Estás en una etapa difícil pero también increíble. Confía en ti. 💪",
    "No tienes que resolverlo todo solo/a. Hay personas dispuestas a apoyarte.",
    "Cada día es una oportunidad de estar un poco mejor que ayer.",
    "Mereces estar bien. No te conformes con menos.",
    "Lo que sientes es válido. Y también tiene solución.",
]

ESTADOS_ANIMO = {
    "1": ("😔", "Muy mal"),
    "2": ("😕", "Mal"),
    "3": ("😐", "Regular"),
    "4": ("🙂", "Bien"),
    "5": ("😄", "Muy bien"),
}

CONSEJOS_ESTADO = {
    "1": [
        "Que estés muy mal hoy no significa que siempre vas a estar así. Los días difíciles pasan.",
        "• Haz una sola cosa pequeña por ti hoy: tomar agua, salir 10 minutos al sol, escuchar música que te guste.",
        "• Si sientes que no puedes más, llama a SAPTEL: 55 5259-8121. Es gratis y anónimo.",
        "• No tienes que fingir que estás bien. Busca a alguien de confianza y cuéntale cómo te sientes.",
    ],
    "2": [
        "Está bien no estar bien. Lo importante es no quedarse solo con eso.",
        "• Intenta identificar qué está causando que te sientas mal — a veces nombrarlo ayuda.",
        "• Una caminata corta puede cambiar un poco el estado de ánimo.",
        "• Si llevas varios días sintiéndote mal, considera hablar con tu orientador escolar.",
    ],
    "3": [
        "Regular es válido. No todos los días tienen que ser extraordinarios.",
        "• Haz algo que normalmente disfrutas, aunque sea por 20 minutos.",
        "• Tomar agua, comer algo y dormir bien pueden mejorar más de lo que crees.",
    ],
    "4": [
        "Qué bueno que estés bien. Aprovecha esa energía.",
        "• Es buen momento para avanzar algo pendiente de la escuela.",
        "• Anota qué contribuyó a que te sintieras bien hoy — te puede ayudar en días difíciles.",
    ],
    "5": [
        "¡Excelente! Los días buenos son para disfrutarlos.",
        "• Comparte esa energía positiva con alguien — un mensaje, una ayuda, una palabra amable.",
        "• Recuerda este día cuando vengan los difíciles. Puedes volver a estar así.",
    ],
}

RECURSOS = [
    ("🆘 SAPTEL — Crisis 24/7",        "📞 55 5259-8121",           "Apoyo emocional, adicciones y crisis. Gratuito y anónimo.",    ["GRATIS","ANÓNIMO","24/7"], RE),
    ("💊 CONADIC — Línea de la Vida",  "📞 800 911-2000",           "Orientación sobre adicciones y salud mental.",                   ["GRATIS","ANÓNIMO","24/7"], RE),
    ("🏥 CIJ",                         "🌐 cij.gob.mx",             "Prevención y tratamiento de adicciones para jóvenes.",          ["GRATIS","PRESENCIAL"],    BL),
    ("🏫 Orientador de tu escuela",    "📍 En tu plantel",          "Apoyo confidencial en adicciones, familia y bullying.",         ["GRATIS","CONF."],         G),
    ("🏛 IMSS — Salud mental",         "🏥 Clínica IMSS cercana",   "Orientación psicológica si tienes acceso al IMSS.",             ["CON IMSS"],               M),
    ("🍽 DIF — Desayunos escolares",   "📍 Tu escuela/delegación",  "Desayunos y apoyos para estudiantes de bajos recursos.",        ["SUBSIDIO GOB."],          Y),
    ("🥛 LICONSA",                     "🌐 liconsa.gob.mx",         "Leche a precio de apoyo para familias con bajos recursos.",     ["SUBSIDIO GOB."],          Y),
    ("📚 Beca Benito Juárez",          "📍 Pregunta en tu escuela", "Apoyo económico mensual para estudiantes de secundaria.",       ["SUBSIDIO GOB."],          Y),
    ("📺 Aprende en Casa / Canal Once","📺 TV / YouTube SEP",        "Contenido educativo gratuito para todas las materias.",         ["GRATIS"],                 C),
    ("📖 Khan Academy",                "🌐 khanacademy.org/es",      "Clases gratuitas de todas las materias de secundaria.",         ["GRATIS","ONLINE"],        C),
]

MAPA_TEMAS = {
    "1":  ("Estrés escolar",        "estres_escolar",   Y),
    "2":  ("Redes sociales",        "redes_sociales",   M),
    "3":  ("Adicciones",            "adicciones",       RE),
    "4":  ("Bullying",              "bullying",         C),
    "5":  ("Salud mental",          "salud_mental",     BL),
    "6":  ("Presión de grupo",      "presion_de_grupo", G),
    "7":  ("Problemas económicos",  "economia",         Y),
    "8":  ("Problemas familiares",  "familia",          M),
    "9":  ("Soledad",               "soledad",          BL),
    "10": ("Identidad/autoestima",  "identidad",        G),
}

# ═══════════════════════════════════════════════════════
#  UTILIDADES
# ═══════════════════════════════════════════════════════

def limpiar():
    os.system("clear" if os.name != "nt" else "cls")

def linea(char="─", color=C):
    print(f"{color}{char * WIDTH}{R}")

def centrar(texto, color=""):
    print(f"{color}{texto.center(WIDTH)}{R}")

def cabecera():
    limpiar()
    linea("═", C)
    centrar(f"{B}{C}💙  APOYO ESTUDIANTIL  💙{R}", "")
    centrar("Calidad de vida para estudiantes de secundaria", DIM)
    linea("═", C)
    print()

def menu_opcion(num, texto, icono="▸", color=C):
    print(f"  {color}{icono} {B}{num}{R}{color}){R}  {texto}")

def pedir(mensaje, color=G):
    return input(f"\n{color}{B}▶ {R}{color}{mensaje}: {R}").strip()

def enter(msg="Presiona Enter para continuar..."):
    input(f"\n{DIM}{msg}{R}")

def mostrar_bloque(lineas, color=BL):
    print(f"\n  {color}┌{'─'*(WIDTH-4)}┐{R}")
    print(f"  {color}│{R} {B}💡 Orientación{R}")
    print(f"  {color}│{R}")
    for l in lineas:
        for w in textwrap.wrap(l, width=WIDTH-6) or [""]:
            print(f"  {color}│{R}  {w}")
    frase = random.choice(FRASES_ALIENTO)
    print(f"  {color}│{R}")
    for w in textwrap.wrap(frase, width=WIDTH-6):
        print(f"  {color}│{R}  {G}{w}{R}")
    print(f"  {color}└{'─'*(WIDTH-4)}┘{R}")

def obtener_consejos(tema):
    datos = CONSEJOS.get(tema, {})
    resultado = list(datos.get("general", []))
    eco = perfil.get("economia", "")
    fam = perfil.get("familia", "")
    net = perfil.get("internet", "")
    mapa_eco = {"1":"muy_limitada","2":"limitada","3":"media","4":"media"}
    mapa_fam = {"2":"madre","3":"padre","4":"abuelos"}
    for clave, val in [(mapa_eco.get(eco,""), eco), (mapa_fam.get(fam,""), fam)]:
        if clave and clave in datos:
            resultado += datos[clave]
    if net in ("3","4") and "sin_internet" in datos:
        resultado += datos["sin_internet"]
    elif net in ("1","2") and "con_internet" in datos:
        resultado += datos["con_internet"]
    return resultado or ["No tengo información específica sobre ese tema aún."]

# ═══════════════════════════════════════════════════════
#  MÓDULOS
# ═══════════════════════════════════════════════════════

def configurar_perfil():
    cabecera()
    print(f"  {B}{M}📋 CONFIGURAR MI PERFIL{R}\n")
    print(f"  {DIM}Tus respuestas son privadas y personalizan los consejos.{R}\n")
    linea("─", M)

    preguntas = [
        ("grado",    "¿En qué grado estás?",
         [("1","Primero de secundaria"),("2","Segundo de secundaria"),("3","Tercero de secundaria")]),
        ("economia", "Situación económica de tu familia:",
         [("1","Muy limitada (a veces falta lo básico)"),("2","Limitada (alcanza justo)"),
          ("3","Media (no sobra pero no falta)"),("4","Estable")]),
        ("familia",  "¿Con quién vives principalmente?",
         [("1","Con ambos padres"),("2","Solo con mi mamá"),("3","Solo con mi papá"),
          ("4","Con abuelos u otros familiares"),("5","Otra situación")]),
        ("internet", "¿Cómo accedes a internet?",
         [("1","Wifi en casa siempre"),("2","Solo datos de celular"),
          ("3","Solo en la escuela"),("4","Muy poco o casi nada")]),
    ]

    for campo, pregunta, opciones in preguntas:
        print(f"\n  {B}{pregunta}{R}")
        for k, v in opciones:
            menu_opcion(k, v, color=M)
        validas = [o[0] for o in opciones]
        while True:
            op = pedir(f"Elige [1-{len(validas)}]", M)
            if op in validas:
                perfil[campo] = op
                break
            print(f"  {RE}Opción no válida.{R}")

    opciones_p = {
        "1":"Estrés escolar","2":"Redes sociales / celular","3":"Alcohol o drogas",
        "4":"Cigarro / vaping","5":"Bullying","6":"Problemas económicos",
        "7":"Problemas familiares","8":"Soledad / aislamiento",
        "9":"Ansiedad o depresión","10":"Autoestima e identidad",
    }
    print(f"\n  {B}¿Qué temas te preocupan? {DIM}(varios, separados por comas){R}")
    for k, v in opciones_p.items():
        menu_opcion(k, v, color=M)
    sel = pedir("Tu selección. Ej: 1,3,5", M)
    seleccionados = [s.strip() for s in sel.split(",") if s.strip() in opciones_p]
    perfil["preocupaciones"] = [opciones_p[s] for s in seleccionados]

    linea("─", M)
    print(f"\n  {G}{B}✅ Perfil guardado.{R}")
    if perfil["preocupaciones"]:
        print(f"  {DIM}Temas: {', '.join(perfil['preocupaciones'])}{R}")
    enter()


def orientacion():
    if not perfil["grado"]:
        print(f"\n  {Y}⚠ Primero configura tu perfil (opción 1).{R}")
        enter(); return

    cabecera()
    print(f"  {B}{BL}📖 ORIENTACIÓN POR TEMA{R}\n")
    print(f"  {B}Elige un tema:{R}\n")
    for k, (nombre, _, color) in MAPA_TEMAS.items():
        menu_opcion(k, nombre, color=color)
    print(f"\n  {DIM}0){R}  Volver al menú")

    while True:
        op = pedir("Elige un tema", BL)
        if op == "0": return
        if op in MAPA_TEMAS: break
        print(f"  {RE}Opción no válida.{R}")

    nombre, clave, color = MAPA_TEMAS[op]
    cabecera()
    print(f"  {B}{color}📌 {nombre.upper()}{R}\n")
    linea("─", color)
    mostrar_bloque(obtener_consejos(clave), color)
    enter()


def checkin_diario():
    cabecera()
    fecha = datetime.now().strftime("%d/%m/%Y")
    print(f"  {B}{G}🌟 CHECK-IN DIARIO{R}  {DIM}{fecha}{R}\n")
    linea("─", G)
    print(f"\n  {B}¿Cómo te sientes hoy?{R}\n")
    for k, (ico, desc) in ESTADOS_ANIMO.items():
        print(f"  {G}{k}){R}  {ico}  {desc}")
    while True:
        op = pedir("Elige [1-5]", G)
        if op in ESTADOS_ANIMO: break
        print(f"  {RE}Elige entre 1 y 5.{R}")

    icono, estado = ESTADOS_ANIMO[op]
    print(f"\n  Registrado: {icono} {B}{estado}{R}")
    print(f"\n  {B}¿Quieres contarme qué pasó hoy?{R} {DIM}(Enter para omitir){R}")
    detalle = input(f"  {G}{B}▶ {R}").strip()
    if detalle:
        print(f"\n  {DIM}Escuchado: '{detalle}'{R}")
    mostrar_bloque(CONSEJOS_ESTADO[op], G)
    enter()


def mostrar_recursos():
    cabecera()
    print(f"  {B}{G}📋 RECURSOS DE APOYO GRATUITOS{R}\n")
    linea("─", G)
    for nombre, contacto, desc, tags, color in RECURSOS:
        tags_str = "  ".join([f"{color}[{t}]{R}" for t in tags])
        print(f"\n  {color}{B}{nombre}{R}")
        print(f"     {B}{contacto}{R}")
        print(f"     {DIM}{desc}{R}")
        print(f"     {tags_str}")
    linea("─", G)
    enter()


def estado_perfil():
    if not perfil["grado"]:
        return f"  {DIM}Perfil: {RE}No configurado{R}"
    grados = {"1":"1°","2":"2°","3":"3°"}
    n = len(perfil["preocupaciones"])
    return f"  {DIM}Perfil activo: {G}{grados[perfil['grado']]} secundaria{R}{DIM} | {n} tema(s){R}"


def menu_principal():
    while True:
        cabecera()
        print(estado_perfil())
        print()
        linea("─", C)
        print(f"\n  {B}¿Qué quieres hacer?{R}\n")
        menu_opcion("1", "Configurar mi perfil",         "📋", M)
        menu_opcion("2", "Orientación por tema",         "📖", BL)
        menu_opcion("3", "Check-in diario",              "🌟", G)
        menu_opcion("4", "Recursos de apoyo gratuitos",  "📋", Y)
        menu_opcion("0", "Salir",                        "✖",  RE)
        print()
        linea("─", C)
        op = pedir("Elige una opción", C)
        if   op == "1": configurar_perfil()
        elif op == "2": orientacion()
        elif op == "3": checkin_diario()
        elif op == "4": mostrar_recursos()
        elif op == "0":
            cabecera()
            centrar("¡Cuídate mucho! Siempre puedes pedir ayuda. 💙", G)
            centrar("SAPTEL: 55 5259-8121  (24/7 · Gratis · Anónimo)", DIM)
            print()
            sys.exit(0)
        else:
            print(f"  {RE}Opción no válida.{R}")
            import time; time.sleep(1)


def bienvenida():
    cabecera()
    print(f"""
  {B}Bienvenido/a a Apoyo Estudiantil{R}

  {DIM}Orientación sobre:{R}

  {G}✓{R}  Adicciones y presión de grupo
  {G}✓{R}  Redes sociales y salud digital
  {G}✓{R}  Recursos según tu situación económica
  {G}✓{R}  Bullying y conflictos escolares
  {G}✓{R}  Salud mental y bienestar emocional

  {DIM}No necesita internet. Tu información es privada.{R}
    """)
    linea("─", C)
    print(f"\n  {Y}⚠  Si estás en crisis llama a:{R}")
    print(f"  {B}   SAPTEL: 55 5259-8121  (Gratis · Anónimo · 24/7){R}")
    enter("Presiona Enter para comenzar...")


if __name__ == "__main__":
    try:
        bienvenida()
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n\n  {DIM}Programa cerrado. ¡Cuídate! 💙{R}\n")
        sys.exit(0)