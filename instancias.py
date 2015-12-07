import random

generos = [ "Thriller", "Romantica", "Aventura", "Terror", "Historica", 
"Ciencia-Ficcion", "Biografia", "Infantil", "Autoayuda", "Hogar", "Manual",
"Politica", "Erotica", "Economica", "Deportes", "Viajes", "Sociedad"]

escritores = ["Tolkien", "Roald dahl", "Jk rowling", "Douglas adams", "Luis zafon", "Tom clancy", "Elvira lindo", "Pepe colubi", "Cervantes"]

libros = [ 
"El extranjero",
"En busca del tiempo perdido",
"El proceso",
"El principito",
"La condiciaon humana",
"Viaje al fin de la noche",
"Las uvas de la ira",
"Por quiaen doblan las campanas",
"El gran Meaulnes",
"La espuma de los daias",
"El segundo sexo",
"Esperando a Godot",
"El ser y la nada",
"El nombre de la rosa",
"Archipiaelago Gulag",
"Paroles",
"Alcoholes",
"El Loto Azul",
"Las habitaciones de atraas",
"Tristes traopicos",
"Un mundo feliz",
"1984",
"Astaerix el Galo",
"La cantante calva",
"Tres ensayos sobre teoraia sexual",
"Opus nigrum",
"Lolita",
"Ulises",
"El desierto de los taartaros",
"Los monederos falsos",
"El hausar en el tejado",
"Bella del Seanor",
"Cien aanos de soledad",
"El ruido y la furia",
"Therese Desqueyroux",
"Zazie en el metro",
"La confusiaon de los sentimientos",
"Lo que el viento se llevao",
"El amante de Lady Chatterley",
"La montaana maagica",
"Buenos daias tristeza",
"El silencio del mar",
"La vida instrucciones de uso",
"El sabueso de los Baskerville",
"Bajo el sol de Satanaas",
"El gran Gatsby",
"La broma",
"El desprecio",
"El asesinato de Roger Ackroyd",
"Nadja",
"Auraelien",
"El zapato de raso",
"Seis personajes en busca de autor",
"El resistible ascenso de Arturo Ui",
"Viernes o la vida salvaje",
"La guerra de los mundos",
"Si esto es un hombre",
"El Seanor de los Anillos",
"Los zarcillos de la viana",
"Capital del dolor",
"Martin Eden",
"La balada del mar salado",
"El grado cero de la escritura",
"El honor perdido de Katharina",
"El mar de las Sirtes",
"Las palabras y las cosas",
"En el camino",
"El maravilloso viaje de Nils Holgersson",
"Una habitaciaon propia",
"Craonicas marcianas",
"El arrebato de Lol",
"El atestado",
"Tropismos",
"Diario 1887-1910",
"Lord Jim",
"Escritos",
"El teatro y su doble",
"Manhattan Transfer",
"Ficciones",
"Moravagine",
"El general del ejaercito muerto",
"La decisiaon de Sophie",
"Romancero gitano",
"La muerte ronda a Maigret",
"Santa Maraia de las Flores",
"El hombre sin atributos",
"Furor y misterio",
"El guardiaan entre el centeno",
"No hay orquaideas para Miss Blandish",
"Blake y Mortimer",
"Los cuadernos de Malte",
"La modificaciaon",
"Los oraigenes del totalitarismo",
"El maestro y Margarita",
"La crucifixiaon rosa",
"El sueano eterno",
"Amers",
"Tomaas el Gafe",
"Bajo el volcaan",
"Hijos de la medianoche"
]

print "(definstances instancies-generals"
for g in generos:
  a = g.replace(" ", "")
  print "([%s] of Genero" % a
  print "\t(nombre \"%s\")" % g
  print "\t(nsfw FALSE))"

for e in escritores:
  a = e.replace(" ", "")
  print "([%s] of Escritor\n\t(nombre \"%s\"))" % (a,e)


boolean = ["TRUE", "FALSE"]
toins =  lambda x: "[%s]" % x.replace(" ", "")
for l in libros:
  print "([%s] of Libro" % l.replace(" ", "")
  print "\t(paginas %d)" % random.randint(150, 1200)
  print "\t(polemico %s)" % random.choice(boolean)
  print "\t(nombre \"%s\")" % l
  print "\t(generos %s)" % ' '.join(map(toins, random.sample(generos, random.randint(1,3))))
  print "\t(escritor %s)" % toins(random.choice(escritores))
  print "\t(puntuacion %d)" % random.randint(0,10)
  print "\t(nsfw %s))" % random.choice(boolean)
  random.jumpahead(50)

print ")"
