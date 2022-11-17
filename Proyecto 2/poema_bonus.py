import random

lista_frases_ejemplo = ["Estoy perdido como un pajaro", "Con la tristeza de un humano","Me mirabas y sentia mi pecho","Tus ojos tristes, mi gesto","Quiero volar pero mi vuelo esta","La noche esta fria y tu mano","Miro hacia arriba y el cielo esta","Autopistas infinitas, un camino","Titilan los astros y al verte me siento","El pasado ya no es nuestro, el futuro esta","Pero existes, y al ver tu rostro me siento","Sus ojos brillaban como un diamante", "Cuando miraba su alma me sentia", "Y yo con el sentimiento de un autoestopista", "Como cuando miro al cielo", "Con la sensacion de un piscinero","Y la nieve estaba sobre el libro", "La lluvia caia sobre la casa del", "La suerte estaba del lado de aquel", "Nacian virutas desde la mirada del", "Nadie sabia de donde venia aquel hombre", "La tristeza invadio a aquel que no conocia el", "Puesto que la marcha habia supuesto un", "No suponia un reto para aquel tio", "Sufriamos la situacion que tenemos por ser un", "Llego el momento de sufrir todo lo zanjado"]
lista_palabras_bonitas_ado = ["ahitado", "amado", "aviado", "becado", "binado", "birlado", "blincado", "bordado", "boyado", "bramado", "brindado", "brumado", "bufado", "cegado", "chaflado", "charrado", "chirriado", "chochado", "chollado", "choyado", "cismado", "clorado", "corado", "costado", "cotado", "crispado", "croado", "cuchado", "cuidado", "cunado", "desbruado", "desgrado", "drenado", "duchado", "emprado", "enriado", "expiado", "faltado", "feriado", "foliado", "forjado", "fraguado", "fricado", "gofrado", "guinchado", "hastiado", "horado", "hoyado", "huevado", "jamado", "jambado", "jarciado", "juzgado", "lardado", "lastrado", "legado", "llorado", "macado", "mallado", "marchado", "masado", "merado", "mesado", "migado", "migrado", "morcado", "morfado", "mugado", "papado", "pendrado", "pescado", "potado", "poyado", "pujado", "pullado", "pulsado", "puntado", "puntuado", "raspado", "rispado", "rochado", "salgado", "salmado", "salvado", "seriado", "situado", "tascado", "timado", "tramado", "turbado", "untado", "vejado", "velado", "vitado", "volcado", "yantado", "yapado", "zallado", "zampado"]
lista_palabras_bonitas_ido = ["acleido", "algaido", "ardido", "bandido", "batido", "bebido", "bellido", "cabido", "canido", "caido", "cencido", "cogido", "cohibido", "comido", "complido", "corrido", "crecido", "cumplido", "curtido", "dolido", "fabrido", "falido", "fallido", "febrido", "fingido", "florido", "fornido", "fruncido", "fundido", "galdido", "gandido", "garrido", "hardido", "hendido", "herido", "infido", "ingrido", "instruido", "lamido", "leido", "lucido", "manido", "marcido", "marrido", "mentido", "metido", "mordido", "movido", "nacido", "nutrido", "pansido", "partido", "perdido", "podrido", "polido", "prendido", "pulido", "raido", "rendido", "roido", "sabido", "salido", "sencido", "sentido", "subido", "sufrido", "surtido", "tapido", "tendido", "torcido", "transido", "traido", "tullido", "tupido", "vaguido", "valido", "vellido", "vivido"]

numero_frases_poema = int(input("Cuantos parrafos de cuatro versos quieres que tenga tu poema para evitar la guerra contra los Vogos? "))
contador_versos_poemas = 0
print("===============================POEMA==========================")
print("")
while contador_versos_poemas < numero_frases_poema:

    #1
    frase_primera = random.randint(0, len(lista_frases_ejemplo)-1)
    palabra_ado = random.randint(0, len(lista_palabras_bonitas_ado)-1)
    frase_imprimir = lista_frases_ejemplo[frase_primera] + " " + lista_palabras_bonitas_ado[palabra_ado]
    print(frase_imprimir)

    #2
    frase_primera = random.randint(0, len(lista_frases_ejemplo)-1)
    palabra_ido = random.randint(0, len(lista_palabras_bonitas_ido)-1)
    frase_imprimir = lista_frases_ejemplo[frase_primera] + " " + lista_palabras_bonitas_ido[palabra_ido]
    print(frase_imprimir)

    #3
    frase_primera = random.randint(0, len(lista_frases_ejemplo)-1)
    palabra_ido = random.randint(0, len(lista_palabras_bonitas_ido)-1)
    frase_imprimir = lista_frases_ejemplo[frase_primera] + " " + lista_palabras_bonitas_ido[palabra_ido]
    print(frase_imprimir)

    #4
    frase_primera = random.randint(0, len(lista_frases_ejemplo)-1)
    palabra_ado = random.randint(0, len(lista_palabras_bonitas_ado)-1)
    frase_imprimir = lista_frases_ejemplo[frase_primera] + " " + lista_palabras_bonitas_ado[palabra_ado]
    print(frase_imprimir)
    contador_versos_poemas += 1
    print("")
print("")
print("==============================================================")
