# Reproducibilidad Computacional para Conversión Tiempo a Profundidad de Datos Sísmicos

## Descripción General

Este es un documento de tesis académica que aborda la **conversión de datos sísmicos de tiempo a profundidad** utilizando herramientas de código abierto y reproducibles. La tesis demuestra que es posible realizar este proceso complejo de forma económica y eficiente, sin depender de costosos software comerciales.

**Autor:** Javier Nieto Baltazar  
**Institución:** Benemérita Universidad Autónoma de Puebla (BUAP)  
**Facultad:** Ingeniería  
**Programa:** Ingeniería Geofísica  
**Fecha:** Mayo 2018  
**Director de Tesis:** Sergio Chávez Pérez  


---

## 📚 Contenido Principal

### Capítulos

1. **Reproducibilidad Computacional en Representación Sísmica**
   - Introducción a la investigación reproducible
   - Importancia del código abierto en geociencias
   - Revisión de paqueterías de código abierto para sismología

2. **Conversión Tiempo a Profundidad de Datos Sísmicos**
   - Conceptos fundamentales
   - Importancia del modelo de velocidad
   - Tipos de velocidades en sísmica (instantánea, promedio, intervalo, RMS)
   - Herramientas computacionales utilizadas

3. **Herramientas Computacionales Implementadas**
   - **OpendTect** - Visualización e integración de datos sísmicos
   - **Madagascar** - Procesamiento y análisis de datos multidimensionales
   - **Seismic Unix** - Visualización y procesamiento de datos sísmicos

4. **Estimación de Velocidad de Intervalo**
   - Ecuación de Dix
   - Teoría de rayos paraxiales (Cameron et al., 2007)
   - Casos de estudio comparativos

5. **Discusión y Conclusiones**
   - Análisis de resultados
   - Ventajas de herramientas de código abierto
   - Recomendaciones para futuros trabajos

---

## 🔧 Herramientas y Tecnologías Utilizadas

### Software de Código Abierto

- **Madagascar** - Platform de análisis multidimensional y reproducibilidad
  - Comandos: `sftimetodepth`, `sfdepth2time`, `sfdix`, `sfcameron2d`
  - Documentación: http://www.ahay.org/wiki/Main_Page

- **OpendTect** - Suite para visualización e interpretación sísmica
  - Herramienta: Time to Depth Conversion
  - Documentación: http://doc.opendtect.org/

- **Seismic Unix** - Paquetería para procesamiento sísmico
  - Comandos: `suttoz`, `suztot`
  - Documentación: https://cwp.mines.edu/

### Lenguajes de Programación

- **Python** - Scripting y automatización
- **Bash** - Secuencias de comando en Linux

### Formato y Documentación

- **LaTeX** - Tipografía profesional
- **Markdown** - Este archivo

---

## 📊 Datos Utilizados

Los datos sísmicos y de velocidad proceden del **repositorio de datos libres de OpendTect**:
- **Ubicación:** Sector holandés del Mar del Norte
- **Cobertura:** Sísmica 3D comercial
- **Período Geológico:** Mioceno al Pleistoceno
- **Litología:** Paquete deltaico (arenas y lutitas)
- **Fuente:** https://www.opendtect.org/osr/

---

## 📁 Estructura del Proyecto

```
escrito_final_biblioteca_latex/
├── README.md                          # Este archivo
├── tesis.tex                          # Documento principal LaTeX
├── referencias.bib                    # Bibliografía
├── tesis-blx.bib                     # Archivo auxiliar bibliografía
├── tesis.pdf                          # PDF compilado
├── imagenes/                          # Figuras y gráficos
│   ├── logobuap                      # Logo de la universidad
│   ├── fig1                          # Paqueterías de código abierto
│   ├── tabla1                        # Comparación migración vs conversión
│   ├── sismicaoriginal_velocidad... # Datos sísmicos y velocidad
│   ├── imgttodOP_imgptot...         # Resultados OpendTect
│   ├── imgttodMA1D_imgdtot...       # Resultados Madagascar 1D
│   ├── velocidaddeintervalo2D       # Modelo 2D de velocidad
│   ├── imgttodMA2D_imgdtot...       # Resultados Madagascar 2D
│   ├── imgttodSU_imgdtot...         # Resultados Seismic Unix
│   ├── vintdix1d                    # Velocidad intervalo 1D
│   ├── ilustracionrayo...           # Conceptos teóricos
│   ├── combo1                       # Caso I (comparativa)
│   └── combo2                       # Caso II (comparativa)
├── tesis.aux                          # Archivo auxiliar LaTeX
├── tesis.toc                          # Tabla de contenidos
├── tesis.lof                          # Lista de figuras
├── tesis.lot                          # Lista de tablas
└── Extras/                            # Archivos SQL complementarios
    ├── crear-tablas.sql              # Creación de base de datos
    ├── crear-logs-tabla.sql          # Tabla de logs
    └── insertar-datos-ejemplo.sql    # Datos de ejemplo
```

---

## 🚀 Cómo Compilar el Documento

### Requisitos

- **TeX Live** o **MiKTeX** (distribución LaTeX completa)
- **BibLaTeX** (para gestión de bibliografía)
- **Pdflatex** o **XeLaTeX**

### En Windows (PowerShell)

```powershell
# Navegar a la carpeta del proyecto
cd "c:\Users\javi_\Downloads\escritos_finales\escritos_finales\escrito_final_biblioteca_latex"

# Compilar el documento (primera pasada)
pdflatex tesis.tex

# Procesar bibliografía
biber tesis

# Compilar nuevamente (segunda pasada)
pdflatex tesis.tex

# Compilar una tercera vez para actualizar referencias cruzadas
pdflatex tesis.tex
```

### En Linux/Mac

```bash
cd ~/Downloads/escritos_finales/escritos_finales/escrito_final_biblioteca_latex
pdflatex tesis.tex
biber tesis
pdflatex tesis.tex
pdflatex tesis.tex
```

---

## 📖 Resumen Ejecutivo

### Problemática

La conversión de datos sísmicos de tiempo a profundidad es un proceso crítico en exploración petrolera, pero generalmente se realiza con software comercial de alto costo, limitando el acceso a estudiantes, investigadores e industria pequeña.

### Solución Propuesta

Demostrar que herramientas de **código abierto y reproducibles** (Madagascar, OpendTect, Seismic Unix) pueden realizar esta conversión de forma confiable, económica y eficiente.

### Contribuciones Principales

1. **Reproducibilidad Computacional**: Documentación completa con código ejecutable
2. **Análisis Comparativo**: Evaluación de tres herramientas de código abierto
3. **Metodología Avanzada**: Implementación de rayos paraxiales para estimación de velocidad
4. **Accesibilidad**: Demostración en hardware de bajo costo (Intel Atom, 2GB RAM)

### Resultados Clave

- ✅ Conversión exitosa tiempo-profundidad con OpendTect
- ✅ Modelos de velocidad 1D y 2D con Madagascar
- ✅ Implementación con Seismic Unix
- ✅ Comparación: rayos paraxiales vs ecuación de Dix
- ✅ Reducción significativa de costos sin comprometer calidad

---

## 🔍 Conceptos Principales

### Conversión Tiempo a Profundidad

Transformación de datos sísmicos de dominio de tiempo a dominio de profundidad usando la relación fundamental:

$$Z = \frac{1}{2} \sum_{i=0}^{n} V_i (t_{i-1}-t_i)$$

Donde:
- **Z**: Profundidad
- **V_i**: Velocidad de intervalo
- **t**: Tiempo

### Tipos de Velocidad Sísmica

| Tipo | Definición | Uso |
|------|-----------|-----|
| **Instantánea** | Límite de velocidad media | Registros acústicos |
| **Promedio** | Suma de espesores / tiempo total | Análisis básico |
| **Intervalo** | Velocidad de formación específica | Conversión T-Z |
| **RMS (Dix)** | Promedio ponderado | Apilamiento NMO |
| **Apilamiento** | De análisis de velocidad | Corrección NMO |

---

## 📚 Bibliografía Principal

- Claerbout, J.F. (1985). Imaging the Earth's Interior
- Cameron, M., Fomel, S., & Sethian, J. (2007-2008). Time-to-depth conversion and seismic velocity estimation
- Robein, E. (2003). Velocities, Time-Imaging and Depth-imaging
- Fomel, S., Sava, P., et al. (2013). Madagascar: Open-source software project
- Sheriff, R.E. (2002). Encyclopedic dictionary of applied geophysics
- Yilmaz, O. (1987). Seismic Data Processing

---

## 💻 Códigos Incluidos

La tesis incluye códigos ejecutables en los apéndices:

### Apéndice A: Madagascar y Seismic Unix
- Conversión 1D con modelo sintético
- Conversión 2D con modelo sintético
- Comandos Seismic Unix

### Apéndice B: Estimación de Velocidad
- Caso I: Comparativa Dix vs Rayos Paraxiales
- Caso II: Aplicación a datos del Golfo de México

**Acceso Completo:** https://github.com/javibash

---

## 🎓 Agradecimientos

- **Director de Tesis:** Sergio Chávez Pérez
- **Asesor Interno:** José Castillo Román
- **Sinodales:** Luis Fernando Gómez Ceballos, José Serrano Ortíz
- **Institución:** Benemérita Universidad Autónoma de Puebla
- **Apoyo:** Instituto Mexicano del Petróleo

---

## 📞 Contacto

- **Email:** nieto.jb@gmail.com
- **GitHub:** https://github.com/javibash

---

## 📜 Licencia

Este documento es parte de una tesis académica de la BUAP. Se proporciona con fines educativos y de investigación.

---

## 🔗 Enlaces Útiles

- [Madagascar Official](http://www.ahay.org/wiki/Main_Page)
- [OpendTect Documentation](http://doc.opendtect.org/)
- [Seismic Unix](https://cwp.mines.edu/)
- [SEG Open Research](http://software.seg.org/)
- [GitHub del Autor](https://github.com/javibash)

---

**Última Actualización:** Noviembre 2025  
**Versión:** 1.0

