#!/bin/bash
# ================================================================
# CONVERSIÓN TIEMPO A PROFUNDIDAD CON SEISMIC UNIX
# ================================================================
# Script para conversión de datos sísmicos usando Seismic Unix
# 
# Autor: Javier Nieto Baltazar
# Instituto: BUAP - Ingeniería Geofísica
# Año: 2018
# ================================================================

# ==========================================
# PREPARAR DATOS
# ==========================================

# Extraer un inline 2D específico del volumen 3D original
# window: limita a los primeros 850 trazas
suwind < sismica.su key=tracr min=1 max=850 > inline.su

# Visualizar sección en tiempo original
echo "Visualizando sección en tiempo original..."
suximage < inline.su title="Seccion en tiempo"

# ==========================================
# PARÁMETROS DE VELOCIDAD
# ==========================================
# Estos valores representan:
# t = tiempos en segundos
# v = velocidades de intervalo en km/s

# Tiempos (segundos)
# 0.05,  0.858,  1.026,  1.125
#
# Velocidades (km/s)
# 1.5,   1.960,  2.175,  2.260

# ==========================================
# CONVERSIÓN TIEMPO A PROFUNDIDAD
# ==========================================

echo "Ejecutando conversión tiempo a profundidad..."

# suttoz: convierte de tiempo a profundidad
# Parámetros:
#   t = tiempos en segundos (donde se conoce la velocidad)
#   v = velocidades de intervalo en km/s
suttoz < inline.su \
    t=0.05,0.858,1.026,1.125 \
    v=1.5,1.960,2.175,2.260 \
    > inlined.su

# Visualizar sección convertida a profundidad
echo "Visualizando sección convertida a profundidad..."
suximage < inlined.su title="Seccion de tiempo a profundidad"

# ==========================================
# CONVERSIÓN PROFUNDIDAD A TIEMPO (VERIFICACIÓN)
# ==========================================

echo "Ejecutando conversión profundidad a tiempo (verificación)..."

# suztot: convierte de profundidad a tiempo
# Parámetros:
#   z = profundidades en km (donde se conoce la velocidad)
#   v = velocidades de intervalo en km/s
suztot < inlined.su \
    z=.0037,.0830,1.012,1.5 \
    v=1.5,1.960,2.175,2.260 \
    > inliner.su

# Visualizar sección reconstruida en tiempo
echo "Visualizando sección reconstruida en tiempo..."
suximage < inliner.su title="Seccion de profundidad a tiempo"

echo "Proceso completado!"
echo "Archivos generados:"
echo "  - inline.su: Sección en tiempo original"
echo "  - inlined.su: Sección convertida a profundidad"
echo "  - inliner.su: Sección reconstruida en tiempo"
