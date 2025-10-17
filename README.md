# Coversiones
En el mundo actual, factores como la globalización y el desarrollo tecnológico demandan competencias matemáticas y digitales aplicables. Esto implica formar personas capaces de combinar precisión, rapidez y comprensión, para ofrecer soluciones creativas a los retos del día a día.Tanto en la educación como en ámbitos profesionales, se requiere de personas que manejen correctamente los sistemas numéricos y las unidades de medida, utilizándolos como una herramienta para resolver problemas y tomar decisiones informadas de forma efectiva.

No obstante, la conversión entre distintos sistemas suele ser compleja y propensa a errores. La falta de herramientas integrales limita la eficiencia y el aprendizaje significativo. En este sentido, plataformas educativas como GeoGebra han demostrado que los entornos interactivos favorecen el aprendizaje activo, mejoran la comprensión de conceptos abstractos y acercan la teoría a situaciones reales (Ziatdinov, 2022).

Con base en ello, consideramos que existe la oportunidad de integrar estas competencias en una interfaz interactiva que permita a los usuarios realizar conversiones numéricas y de unidades, potenciando así su formación educativa, profesional o cotidiana. El proyecto consistirá en una plataforma desarrollada en Python, al estilo de una calculadora con interfaz modular que permite al usuario elegir de entre varias opciones, ingresar datos, obtener resultados precisos en distintas unidades o sistemas numéricos y guardar sus resultados en un historial.

# Cómo funciona
La calculadora contará con módulos temáticos que permitirán realizar diversas conversiones:

•	Módulo 1: Numérico avanzado.
- Decimal a binario/Octal/Hexadecimal
- Decimal a números romanos

•	Módulo 2: Físico
- Longitud: metros/kilómetros/millas/años luz
- Temperatura: °C/K/°F/Rankine

•	Módulo 3: Digital
- Byte a Kilobyte/Kilobyte a Megabyte/Megabyte a Gigabyte
- Bytes por segundo/Megabyte por segundo

•	 Módulo 4: Creativo
- Altura en Torres de Libros
- Energía a barras de chocolate
- Peso en gatos y gatitos
- Volumen en propiedades de un agujero negro
- Distancia en Animales marinos

De esta manera, el proyecto busca fomentar la experimentación, el pensamiento lógico, la cultura científica y tecnológica, así como la curiosidad del usuario.

ALGORITMO GENERAL del Proyecto:
Inicio
1.	Mostrar menú principal con las siguientes opciones:
  o	Módulo 1: Numérico avanzado
  o	Módulo 2: Físico
  o	Módulo 3: Digital
  o	Módulo 4: Creativo
  o	Ver historial
  o	Salir
2.  Solicitar una opción de participación al usuario.
3.	Leer la opción seleccionada por el usuario.
4.  Mientras opción ≠ "Salir" hacer
        Si opción = "Numérico avanzado" entonces
            Ejecutar módulo numérico
        Si opción = "Físico" entonces
            Ejecutar módulo físico
        Si opción = "Digital" entonces
            Ejecutar módulo digital
        Si opción = "Creativo" entonces
            Ejecutar módulo creativo
        Si opción = "Historial" entonces
            Mostrar historial
        FinSi
        Mostrar menú principal
        Leer nueva opción
    FinMientras

# Referencias

Ziatdinov, R., & Valles Jr., J. R. (2022). Synthesis of modeling, visualization, and programming in GeoGebra as an effective approach for teaching and learning STEM topics. Mathematics, 10(3), 398. https://doi.org/10.3390/math10030398


