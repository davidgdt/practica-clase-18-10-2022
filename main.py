def ejercicio1():
  lista = ["p", "t"]
  lista.insert("q","r", "s")
  lista.insert(1, "y")
  lista.append("h")
  lista.append("o")
  lista.append("n")
  assert "".join(lista) == "python"

def ejercicio2():
  lista = [1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9]
  lista.remove(4)
  lista.remove(4)
  lista.remove(5)
  lista.remove(7)
  lista.remove(8)  
  lista.remove(9)
  assert lista == list(range(4, 5))