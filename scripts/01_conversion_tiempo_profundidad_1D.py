#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CONVERSIÓN TIEMPO A PROFUNDIDAD CON MODELO EN UNA DIMENSIÓN
============================================================
Script para conversión de datos sísmicos de tiempo a profundidad 
usando Madagascar con un modelo de velocidad sintético 1D.

Autor: Javier Nieto Baltazar
Instituto: BUAP - Ingeniería Geofísica
Año: 2018
"""

from rsf.proj import *

# ==========================================
# CARGAR Y PROCESAR SECCIÓN SÍSMICA
# ==========================================

# Leer sección sísmica desde archivo SEG-Y
Flow('seis',
     'sismica.sgy',
     'segyread tfile=tfile1.rsf hfile=seis.asc bfile=seis.bin endian=y')

# Crear subsección sísmica con dimensiones específicas
Flow('subseis', "seis" ,
'''
put n2=950  label2="Inline 2D"  
''')

# Visualizar sección en tiempo original
Result('subseis', 
'''
byte gainpanel=all |
grey title="Seccion en tiempo original"  label1="Tiempo" unit1="s" label2="Seccion longitudinal" labelsz=6
''')

# ==========================================
# CREAR MODELO DE VELOCIDAD 1D
# ==========================================

# Definir puntos de velocidad RMS (tiempo en segundos, velocidad en km/s)
Flow('vrms.asc',None,
     '''
     echo
     0.05  1.500
     0.858 1.936
     1.026 1.977
     1.125 2.003
     1.848 2.167
    
     n1=2 n2=6 in=$TARGET
     data_format=ascii_float
     ''')

# Interpolar velocidad RMS desde puntos discretos
Flow('vrms','vrms.asc subseis',
     '''
     dd form=native |
     spline pattern=${SOURCES[1]}
     ''')

# ==========================================
# ESTIMAR VELOCIDAD DE INTERVALO
# ==========================================

# Calcular velocidad de intervalo usando ecuación de Dix
Flow('vintdix','vrms','dix rect1=50')

# Graficar comparación: velocidad RMS vs velocidad intervalo
Result('vintdix','vrms vintdix',
       '''
       cat axis=2 ${SOURCES[1]} |
       graph wanttitle=n dash=1,0
       label1=Tiempo unit1=s 
       label2=Velocidad unit2=km/s
       transp=n yreverse=n labelsz=6
       ''')

# ==========================================
# CONVERSIÓN TIEMPO A PROFUNDIDAD
# ==========================================

# Aplicar conversión tiempo a profundidad
Flow('ttoddix','subseis vintdix',
         '''
         time2depth  velocity=${SOURCES[1]} intime=n |
         put label1=Profundidad unit1=km
         ''')

# Visualizar resultado en profundidad
Result('imgttoddix','ttoddix','grey scalebar=n label1=Profundidad unit1="Km" label2="Seccion longitudinal" title="Seccion en profundidad" labelsz=6 ')

# ==========================================
# CONVERSIÓN PROFUNDIDAD A TIEMPO (VERIFICACIÓN)
# ==========================================

# Convertir de vuelta a tiempo para verificar
Flow('dtotdix','ttoddix vintdix',
         '''
         time2depth  velocity=${SOURCES[1]} intime=n |
         put label1=Tiempo unit1=s
         ''')

# Visualizar sección reconstruida en tiempo
Result('imgdtotdix','dtotdix','grey scalebar=n label1=Tiempo unit1="s" label2="Seccion longitudinal" title="Seccion en tiempo reconstruida" labelsz=6')

End()
