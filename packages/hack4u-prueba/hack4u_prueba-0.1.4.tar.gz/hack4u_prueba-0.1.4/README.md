



## Cursos disponibles:

- Introducción al Linux [15 horas]
- Personalización de Linux [3 horas]
- Introducción al Hacking [54 horas]

## Instalación

Instala el paqute usando `pip3`:

```python3
pip3 install hack4u
```

## Uso básico

### Listar todos los cursos

```python3
from hack4u import list_courses

from course in courses:
    print(course)
```

### Obtener un curso por su nombre

```python3
from hack4u import get_course_by_name

course = get_course_by_name("Introducción a Linux")
print(course)
```

### Calcular ducarión total de los cursos

``` python3
from hack4u.utils import total_duration

print(f"Duración total: {total.duration()} horas")
```
