import math
zonas_wifi=[['2.698','-76.680','63'],['2.724','-76.693','20'],['2.606','-76.742','680'],['2.698','-76.690','15']]
coordenadas= [[2.697,-76.681],[2.697, -76.741],[2.695, -76.691]]
latitud=float(coordenadas[0][0])
longitud=float(coordenadas[1][0])
r=6372.795477598
a=(latitud-float(zonas_wifi[0][0]))/2
b=math.cos(float(latitud))
f=a+b
c=math.cos(float(zonas_wifi[0][1]))
d=(longitud-float(zonas_wifi[1][0]))/2
e=math.sqrt(float(f*c*d))
dist_1= 2*float(r)*math.asin(e)
print(str(dist_1))
