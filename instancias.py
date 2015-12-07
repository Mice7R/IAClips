import random

generos = [ "Thriller", "Romantica", "Aventura", "Terror", "Historica", 
"Ciencia-Ficcion", "Biografia", "Infantil", "Autoayuda", "Hogar", "Manual",
"Politica", "Erotica", "Economica", "Deportes", "Viajes", "Sociedad"]

escritores = ["MagicAutor", "TomClancy", "God"]

libros = [ "El libro perfecto", "Aquel que no leerias", "Otro libro", 
  "Que chulo", "Alicia en el pais de las maravillas", "Q", "QQ", "QQQ" ]

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
