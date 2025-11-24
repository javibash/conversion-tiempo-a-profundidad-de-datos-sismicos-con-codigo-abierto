#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ESTIMACIÓN DE VELOCIDAD DE INTERVALO USANDO RAYOS PARAXIALES - CASO II
=====================================================================
Script que compara dos metodologías para estimar velocidad de intervalo
aplicado a datos del Golfo de México (Gulf of Mexico):
1. Ecuación de Dix (método clásico)
2. Rayos paraxiales (Cameron et al., 2007)

Autor: Javier Nieto Baltazar
Instituto: BUAP - Ingeniería Geofísica
Año: 2018
"""

from rsf.proj import *

def Grey(data, other):
    """Función auxiliar para visualizar datos sísmicos"""
    Result(data, '''
    grey label2=Midpoint unit2="km" clip=1.84785e+06 label1=Time unit1="s" 
    title="" wherexlabel=t wanttitle=y wheretitle=b screenratio=1.4 max1=2.5 %s 
    ''' % other)

# ==========================================
# CARGAR Y PREPARAR DATOS
# ==========================================

# Descargar datos del Golfo de México
Fetch('beinew.HH', 'midpts')

# Preparar datos: convertir formato, añadir etiquetas
Flow('gulf', 'beinew.HH',
     '''
     dd form=native |
     put
     label1=Time unit1=s
     label2=Half-Offset unit2=km
     label3=Midpoint unit3=km | window f2=4
     ''')

# Visualizar datos en 3D
Result('gulf',
       '''
       window min1=0.5 max1=3.8 max2=1.5 |byte |
       transp plane=23 |
       grey3 flat=n frame1=500 frame2=160 frame3=3  
       title="Gulf of Mexico Data" point1=0.8 point2=0.8
       ''')

# ==========================================
# ANÁLISIS DE VELOCIDAD (SEMBLANZA)
# ==========================================

# Calcular análisis de velocidad
Flow('vscan-gulf', 'gulf',
     'vscan v0=1.5 dv=0.02 nv=51 semblance=y',
     split=[3, 250], reduce='cat')

Result('vscan-gulf',
       '''
       byte allpos=y gainpanel=all pclip=100 |
       transp plane=23 |
       grey3 flat=n frame1=750 frame2=100 frame3=25 
       label1=Time unit1=s color=j labelsz=12
       label3=Velocity unit3=km/s 
       label2=Midpoint unit2=km
       title="Velocity Scan (traditional)" point1=0.8 point2=0.8
       ''')

# ==========================================
# SELECCIONAR VELOCIDADES
# ==========================================

# Seleccionar velocidades por máxima semblanza
Flow('vnmo-gulf', 'vscan-gulf', 'pick rect1=5 rect2=5')

Result('vnmo-gulf',
     '''
     grey color=j allpos=n bias=1.4
     scalebar=y barreverse=y barunit=km/s barlabel=Velocidad
     minval=1.5 maxval=2.5 labelsz=12
     label2=Distancia unit2=km label1=Tiempo unit1=s
     title="Velocidad NMO" 
     ''')

# ==========================================
# NORMAL MOVEOUT (NMO) Y APILAMIENTO
# ==========================================

# Aplicar NMO
Flow('nmo-gulf', 'gulf vnmo-gulf', 'nmo velocity=${SOURCES[1]}')

# Apilar todos los CMP
Flow('stack-gulf', 'nmo-gulf', 'stack')

Result('stack-gulf',
       '''
       grey labelsz=12
       label2=Distancia unit2=km label1=Tiempo unit1=s
       title="Gulf of Mexico Data" point1=0.8 point2=0.8
       ''')

# ==========================================
# ESTIMACIÓN DE VELOCIDAD - MÉTODO DIX
# ==========================================

# Calcular velocidad de intervalo usando ecuación de Dix
Flow('vintdix', 'vnmo-gulf', 'dix rect1=10 rect2=10')

# Convertir a profundidad para visualización
Flow('vintdixd', 'vintdix vintdix', 'time2depth velocity=${SOURCES[1]} intime=y')

Plot('vintdixd',
'''
window max1=3.8 | grey color=j allpos=n bias=1.4
scalebar=y barreverse=y barunit="Km/s" labelsz=12
minval=1.5 maxval=2.5 barlabel=Velocidad
label2=Distancia label1=Profundidad unit1=Km
title="Velocidad de intervalo por DIX"
''')

# Conversión tiempo a profundidad con velocidad Dix
Flow('ttoddix', 'stack-gulf vintdixd',
'''
time2depth velocity=${SOURCES[1]} intime=n
''')

Plot('ttoddix',
'''
window max1=3.8 | grey
label2=Distancia unit2=Km label1=Profundidad unit1=km labelsz=12
title="Seccion sismica en profundidad utilizando Vintdix"
''')

# ==========================================
# ESTIMACIÓN DE VELOCIDAD - RAYOS PARAXIALES
# ==========================================

# Calcular velocidad de intervalo usando rayos paraxiales (Cameron 2007)
Flow('vintcam x0 t0', 'vnmo-gulf',
     'transp | cameron2d method=cheb nz=11000 dz=.005 | put label2=Profundidad unit2=Km')

Plot('vintcam',
'''
transp | window max1=3.8 | grey color=j allpos=n bias=1.4 
scalebar=y barreverse=y barunit=Km/s
minval=1.5 maxval=2.5 barlabel=Velocidad labelsz=12
label2=Distancia unit2=Km label1=Profundidad unit1=km
title="Velocidad de intervalo por Cameron"
''')

# Transponer para usar en time2depth
Flow('vintcam2', 'vintcam', 'transp')

# Conversión tiempo a profundidad con velocidad Cameron
Flow('ttodcam', 'stack-gulf vintcam2',
'''
time2depth velocity=${SOURCES[1]} intime=n
''')

Plot('ttodcam',
'''
window max1=3.8 | grey scalebar=n 
label2=Distancia unit2=Km label1=Profundidad unit1=km labelsz=12
title="Seccion sismica en profundidad utilizando Vintcam"
''')

# ==========================================
# ANÁLISIS DE RAYOS (OPCIONAL)
# ==========================================

# Generar rayos de imagen para visualización
Flow('vd x z', 'vintcam', 've2d nt=1000 dt=.004 x=${TARGETS[1]} z=${TARGETS[2]}')

Plot('rayos', 'x z',
     '''
     cmplx ${SOURCES[1]} | transp | window j2=10 |
     graph wanttitle=n yreverse=y labelsz=12
     plotcol=7 scalebar=y wantaxis=n
     bartype=v  
     ''')

Result('vintrayos', 'vintcam rayos', 'Overlay')

# ==========================================
# COMPARATIVAS
# ==========================================

# Comparar modelos de velocidad: Dix vs Cameron
Result('Fint', 'vintdixd vintcam', 'SideBySideAniso')

# Comparar secciones en profundidad: Dix vs Cameron
Result('Fsis', 'ttoddix ttodcam', 'SideBySideAniso')

End()
