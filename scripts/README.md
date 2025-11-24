# Scripts de Conversión Tiempo a Profundidad

Colección de scripts ejecutables extraídos de los Apéndices A y B de la tesis:
**"Reproducibilidad Computacional para Conversión Tiempo a Profundidad de Datos Sísmicos"**

Autor: Javier Nieto Baltazar  
Instituto: BUAP - Ingeniería Geofísica  
Año: 2018

---

## 📋 Índice de Scripts

### 1. **01_conversion_tiempo_profundidad_1D.py**
**Madagascar - Modelo 1D de Velocidad**

Conversión tiempo a profundidad usando un modelo sintético de velocidad en una dimensión.

**Características:**
- Interpolación de velocidad RMS desde puntos discretos
- Cálculo de velocidad de intervalo mediante ecuación de Dix
- Conversión tiempo → profundidad → tiempo
- Visualización comparativa

**Comandos Madagascar utilizados:**
- `sftimetodepth` - Conversión tiempo a profundidad
- `sfdepth2time` - Conversión profundidad a tiempo
- `sfdix` - Ecuación de Dix

**Entrada requerida:**
- `sismica.sgy` - Archivo de datos sísmicos en formato SEG-Y
- `tfile1.rsf`, `seis.asc`, `seis.bin` - Archivos de configuración para leer SEG-Y

**Salida:**
- `imgttoddix.vpl` - Sección en profundidad
- `imgdtotdix.vpl` - Sección reconstruida en tiempo
- `vintdix.vpl` - Gráfica de velocidades (RMS vs Intervalo)

---

### 2. **02_conversion_tiempo_profundidad_2D.py**
**Madagascar - Modelo 2D Sintético de Velocidad**

Conversión tiempo a profundidad usando un modelo sintético 2D que respeta las variaciones laterales de velocidad.

**Características:**
- Creación de modelo sintético 2D con 4 capas
- Velocidades: 1.500, 1.936, 1.997, 2.050, 2.167 km/s
- Interpolación 2D para generar volumen de velocidad completo
- Conversión bidireccional (T→Z→T)
- Mejor reproducción de reflectores comparado con 1D

**Conceptos matemáticos:**
- Interpolación spline para interfases
- Método `unif2` para crear modelo 2D uniforme
- Extensión lateral de velocidad con buzamiento

**Entrada requerida:**
- `sismica.sgy` - Datos sísmicos
- Parámetros de capas predefinidos en el script

**Salida:**
- `imgmod2D.vpl` - Visualización del modelo de velocidad 2D
- `imgttod.vpl` - Sección convertida a profundidad
- `imgdtot.vpl` - Sección reconstruida en tiempo

**Ventajas sobre 1D:**
- Captura variaciones laterales de velocidad
- Menor error en reposicionamiento de reflectores
- Más realista para estructuras complejas

---

### 3. **03_conversion_seismic_unix.sh**
**Seismic Unix - Conversión Interactiva**

Script bash para conversión tiempo a profundidad usando herramientas de Seismic Unix.

**Características:**
- Interfaz de línea de comandos simple
- Acepta velocidades puntuales e interpola internamente
- Visualización interactiva con `suximage`
- Mejor para usuarios sin experiencia en programación

**Comandos Seismic Unix utilizados:**
- `suwind` - Seleccionar trazas específicas
- `suttoz` - Conversión tiempo a profundidad
- `suztot` - Conversión profundidad a tiempo
- `suximage` - Visualización interactiva

**Parámetros de ejemplo:**
```
Tiempos:     0.05, 0.858, 1.026, 1.125 (segundos)
Velocidades: 1.5, 1.960, 2.175, 2.260 (km/s)
```

**Entrada requerida:**
- `sismica.su` - Datos sísmicos en formato SU

**Salida:**
- `inline.su` - Sección extraída en tiempo
- `inlined.su` - Sección convertida a profundidad
- `inliner.su` - Sección reconstruida en tiempo

**Ventajas:**
- Más simple de usar
- Sin necesidad de scripting avanzado
- Interactividad visual

---

### 4. **04_velocidad_paraxial_caso1.py**
**Madagascar - Estimación de Velocidad con Rayos Paraxiales (Caso I)**

Comparación de dos metodologías para estimar velocidad de intervalo:
- Ecuación de Dix (clásica)
- Rayos Paraxiales (Cameron et al., 2007)

**Dataset:** `cmps-tp.HH` del repositorio de Madagascar

**Flujo de procesamiento:**
1. Análisis de velocidad (semblanza)
2. Selección de velocidades NMO
3. Corrección por Normal Moveout (NMO)
4. Apilamiento de trazas
5. Estimación de velocidad intervalo:
   - **Método Dix:** Ecuación clásica (3.1)
   - **Método Cameron:** Rayos paraxiales con dispersión geométrica

**Comandos Madagascar principales:**
- `vscan` - Análisis de velocidad
- `pick` - Selección automática de velocidades
- `nmo` - Corrección Normal Moveout
- `dix` - Ecuación de Dix
- `cameron2d` - Rayos paraxiales
- `time2depth` - Conversión tiempo a profundidad

**Comparativas generadas:**
- Modelos de velocidad (Dix vs Cameron)
- Secciones sísmicas en profundidad
- Diferencias en reposicionamiento de reflectores

**Resultados observables:**
- Dix: Mayor contraste de velocidades, menos suave
- Cameron: Distribución más uniforme, mejor resolución de cambios sutiles

---

### 5. **05_velocidad_paraxial_caso2.py**
**Madagascar - Estimación de Velocidad con Rayos Paraxiales (Caso II)**

Aplicación de metodologías de estimación de velocidad a datos reales del Golfo de México.

**Dataset:** `beinew.HH` - Datos del Golfo de México

**Características especiales:**
- Datos 3D reales de exploración petrolera
- Mayor volumen de datos
- Procesamiento con `split-reduce` para paralelización
- Visualización 3D de volúmenes de velocidad

**Flujo de procesamiento:**
1. Carga y preparación de datos 3D
2. Análisis de velocidad 3D
3. Selección de velocidades NMO
4. Apilamiento 3D
5. Comparación Dix vs Cameron

**Comparativas:**
- Modelos de velocidad 2D extraídos
- Secciones sísmicas en profundidad
- Visualización de rayos de imagen (opcional)

**Diferencias con Caso I:**
- Datos reales vs sintéticos
- Mayor complejidad geológica
- Mejor demostración de ventajas de rayos paraxiales

---

## 🚀 Cómo Ejecutar los Scripts

### Requisitos

**Para scripts de Madagascar (01, 02, 04, 05):**
```bash
# Instalar Madagascar
# Linux: sudo apt-get install madagascar
# MacOS: brew install madagascar
# Windows: Usar WSL o virtual machine

# Verificar instalación
sfmath --version
```

**Para script de Seismic Unix (03):**
```bash
# Instalar Seismic Unix
# Desde: https://cwp.mines.edu/cwpcodes/

# Verificar instalación
suximage --version
```

### Ejecución

**Scripts de Madagascar:**
```bash
# Navegar a carpeta del proyecto
cd path/to/project

# Ejecutar script (genera resultados automáticamente)
scons -c                    # Limpiar resultados previos
python 01_conversion_tiempo_profundidad_1D.py
scons                       # Ejecutar flujo de trabajo

# Ver resultados
sfpen image.vpl             # Visualizar con Pen
```

**Script de Seismic Unix:**
```bash
# Hacer ejecutable
chmod +x 03_conversion_seismic_unix.sh

# Ejecutar
./03_conversion_seismic_unix.sh

# Los resultados se visualizarán automáticamente
```

---

## 📊 Estructura de Datos

### Formatos

- **RSF** - Madagascar native format (archivos binarios + headers)
- **SU** - Seismic Unix format (trazas con headers)
- **SEG-Y** - Formato estándar de la industria
- **ASCII** - Texto plano para puntos de velocidad

### Variables sísmicas típicas

| Variable | Símbolo | Unidad | Rango típico |
|----------|---------|--------|--------------|
| Tiempo | t | segundos (s) | 0 - 6 |
| Profundidad | z | kilómetros (km) | 0 - 3 |
| Velocidad intervalo | V_int | km/s | 1.5 - 3.0 |
| Velocidad RMS | V_rms | km/s | 1.4 - 2.5 |
| Offset | h | kilómetros (km) | 0 - 2 |
| Midpoint | x | kilómetros (km) | Variable |

---

## 🔍 Parámetros Clave

### Velocidades en ejemplos

**Modelo 1D/Seismic Unix:**
- 0.05s → 1.500 km/s
- 0.858s → 1.936 km/s
- 1.026s → 1.977 km/s
- 1.125s → 2.003 km/s

**Modelo 2D sintético:**
- Capa 1: 1.500 km/s (superficial)
- Capa 2: 1.936 km/s
- Capa 3: 1.997 km/s
- Capa 4: 2.050 km/s
- Capa 5: 2.167 km/s (profunda)

**Golfo de México:**
- Rango: 1.5 - 2.5 km/s
- Variación lateral significativa

---

## 📚 Referencias Bibliográficas

Implementados en estos scripts:

1. **Claerbout, J.F.** (1985). Imaging the Earth's Interior
2. **Cameron, M., Fomel, S., & Sethian, J.** (2007-2008). Time-to-depth conversion and seismic velocity estimation using time-migration velocity
3. **Dix, C.H.** (1955). Seismic velocities from surface measurements
4. **Yilmaz, O.** (1987). Seismic Data Processing
5. **Stockwell, J.W. & Cohen, J.K.** (2002). The new SU user's manual

---

## 💡 Recomendaciones de Uso

### Para principiantes:
- Comenzar con **03_conversion_seismic_unix.sh** (más simple)
- Luego **01_conversion_tiempo_profundidad_1D.py** (modelo básico)

### Para análisis avanzado:
- Usar **02_conversion_tiempo_profundidad_2D.py** para modelos complejos
- Comparar resultados con **04_velocidad_paraxial_caso1.py** y **05_velocidad_paraxial_caso2.py**

### Para investigación:
- Modificar parámetros en scripts Madagascar
- Experimentar con diferentes métodos de interpolación
- Comparar resultados Dix vs Cameron

---

## ⚙️ Personalización

### Cambiar velocidades
En scripts de Madagascar, editar arrays:
```python
velocities = (1.500, 1.936, 1.997, 2.050, 2.167)
```

En Seismic Unix, editar parámetros:
```bash
t=0.05,0.858,1.026,1.125
v=1.5,1.960,2.175,2.260
```

### Cambiar datos de entrada
- Reemplazar `sismica.sgy` con tu propio archivo
- Ajustar parámetros `n2=950` según número de trazas
- Modificar tiempos mínimo/máximo según datos

---

## 📞 Contacto

- **Email autor:** nieto.jb@gmail.com
- **GitHub:** https://github.com/javibash

---

## 📄 Licencia

Scripts de código abierto de tesis académica. Uso libre para fines educativos y de investigación.

**Referencia:** Nieto Baltazar, J. (2018). Reproducibilidad Computacional para Conversión Tiempo a Profundidad de Datos Sísmicos. BUAP.

---

**Versión:** 1.0  
**Última actualización:** Noviembre 2025
