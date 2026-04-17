# DayLog [v1.0]

Aplicación personal para registrar tareas diarias, enfocada en simplicidad, control manual del tiempo y persistencia de datos.


## Descripción

DayLog es una herramienta simple para llevar seguimiento del progreso diario, organizada por días y semanas.

El sistema está diseñado para ser claro, mantenible y fácil de extender a futuro.


## Cambios recientes

- Se pulió la estructura general del proyecto
- Mejora en la organización y claridad del código
- Mejora en comentarios para mayor mantenibilidad
- Ajustes en la interfaz para una experiencia más consistente
- Implementación de tema oscuro (QSS)
- Refinamiento general del flujo de la aplicación
- Persistencia real en el sistema del usuario (`~/.daylog`)
- Generación de ejecutable usando PyInstaller


## Estructura
```Bash
DayLog/
├── main.py # Archivo principal.
├── panel/ # Archivos de UI.
├── manager/ # Lógica de negocio.
├── data/ # Datos generales.
├── build/ # Artefactos de build.
└── daylog # <<< Ejecutable >>>
```


## Cómo ejecutar

1. Abrir una terminal dentro de la carpeta del proyecto
2. Dar permisos de ejecución al launcher: `chmod +x daylog`

3. Ejecutar la aplicación:
- Doble clic en el archivo daylog
- o desde terminal ejecutar: `./daylog`