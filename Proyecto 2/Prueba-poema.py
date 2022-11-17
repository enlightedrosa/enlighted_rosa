import random

lista_adjetivos_bonitas_ido = ["acleido", "algaido", "ardido", "bandido", "batido", "bebido", "bellido", "cabido", "canido", "caido", "cencido", "cogido", "cohibido", "comido", "complido", "corrido", "crecido", "cumplido", "curtido", "dolido", "fabrido", "falido", "fallido", "febrido", "fingido", "florido", "fornido", "fruncido", "fundido", "galdido", "gandido", "garrido", "hardido", "hendido", "herido", "infido", "ingrido", "instruido", "lamido", "leido", "lucido", "manido", "marcido", "marrido", "mentido", "metido", "mordido", "movido", "nacido", "nutrido", "pansido", "partido", "perdido", "podrido", "polido", "prendido", "pulido", "raido", "rendido", "roido", "sabido", "salido", "sencido", "sentido", "subido", "sufrido", "surtido", "tapido", "tendido", "torcido", "transido", "traido", "tullido", "tupido", "vaguido", "valido", "vellido", "vivido"]
lista_palabras_bonitas_ado = ["ahitado", "amado", "aviado", "becado", "binado", "birlado", "blincado", "bordado", "boyado", "bramado", "brindado", "brumado", "bufado", "cegado", "chaflado", "charrado", "chirriado", "chochado", "chollado", "choyado", "cismado", "clorado", "corado", "costado", "cotado", "crispado", "croado", "cuchado", "cuidado", "cunado", "desbruado", "desgrado", "drenado", "duchado", "emprado", "enriado", "expiado", "faltado", "feriado", "foliado", "follado", "forjado", "fraguado", "fricado", "gofrado", "guinchado", "hastiado", "horado", "hoyado", "huevado", "jamado", "jambado", "jarciado", "juzgado", "lardado", "lastrado", "legado", "llorado", "macado", "mallado", "marchado", "masado", "merado", "mesado", "migado", "migrado", "morcado", "morfado", "mugado", "papado", "pendrado", "pescado", "potado", "poyado", "pujado", "pullado", "pulsado", "puntado", "puntuado", "raspado", "rispado", "rochado", "salgado", "salmado", "salvado", "seriado", "situado", "tascado", "timado", "tramado", "turbado", "untado", "vejado", "velado", "vitado", "volcado", "yantado", "yapado", "zallado", "zampado"]
lista_verbos = ["gorflingola eh...", "tremola", "vendata", "perspicuza", "verbinca", "flafetatea", "bebiciona", "malificiona", "zazobra", "testesta mmm...", "flifea", "raspeta", "wapliea eh...", "cercezona", "namiciona mm...","corta", "moria", "retuerce ehh..", "carcome", "deduce", "reduciria mmm...", "agrava", "secciona", "vota", "flotaria eh...", "volo", "lave", "taladra", "cavare mm...", "sostenga", "mantiene", "flagele", "suturaria ehh...", "mate", "enciende", "atrasase ehh... mm....", "perturbara", "trabaje", "publicase mmm...", "resistiese"]
contador_versos_poemas = 0

lista_det_sustantivo = ["la juegika", "la tropioka", "el tripouille", "el porttrillo", "el crincos", "el joua", "la cokisea", "el fillotero", "el chiucholleno", "el dopitone", "el sipole", "los kokesos", "la remocailla", "el famoso", "el entusiasmo", "los autos", "el discurso", "la campera", "el coro", "las gas", "la cama", "el vocabulario", "la tristeza", "el departamento", "la tropa", "la tecla", "el refugio", "el hierro", "los diarios", "el candidato", "la pradera", "la ensalada", "la silla", "la puerta", "la persiana", "la oficina", "el buzo", "el odio", "la planta", "la alma", "la ceremonia", "la corbata", "el ojo", "el racimo", "la bomba", "el zapato", "la angustia", "los caramelos", "la impresora", "los anteojos", "las cartas", "la herramienta", "el ruido", "el cuaderno", "el tiempo", "la percha", "la muela", "la remera", "el mono", "la elegancia", "la planeta", "la persona", "el verano", "la riqueza", "el castillo", "la botella", "el gobierno", "el plato", "el templo", "el palo", "la guerra", "la abuela", "el velero", "el tornillo", "el mano", "el granizo", "el colegio", "la familia", "las hojas", "la presidencia", "el edificio", "la lima", "la fauna", "la mapa", "la lapicera", "la pantalla", "la escuela", "la servilleta", "el teclado", "la cuna", "el pelo", "la manada", "los perros", "la discoteca", "la rueda", "la letra", "el aluminio", "los libros", "el martillo", "la crema", "la guitarra", "el equipo", "el nabeho", "el fafeho", "el aakewo", "el oaceio", "el maweno", "el taieuo", "el qaleoo", "el fahedo", "el takexo", "el dafeao", "el hawebo", "el jadewo", "el gapeyo", "el baeeeo", "el waeeao", "el raaeoo", "el xakeuo", "el tajeeo", "el yageoo", "el taiebo", "el caiego", "el fafeno", "el oapeto", "el watefo", "el oagebo", "el kauero", "el laceao", "el daaemo", "el paiewo", "el tasero", "el jaleco", "el takeao", "el kakeuo", "el kawewo", "el pajewo", "el baneto", "el tatejo", "el xaneno", "el xakebo", "el waueeo", "el paeego", "el paneqo", "el vamebo", "el rahero", "el safemo", "el kateuo", "el xayemo", "el jaueko", "el iaweeo", "el bavemo", "el qameto", "el nafeco", "el uaeexo", "el paeero", "el oaleto", "el xakepo", "el daieio", "el wayebo", "el pavedo", "el baieso", "el uaqeho", "el raseko", "el iayevo", "el wameko", "el iadeko", "el dajeko", "el daeemo", "el paremo", "el wadejo", "el haxefo", "la nabeha", "la fafeha", "la aakewa", "la oaceia", "la mawena", "la taieua", "la qaleoa", "la faheda"]


print("===============================POEMA==========================")
print("")
a = 0
numero_frases_poema = int(input("[ACCESO DE SUPERUSUARIO CONCEDIDO]. Cuantas passwords quieres?: "))
while contador_versos_poemas < numero_frases_poema:
    #det + sustantivo + adjetvi + verbo
    n_det_sustantivo = random.randint(0,len(lista_det_sustantivo)-1)
    n_det_sustantivo2 = random.randint(0,len(lista_det_sustantivo)-1)

    n_adjetivo = random.randint(0, len(lista_adjetivos_bonitas_ido)-1)

    n_verbo = random.randint(0, len(lista_verbos)-1)
    n_verbo2 = random.randint(0, len(lista_verbos)-1)

    if a % 4 == 0: 
        frase_imprimir = lista_det_sustantivo[n_det_sustantivo] + " " + lista_verbos[n_verbo] + " " + lista_adjetivos_bonitas_ido[n_adjetivo] + " " + lista_det_sustantivo[n_det_sustantivo2]
    elif a  % 4 == 1:
        frase_imprimir = lista_verbos[n_verbo] + " " + lista_det_sustantivo[n_det_sustantivo] + " " + lista_adjetivos_bonitas_ido[n_adjetivo] + " " + lista_verbos[n_verbo2]
    elif a  % 4 == 2:
        frase_imprimir = lista_det_sustantivo[n_det_sustantivo] + " " + lista_verbos[n_verbo] + " " + lista_palabras_bonitas_ado[n_adjetivo] + " " + lista_det_sustantivo[n_det_sustantivo2]
    elif a  % 4 == 3:
        frase_imprimir = lista_verbos[n_verbo] + " " + lista_det_sustantivo[n_det_sustantivo] + " " + lista_palabras_bonitas_ado[n_adjetivo] + " " + lista_verbos[n_verbo2]
    print(frase_imprimir)
    contador_versos_poemas += 1
    a += 1
print("8905KLSK&&$)$WKDSKW$UEIU?=$WJKDSJDS$)(DSKLDSSDJLSKDJSKDSDSOD()$=WDSLKKLSD")
print("")
print("[ERROR 42: POESIA VOGONA. AUTODESTRUCCION INMINENTE]")
while True:
    i = 1