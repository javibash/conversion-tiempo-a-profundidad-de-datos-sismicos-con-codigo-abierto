#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CONVERSIÓN TIEMPO A PROFUNDIDAD CON MODELO EN DOS DIMENSIONES
=============================================================
Script para conversión de datos sísmicos de tiempo a profundidad 
usando Madagascar con un modelo de velocidad sintético 2D.

Autor: Javier Nieto Baltazar
Instituto: BUAP - Ingeniería Geofísica
Año: 2018
"""

from rsf.proj import *
import string

# ==========================================
# CONFIGURACIÓN Y PARÁMETROS
# ==========================================

# Dimensiones del modelo
xmax = 23.75  # Extensión en X (km)
zmax = 2      # Extensión en Z (profundidad, km)

# Definir capas (profundidades en tiempo para cada posición x)
layers = ((0.05,0.05,0.05,0.05),
          (0.5,0.45,0.40,0.3),
          (0.8,0.55,0.45,0.31),
          (1.20,1.1,1.0,.80))

# Velocidades de intervalo para cada capa (km/s)
# Orden: más superficial a más profunda
velocities = (1.500,
              1.936,
              1.997,
              2.050,
              2.167)

def arr2str(array, sep=' '):
    """Convertir array a string"""
    return string.join(map(str, array), sep)

vstr = arr2str(velocities, ',')
n1 = len(layers[0])
n2 = len(layers)

# ==========================================
# CREAR MODELO DE VELOCIDAD 2D SINTÉTICO
# ==========================================

# Crear archivo ASCII con información de capas
Flow('layers.asc',None,
     '''
     echo %s
     n1=%d n2=%d o1=0 d1=%g
     data_format=ascii_float in=$TARGET     
     ''' % (string.join(map(arr2str, layers), ' '),
            n1, n2, xmax/(n1-1)))

Flow('layers', 'layers.asc', 'dd form=native')

# Parámetro de interpolación (no-redondo para reproducibilidad)
d = 0.0101

# Interpolar interfases sísmicas
Flow('refs','layers',
     'spline o1=0 d1=%g n1=%d' % (d, int(1.5+xmax/d)))

# Calcular buzamiento de interfaces
Flow('dips','refs','deriv scale=y')

# Crear modelo 2D de velocidad de intervalo
Flow('mod2D','refs',
     '''
     unif2 d1=%g n1=%d v00=%s 
     ''' % (d, int(1.5+zmax/d), vstr))

# Visualizar modelo de velocidad
Result('imgmod2D',
       'mod2D',
       '''
       window min1=.05 |
       grey color=j title="Modelo de velocidad de intervalo sintetico 2D"   
       titlesz=8 labelsz=6 scalarbar=y labelsz=6 bias=1
       label1="Profundidad" unit1="Km"
       label2="Distancia" unit2="Km"
       ''' )

# ==========================================
# CARGAR Y PROCESAR SECCIÓN SÍSMICA
# ==========================================

# Leer sección sísmica desde archivo SEG-Y
Flow('seis',
     'sismica.sgy',
     'segyread tfile=tfile1.rsf hfile=seis.asc bfile=seis.bin endian=y')

# Crear subsección sísmica
Flow('subseis', "seis" ,
'''
put n2=950  label2="Inline 2D" 
''')

# Visualizar sección en tiempo original
Result('subseis', 
'''
byte gainpanel=all |
grey title="Seccion en tiempo original"  label1="Tiempo" label2="Seccion longitudinal" unit1="s" labelsz=6
''')

# ==========================================
# CONVERSIÓN TIEMPO A PROFUNDIDAD
# ==========================================

# Aplicar conversión tiempo a profundidad con modelo 2D
Flow('ttod','subseis mod2D',
         '''
         time2depth  velocity=${SOURCES[1]} intime=n |
         put label1=Profundidad unit1=km
         ''')

# Visualizar resultado en profundidad
Result('imgttod', 'ttod',
       'window max1=1.8 | grey scalebar=n  labelsz=6 label1=Profundidad label2="Seccion longitudinal" unit1="Km" title="Seccion en profundidad"')

# ==========================================
# CONVERSIÓN PROFUNDIDAD A TIEMPO (VERIFICACIÓN)
# ==========================================

# Convertir de vuelta a tiempo para verificar
Flow('dtot','ttod mod2D',
         '''
         depth2time  velocity=${SOURCES[1]} intime=n |
         put label1=Tiempo unit1=s
         ''')

# Visualizar sección reconstruida en tiempo
Result('imgdtot','dtot','window max1=1.8 | grey scalebar=n labelsz=6 label1="Tiempo" label2="Seccion longitudinal" unit1="s" title="Seccion en tiempo reconstruida"')

End()
