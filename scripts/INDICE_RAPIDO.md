# Índice de Scripts - Resumen Rápido

## Archivos Generados

```
scripts/
├── README.md                                    (Este archivo - LEER PRIMERO)
├── 01_conversion_tiempo_profundidad_1D.py     (Madagascar - Modelo 1D)
├── 02_conversion_tiempo_profundidad_2D.py     (Madagascar - Modelo 2D)
├── 03_conversion_seismic_unix.sh              (Seismic Unix - Bash script)
├── 04_velocidad_paraxial_caso1.py             (Madagascar - Rayos paraxiales, Caso I)
├── 05_velocidad_paraxial_caso2.py             (Madagascar - Rayos paraxiales, Caso II)
└── INDICE_RAPIDO.md                           (Este archivo)
```

---

## 🎯 Guía Rápida de Selección

### ¿Cuál script debo usar?

**Si solo quiero conversión básica:**
→ Usar **03_conversion_seismic_unix.sh** (más simple, interfaz gráfica)

**Si quiero aprender Madagascar:**
→ Usar **01_conversion_tiempo_profundidad_1D.py** (código comentado, modelo simple)

**Si tengo estructuras complejas:**
→ Usar **02_conversion_tiempo_profundidad_2D.py** (modelo 2D con variación lateral)

**Si quiero comparar metodologías:**
→ Usar **04_velocidad_paraxial_caso1.py** (Dix vs Cameron, datos sintéticos)

**Si tengo datos reales complejos:**
→ Usar **05_velocidad_paraxial_caso2.py** (Datos del Golfo de México)

---

## 📝 Comparativa Rápida

| Script | Software | Modelo | Complejidad | Datos | Objetivo |
|--------|----------|--------|-------------|-------|----------|
| 01 | Madagascar | 1D | Baja | Sintéticos | Aprendizaje básico |
| 02 | Madagascar | 2D | Media | Sintéticos | Estructuras complejas |
| 03 | Seismic Unix | 1D | Baja | Cualquiera | Uso rápido/visual |
| 04 | Madagascar | 1D | Alta | Sintéticos | Investigación (metodologías) |
| 05 | Madagascar | 2D | Alta | Reales | Investigación (aplicación) |

---

## ⚡ Inicio Rápido

### Opción 1: Solo visualización (recomendado para principiantes)
```bash
# Editar parámetros en script
# Ejecutar
./03_conversion_seismic_unix.sh
```

### Opción 2: Análisis reproducible con Madagascar
```bash
# Instalar Madagascar
# Ejecutar
python 01_conversion_tiempo_profundidad_1D.py
scons
```

### Opción 3: Comparar metodologías
```bash
python 04_velocidad_paraxial_caso1.py
scons
# Buscar resultados en archivo "Fint" y "Fsis"
```

---

## 🔑 Conceptos Clave por Script

### 01 & 03: Conversión Básica
- **Ecuación:** $Z = \frac{1}{2} \sum V_i (t_{i-1} - t_i)$
- **Método:** Escalamiento simple
- **Velocidad:** Puntos discretos interpolados

### 02: Variación Lateral
- **Modelo:** 2D con buzamiento
- **Interpolación:** Spline 2D
- **Ventaja:** Captura heterogeneidades

### 04 & 05: Estimación de Velocidad
- **Dix:** Ecuación clásica (rápida, menos precisa)
- **Cameron:** Rayos paraxiales (lenta, más precisa)
- **Dispersión geométrica:** Corrección por lateralidad

---

## 📊 Datos de Entrada Requeridos

### Para scripts 01, 02, 03:
```
sismica.sgy (o sismica.su)
```

### Para scripts 04, 05:
```
Se descargan automáticamente del repositorio de Madagascar
- Caso 1: cmps-tp.HH
- Caso 2: beinew.HH
```

---

## 📤 Salidas Generadas

**Madagascar:** Archivos RSF + visualización .vpl
- Modelos de velocidad
- Secciones sísmicas
- Gráficos comparativos

**Seismic Unix:** Archivos SU + visualización interactiva
- Secciones en formato SU
- Ventanas gráficas interactivas

---

## 🛠️ Requisitos de Software

**Opción A: Usar todo**
```bash
# Linux
sudo apt install madagascar seismic-unix

# MacOS
brew install madagascar seismic-unix

# Windows
# Usar WSL2 + Linux o VirtualMachine
```

**Opción B: Solo Madagascar**
```bash
# Ejecutar scripts 01, 02, 04, 05
```

**Opción C: Solo Seismic Unix**
```bash
# Ejecutar script 03
# Más limitado pero funcional
```

---

## 🎓 Orden Recomendado de Estudio

### Principiante (1-2 semanas)
1. Leer README.md principal
2. Ejecutar 03_conversion_seismic_unix.sh
3. Modificar parámetros y observar cambios
4. Leer 01_conversion_tiempo_profundidad_1D.py

### Intermedio (2-4 semanas)
1. Ejecutar 01 completamente (análisis de código)
2. Ejecutar 02 con modelo 2D
3. Comparar resultados 1D vs 2D
4. Modificar velocidades y capas

### Avanzado (1-2 meses)
1. Ejecutar y analizar 04 (comparativa Dix vs Cameron)
2. Ejecutar y analizar 05 (datos reales)
3. Experimentar con parámetros de cameron2d
4. Implementar variaciones propias

---

## 🔗 Relación con la Tesis

| Capítulo | Apéndice | Script(s) |
|----------|----------|-----------|
| Cap 2 - Herramientas | A | 01, 02, 03 |
| Cap 3 - Estimación Velocidad | B | 04, 05 |

---

## 📞 Soporte

- **Documentación completa:** Ver README.md en carpeta scripts
- **Código comentado:** Todos los scripts tienen comentarios en español
- **Referencia completa:** Capítulos relevantes en tesis.tex

---

## ✅ Checklist de Verificación

Antes de ejecutar cualquier script:

- [ ] Software requerido instalado
- [ ] Datos de entrada disponibles
- [ ] Carpeta de trabajo correcta
- [ ] Permisos de escritura en carpeta
- [ ] Variables de entorno configuradas (para Madagascar/Seismic Unix)

---

**Última actualización:** Noviembre 2025  
**Versión:** 1.0
