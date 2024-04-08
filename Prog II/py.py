import matplotlib.pyplot as plt



class HashTable(Diccionario):
    """
    Implementación de Diccionario con tabla hash
    de tamaño fijo y resolución de colisiones
    por encadenamiento
    """

    def __init__(self, size: int):
        """
        El constructor inicializa una tabla de tamaño `size` que recibe
        como parametro. Utiliza el tipo lista incluido en Python
        """
        ### COMPLETAR AQUI CON SU CODIGO.
        self.size = size
        self.table = [None] * size

    def funcion_hash(self, key: Clave):
        """
        Recibe como parametro la clave convertida a int y devuevle el
        modulo entre el valor recibido y el tamaño de la tabla
        """
        return key % self.size

    def insert(self, key: Clave, data: Any) -> None:
        """
          Implementacion del metodo insert, recibe como parametros el objeto Clave
        y dato al que hace referencia.

          Este metodo asigna las claves al bucket correspondiente
        en función de su valor hash y gestiona tanto la inserción de nuevas
        claves como la actualización de claves existentes en la tabla hash.

          No retorna un resultado.

          Bucket: contenedor o compartimento utilizado para almacenar un conjunto de elementos.
        """
        ### COMPLETAR AQUI CON SU CODIGO
        key_hash = self.funcion_hash(key.to_int()) # llamo al modulo to_int(), y le paso el resultado a la funcion hash
        if self.table[key_hash] is None:
            self.table[key_hash] = [(key, data)]
            return
        elif self.table[key_hash] is not None: # verifico la existencia de la key dentro del valor hash, de existir se actualiza el dato
            for rango in range(0, len(self.table[key_hash])):
                if self.table[key_hash][rango][0] == key:
                    self.table[key_hash][rango] = [(key, data)]
                    return
        self.table[key_hash].append((key, data))

    def search(self, key: Clave) -> Any | None:
        """
         Implementacion del metodo search. Recibe como parametro la clave y retorna
        el valor asociado en caso de existir, o None en caso contrario.

          Calcula el hash de la clave que se está buscando y verifica si la
        posición calculada por el hash está vacía. De ser asi se devuelve None para
        indicar que la clave no se encuentra en la tabla.
          Si hay entradas en ese bucket, se recorren para buscar una clave específica.
        Cuando se encuentra la coincidencia, se devuelve el valor asociado a esa clave.


        """
        ### COMPLETAR AQUI CON SU CODIGO.
        key_hash = self.funcion_hash(key.to_int())
        if self.table[key_hash] == None:
            return None
        else:
            for k, valor in self.table[key_hash]:
              if k == key:
                return valor

    def delete(self, key: Clave) -> None:
        """
          Implementacion del metodo delete. Recibe como parametro la key de la clase Clave y no devuelve valor.

          Se verifica si hay una entrada en esa posición de la tabla. Si hay entradas (tuplas),
        se recorren para encontrar la tupla que tiene la misma clave que se desea eliminar.

          Cuando se encuentra la coincidencia, esa tupla se elimina del bucket.
        """
        ### COMPLETAR AQUI CON SU CODIGO.
        key_hash = self.funcion_hash(key.to_int())
        if self.table[key_hash] is not None:
            for i, (k, _) in enumerate(self.table[key_hash]): #  con el _ indico que no estoy interesados en la segunda parte de la tupla
                if k == key:
                    del self.table[key_hash][i]

    def __len__(self) -> int:
        """
        Este método sobrecarga la función `len`.

        Debe devolver la cantidad de elementos insertados en la tabla.

        Si la tabla esta vacía, devuelve cero, sino inicializa un contador en cero.
        Luego, recorre cada bucket en la tabla hash y suma la cantidad de elementos al contador.
        Finalmente, devuelve el valor del contador.
        """
        ### COMPLETAR AQUI CON SU CODIGO.
        if self.table is None:
          return 0
        contador = 0
        for lista in self.table:
            if lista is not None:
                contador += len(lista)
        return contador

    def _load_factor(self) -> float:
        """
        Este método debe devolver el factor de carga de la tabla.

        Obtiene la cantidad de elementos almacenados en la tabla y la capacidad total
        de la tabla y calcula el factor de carga dividiendo la cantidad de elementos
        almacenados por la capacidad total.
        """
        ### COMPLETAR AQUI CON SU CODIGO.
        almacenado = 0  # Inicializa la cantidad de elementos almacenados
        almacenado = len(self)
        capacidad = self.size  # Obtiene la capacidad total de la tabla
        load_factor = almacenado / capacidad  # Calcula el factor de carga
        return load_factor


    def _longest_list(self) -> int:
        """
        Este método debe devolver la longitud de la lista mas larga de la tabla
        """
        ### COMPLETAR AQUI CON SU CODIGO.

        longitud_max = 0
        for bucket in self.table:
            if bucket is not None:
                longitud_max = max(longitud_max, len(bucket))
        return longitud_max


    def __str__(self) -> str:
        """
        Mostrar la cantidad de elementos de la tabla (__len__), el factor de carga (_load_factor)
        y la longitud de la lista mas larga (_longest_list)
        """
        ### COMPLETAR AQUI CON SU CODIGO.
        elements_count = len(self)
        load_factor = self._load_factor()
        longest_list_length = self._longest_list()

        return f"Elementos en la tabla: {elements_count}\n" \
            f"Factor de carga: {load_factor}\n" \
            f"Longitud de la lista más larga: {longest_list_length}"

    def grafico(self):
        """
        Muestra una grafica de la distribucion de elementos en la lista
        """
        longitudes = []
        barras = 0
        elementos = 0
        for i in self.table:
            count = 0
            actual = i
            if actual is not None:
                barras += 1
            while actual is not None:
                count += 1
                elementos += 1
        longitudes.append(count)

        promedio = elementos/barras

        indices = list(range(len(longitudes)))

        fig, ax = plt.subplots()

        # Cambiar el fondo a blanco
        fig.set_facecolor('white')

        # Crear un gráfico de barras con colores personalizados
        bar_colors = 'lightcoral'
        edge_color = bar_colors
        bar_width = 0.1

        # Crear un gráfico de barras con colores que contrasten
        plt.bar(indices, longitudes, color= bar_colors, edgecolor=edge_color, width=bar_width)

        # Personalizar el título y etiquetas
        text = f"Índice\n\n Datos de la tabla\n Cantidad total de elementos: {self._len_()} \ Factor de carga: {round(self._load_factor(),2)} \ Longitud de la lista mas larga: {self._longest_list()} \ Promedio Elementos por Lista: {round(promedio,2)}"
        plt.title('Base de datos del Inventario', fontsize=18, color='black')
        plt.xlabel(text, fontsize=12, color='black')
        plt.ylabel('Cantidad de Elementos', fontsize=12, color='black')

        # Puedes ajustar el tamaño de la figura si es necesario
        fig.set_size_inches(20, 6)

        ax.tick_params(axis='x', colors='black')
        ax.tick_params(axis='y', colors='black')

        # Calcular las coordenadas para centrar el texto debajo del gráfico
        text_x = (max(indices) + min(indices)) / 2 # Centrar horizontalmente
        text_y = min(plt.yticks()[0]) - 1  # Colocar debajo del eje y

        plt.show()