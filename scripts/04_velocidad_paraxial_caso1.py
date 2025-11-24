#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ESTIMACIÓN DE VELOCIDAD DE INTERVALO USANDO RAYOS PARAXIALES - CASO I
=====================================================================
Script que compara dos metodologías para estimar velocidad de intervalo:
1. Ecuación de Dix (método clásico)
2. Rayos paraxiales (Cameron et al., 2007)

Análisis comparativo de resultados en conversión tiempo a profundidad.

Autor: Javier Nieto Baltazar
Instituto: BUAP - Ingeniería Geofísica
Año: 2018
"""

from rsf.proj import *

# ==========================================
# OBTENER DATOS
# ==========================================

# Descargar datos del repositorio de Madagascar
# Dataset: 'cmps-tp' del servidor 'blake'
Fetch('cmps-tp.HH', 'blake')

# ==========================================
# PREPARAR CONJUNTOS DE PUNTO MEDIO COMÚN (CMP)
# ==========================================

# Leer y preparar datos de CMP
Flow('cmps', 'cmps-tp.HH',
     'dd form=native | reverse which=2')

# Extraer un CMP individual para análisis detallado
Flow('cmp', 'cmps',
     '''
     window f3=950 n3=1 max1=6 |
     put o2=0.0 d2=1
     ''')

Plot('cmp',
     '''
     grey title="CMP gather" 
     unit1=s label2=Offset unit2=km labelsz=12
     ''')

# Extraer sección de offset cercano (near offset)
Result('noff', 'cmps',
       '''
       window n2=1 n3=1024 |
       grey title="Near Offset Section" 
       unit1=s label2=Distancia unit2=km label1=Tiempo labelsz=12
       ''')

# ==========================================
# PREPARAR MAPAS DE OFFSET
# ==========================================

Flow('off1', None, 'math n1=24 o1=0.4 d1=0.1  output=x1')
Flow('off2', None, 'math n1=24 o1=2.8 d1=0.05 output=x1')
Flow('off', 'off1 off2', 'cat axis=1 ${SOURCES[1]}')
Flow('offs', 'off', 'spray n=111')

# ==========================================
# ANÁLISIS DE VELOCIDAD (SEMBLANZA)
# ==========================================

vscan = '''
vscan offset=${SOURCES[1]} 
v0=1.4 nv=61 dv=0.005 half=n semblance=y
'''
pick = 'pick rect1=20 rect2=3 vel0=1.5'

# Realizar análisis de velocidad en un CMP
Flow('vscan', 'cmp off', vscan)
Plot('vscan',
     '''
     grey color=j allpos=y title="Velocity Scan" 
     unit1=s label2=Velocity unit2=km/s pclip=100 labelsz=12
     ''')

# Seleccionar velocidades máximas por semblanza
Flow('pick', 'vscan', pick)
Plot('pick0', 'pick',
     '''
     graph transp=y yreverse=y min2=1.4 max2=1.7 
     plotcol=7 plotfat=10 pad=n wanttitle=n wantaxis=n labelsz=12
     ''')
Plot('pick1', 'pick',
     '''
     graph transp=y yreverse=y min2=1.4 max2=1.7 
     plotcol=0 plotfat=1 pad=n wanttitle=n wantaxis=n labelsz=12
     ''')
Plot('vscan2', 'vscan pick0 pick1', 'Overlay')

# Análisis de velocidad para cada 10th CMP
Flow('vscans', 'cmps offs', 'window j3=10 | ' + vscan)

# Seleccionar velocidades
Flow('picks0', 'vscans', pick)

# Interpolar velocidades a la malla completa
Flow('picks', 'picks0',
     'transp | remap1 n1=1105 d1=0.05 o1=0 | transp')

Result('picks',
       '''
       grey color=j scalebar=y barreverse=y 
       allpos=n bias=1.47
       barlabel=Velocidad barunit=Km/s
       minval=1.5 maxval=1.7 labelsz=12
       title="Velocidad de apilamiento" 
       label1=Tiempo unit1=s label2=Distancia unit2=km
       ''')

# ==========================================
# NORMAL MOVEOUT (NMO) Y APILAMIENTO
# ==========================================

nmo = '''
nmo offset=${SOURCES[1]} 
velocity=${SOURCES[2]} half=n
'''

Flow('nmo', 'cmp off pick', nmo)
Plot('nmo',
     '''
     grey title="Normal Moveout" 
     unit1=s label2=Offset unit2=km labelsz=12
     ''')
Result('nmo', 'cmp vscan2 nmo', 'SideBySideAniso')

# Aplicar NMO y apilar todos los CMP
Flow('nmos', 'cmps off picks', nmo)
Flow('stack', 'nmos', 'stack')

Result('stack',
       '''
     
       grey title="Seccion apilada"  labelsz=12
       label1=Tiempo unit1=s label2=Distancia unit2=km
       ''')

# ==========================================
# ESTIMACIÓN DE VELOCIDAD - MÉTODO DIX
# ==========================================

# Seleccionar semblanza en picos de velocidad
Flow('semb', 'vscans picks0', 'slice pick=${SOURCES[1]}')

# Calcular velocidad de intervalo usando ecuación de Dix
Flow('vel0', 'picks0 semb',
     'dix rect1=20 rect2=2 weight=${SOURCES[1]}')

# Interpolar a la malla completa
Flow('vel', 'vel0',
     'transp | remap1 n1=1105 d1=0.05 o1=0 | transp')

Plot('vel',
       '''
       grey color=j scalebar=y barreverse=y 
       allpos=n bias=1.52 
       barlabel=Velocidad barunit=Km/s
       minval=1.4 maxval=1.7 labelsz=12
       title="Velocidad de intervalo por DIX" 
       label1=Profundidad unit1=km label2=Distancia unit2=km
       ''')

# Conversión tiempo a profundidad con modelo Dix
Flow('image', 'stack vel',
     '''
     time2depth velocity=${SOURCES[1]} 
     intime=y dz=0.005 nz=1001
     ''')

Plot('image',
       '''
       window n2=1024 min1=3 | grey title="Image with Dix" labelsz=12
       label1=Profundidad unit1=km label2=Distancia unit2=km
       ''')

# ==========================================
# ESTIMACIÓN DE VELOCIDAD - RAYOS PARAXIALES
# ==========================================

# Calcular velocidad de intervalo usando rayos paraxiales (Cameron 2007)
Flow('vcam', 'picks', ' transp | cameron2d method=cheb nz=11000 dz=.005  ')
Flow('vcam2', 'picks', 'cameron2d method=cheb nz=11000 dz=.005  ')

Plot('vcam',
       '''
       window max2=1.8 | grey color=j scalebar=y barreverse=y transp=n
       allpos=n bias=1.47
       barlabel=Velocidad barunit=Km/s
       minval=1.4 maxval=1.7 labelsz=12
       title="Velocidad de intervalo por Cameron" 
       label1=Distancia unit1=km label2=Profundidad unit2=km
              ''')

# Transponer y remapear
Flow('vcamt', 'vcam', 'transp')
Flow('vcam0', 'vcamt',
     'remap1 n1=625 d1=.004 o1=4')
Flow('vcam00', 'vcam0',
     'transp | remap1 n1=11000 d1=0.005 o1=0 | transp')

Result('vcam00',
       '''
       grey color=j scalebar=y barreverse=y transp=n
       bias=1.4 allpos=n labelsz=12
       title="Interval Velocity by Cameron" 
       label1=Profundidad unit1=km label2=Distancia unit2=km
              ''')

# Conversión tiempo a profundidad con modelo Cameron
Flow('imagecam', 'stack vcam2',
     '''
     time2depth velocity=${SOURCES[1]} 
     intime=y dz=0.005 nz=1001
     ''')

Plot('imagecam',
       '''
       window n2=1024 min1=3 | grey title="Seccion en profundidad con Cameron" labelsz=12
       label1=Profundidad unit1=km label2=Distancia unit2=km
       ''')

# ==========================================
# COMPARATIVAS
# ==========================================

# Comparar modelos de velocidad: Dix vs Cameron
Result('Fint', 'vel vcam', 'SideBySideAniso')

# Comparar secciones en profundidad: Dix vs Cameron
Result('Fsis', 'image imagecam', 'SideBySideAniso')

End()
