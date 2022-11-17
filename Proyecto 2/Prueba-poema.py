import random

lista_adjetivos_bonitas_ido = ["acleido", "algaido", "ardido", "bandido", "batido", "bebido", "bellido", "cabido", "canido", "caido", "cencido", "cogido", "cohibido", "comido", "complido", "corrido", "crecido", "cumplido", "curtido", "dolido", "fabrido", "falido", "fallido", "febrido", "fingido", "florido", "fornido", "fruncido", "fundido", "galdido", "gandido", "garrido", "hardido", "hendido", "herido", "infido", "ingrido", "instruido", "lamido", "leido", "lucido", "manido", "marcido", "marrido", "mentido", "metido", "mordido", "movido", "nacido", "nutrido", "pansido", "partido", "perdido", "podrido", "polido", "prendido", "pulido", "raido", "rendido", "roido", "sabido", "salido", "sencido", "sentido", "subido", "sufrido", "surtido", "tapido", "tendido", "torcido", "transido", "traido", "tullido", "tupido", "vaguido", "valido", "vellido", "vivido"]
lista_verbos = ["gorflingola", "tremola", "vendata", "perspicuza", "verbinca", "flafetatea", "bebiciona", "malificiona", "zazobra", "testesta", "flifea", "raspeta", "wapliea", "cercezona", "namiciona","corta", "moria", "retuerce", "carcome", "deduce", "reduciria", "agrava", "secciona", "vota", "flotaria", "volo", "lave", "taladra", "cavare", "sostenga", "mantiene", "flagele", "suturaria", "mate", "enciende", "atrasase", "perturbara", "trabaje", "publicase", "resistiese"]
contador_versos_poemas = 0

lista_det_sustantivo = ["la fiesta", "la clientela", "el teatro", "el partido", "el cuadro", "el radio", "la computadora", "el candado", "el cuchillo", "el diputado", "el piso", "los fideos", "la madera", "el famoso", "el entusiasmo", "los autos", "el discurso", "la campera", "el coro", "las gas", "la cama", "el vocabulario", "la tristeza", "el departamento", "la tropa", "la tecla", "el refugio", "el hierro", "los diarios", "el candidato", "la pradera", "la ensalada", "la silla", "la puerta", "la persiana", "la oficina", "el buzo", "el odio", "la planta", "la alma", "la ceremonia", "la corbata", "el ojo", "el racimo", "la bomba", "el zapato", "la angustia", "los caramelos", "la impresora", "los anteojos", "las cartas", "la herramienta", "el ruido", "el cuaderno", "el tiempo", "la percha", "la muela", "la remera", "el mono", "la elegancia", "la planeta", "la persona", "el verano", "la riqueza", "el castillo", "la botella", "el gobierno", "el plato", "el templo", "el palo", "la guerra", "la abuela", "el velero", "el tornillo", "el mano", "el granizo", "el colegio", "la familia", "las hojas", "la presidencia", "el edificio", "la lima", "la fauna", "la mapa", "la lapicera", "la pantalla", "la escuela", "la servilleta", "el teclado", "la cuna", "el pelo", "la manada", "los perros", "la discoteca", "la rueda", "la letra", "el aluminio", "los libros", "el martillo", "la crema", "la guitarra", "el equipo"]


print("===============================POEMA==========================")
print("")
numero_frases_poema = int(input("Cuantos versos quieres que tenga tu poema para evitar la guerra contra los Vogos? "))
while contador_versos_poemas < numero_frases_poema:
    #det + sustantivo + adjetvi + verbo
    n_det_sustantivo = random.randint(0,len(lista_det_sustantivo)-1)

    n_adjetivo = random.randint(0, len(lista_adjetivos_bonitas_ido)-1)

    n_verbo = random.randint(0, len(lista_verbos)-1)

    frase_imprimir = lista_det_sustantivo[n_det_sustantivo] + " " + lista_verbos[n_verbo] + " " + lista_adjetivos_bonitas_ido[n_adjetivo]
    print(frase_imprimir)
    contador_versos_poemas += 1
print("")
print("==============================================================")
