# Actividad 02

25% de la Nota Final

- Primera Convocatoria 30/06/2021
- Segunda Convocatoria 05/09/2021

Para hacer las entregas hay que hacer un tag al repositorio en una fecha anterior a la fecha de entrega de la actividad, y pegar el enlace al tag del repositorio en la actividad de blackboard.

Los ficheros de audio Mp3 tienen una serie de metadatos llamados tags, que contienen información acerca de la canción, su autor, álbum, nombre, año, género,... Es habitual que dicha información se muestre al usuario cuando está escuchando una canción a través del reproductor de audio, y muchas veces dicha información no está rellena o es incorrecta.
Para manejar, actualizar y rellenar dichos datos hay una serie de aplicaciones que se suelen llamar Mp3 Tag Editors.

El objetivo de esta actividad es desarrollar una aplicación que cumpla este objetivo, sea capaz de leer un fichero Mp3, acceder a sus metadatos, mostrárselos al usuario y darle la opción de modificarlos, y guardarlos de vuelta en el fichero Mp3.

Para la parte de GUI, se tiene que usar PyQt6 como se ha visto en clase. Para la parte específica de Mp3, se puede usar la librería eyeD3 de Python, que se puede encontrar en PyPI, https://pypi.org/project/eyed3/. Se puede consultar la documentación de dicha librería en https://eyed3.readthedocs.io/en/latest/ donde hay multitud de ejemplos de como usar dicha librería para acceder a los datos de un fichero Mp3 y como guardarlos.

Es suficiente con acceder y actualizar los tags más habituales, artist, album, title, track_number, genre, release_date,...

Se deja entera libertad al alumno a la hora de crear la interfaz de usuario, estructurar el layout como crea conveniente, los casos de uso y las funcionalidades que considere oportunas.
