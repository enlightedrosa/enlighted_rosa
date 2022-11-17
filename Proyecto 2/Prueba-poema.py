import random

lista_adjetivos_bonitas_ido = ["acleido", "algaido", "ardido", "bandido", "batido", "bebido", "bellido", "cabido", "canido", "caido", "cencido", "cogido", "cohibido", "comido", "complido", "corrido", "crecido", "cumplido", "curtido", "dolido", "fabrido", "falido", "fallido", "febrido", "fingido", "florido", "fornido", "fruncido", "fundido", "galdido", "gandido", "garrido", "hardido", "hendido", "herido", "infido", "ingrido", "instruido", "lamido", "leido", "lucido", "manido", "marcido", "marrido", "mentido", "metido", "mordido", "movido", "nacido", "nutrido", "pansido", "partido", "perdido", "podrido", "polido", "prendido", "pulido", "raido", "rendido", "roido", "sabido", "salido", "sencido", "sentido", "subido", "sufrido", "surtido", "tapido", "tendido", "torcido", "transido", "traido", "tullido", "tupido", "vaguido", "valido", "vellido", "vivido"]
lista_verbos = ["gorflingola", "tremola", "vendata", "perspicuza", "verbinca", "flafetatea", "bebiciona", "malificiona", "zazobra", "testesta", "flifea", "raspeta", "wapliea", "cercezona", "namiciona","corta", "moria", "retuerce", "carcome", "deduce", "reduciria", "agrava", "secciona", "vota", "flotaria", "volo", "lave", "taladra", "cavare", "sostenga", "mantiene", "flagele", "suturaria", "mate", "enciende", "atrasase", "perturbara", "trabaje", "publicase", "resistiese"]
numero_frases_poema = 0
contador_versos_poemas = 0

lista_det_sustantivo = ["tomate"]


print("===============================POEMA==========================")
print("")
while contador_versos_poemas != 100:
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
