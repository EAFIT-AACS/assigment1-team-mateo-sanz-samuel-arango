# Autores Mateo Sanz Medina, Samuel Arango Echeveri
# Practica 1 lenguajes 
def obtener_grupo(particiones, estado):
    for indice, grupo in enumerate(particiones):
        if estado in grupo:
            return indice
    return -1

def minimizardfa(estados, alfabeto, estados_finales, transiciones):
    particiones = [sorted(estados_finales), sorted(set(estados) - estados_finales)]
    
    while True:
        nuevasparticiones = []
        for grupo in particiones:
            subdivisiones = {}
            for estado in grupo:
                clave = tuple(obtener_grupo(particiones, transiciones[estado][simbolo]) for simbolo in range(len(alfabeto)))
                if clave not in subdivisiones:
                    subdivisiones[clave] = []
                subdivisiones[clave].append(estado)
            
            nuevasparticiones.extend(sorted(subgrupo) for subgrupo in subdivisiones.values())
        
        if sorted(nuevasparticiones, key=lambda x: sorted(x)) == sorted(particiones, key=lambda x: sorted(x)):
            break
        particiones = nuevasparticiones
    
    resultado = " ".join(f"({grupo[i]},{grupo[j]})" for grupo in particiones if len(grupo) > 1 for i in range(len(grupo)) for j in range(i + 1, len(grupo)))
    return resultado if resultado else "No hay estados equivalentes"

def leer_entrada(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
    
    indice = 0
    num_casos = int(lineas[indice].strip())
    indice += 1
    
    casos = []
    
    for _ in range(num_casos):
        num_estados = int(lineas[indice].strip())
        indice += 1
        
        alfabeto = lineas[indice].strip().split()
        indice += 1
        
        estados_finales = set(map(int, lineas[indice].strip().split()))
        indice += 1
        
        transiciones = []
        for _ in range(num_estados):
            datos = list(map(int, lineas[indice].strip().split()))
            indice += 1
            if len(datos) < len(alfabeto) + 1:
                raise ValueError(f"Error en estado {_}: número incorrecto de transiciones.")
            transiciones.append(datos[1:])
        
        casos.append((num_estados, alfabeto, estados_finales, transiciones))
    
    return num_casos, casos

def automata():
    archivo = "archivo.txt"
    try:
        _ , casos = leer_entrada(archivo)
        for i, (num_estados, alfabeto, estados_finales, transiciones) in enumerate(casos, 1):
            resultado = minimizardfa(range(num_estados), alfabeto, estados_finales, transiciones)
            print(f"Caso {i}: {resultado}")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    automata()
   