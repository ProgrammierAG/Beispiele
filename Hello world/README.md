# Hello.py

Das Programm soll **Hello world** ausgeben.

```python
print("Hello world")
```

---


Da wir echt krasse Programmierer sind, reicht das nicht.

Deshalb wollen wir unseren Nutzer persöhnlich grüßen, dies machen wir mit der  `input()`  Funktion.

---

Wir wissen, dass man Ausgabewerte von Funktionen in Variablen speichern kann, deshalb speichern wir den namen in der variable `name` - wir sind so genial.
```python
name = input("Wie heißt du?")
```
Jetzt wollen wir das auch ausgeben. Für die Kombination von der ausgabe, die wir definieren und der gespeicherten Variable, gibt es viel wege.

```python
print("Hallo,", name)
print("Hallo, " + name)
print(f"Hallo, {name}")
```
Alle Methoden erzielen das gleiche. Wir haben uns aber für die dritte entschieden, weil sie, trotz den komischen Klammern, einfacher zu lesen ist und weil wir so mehrere variablen speichern können.