import math
import random

# GLOBAL VARIABLES:
vertices = []
faces = []

def cube(c,e,RGB): # c - center, e - edge width, RGB - color
  global vertices, faces
  F = [[0,4,5,1],[0,1,3,2],[0,2,6,4],[1,5,7,3],[2,3,7,6],[4,6,7,5]]
  V = [[0,0,0],[0,0,e],[0,e,0],[0,e,e],[e,0,0],[e,0,e],[e,e,0],[e,e,e]] 
  for i in range (0,6):
    faces += ['4 '+str(F[i][0]+len(vertices))+' '+str(F[i][1]+len(vertices))+' '+str(F[i][2]+len(vertices))+
    ' '+str(F[i][3]+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  for j in range (0,8):
    vertices += [str(c[0]+V[j][0]-e/2)+' '+str(c[1]+V[j][1]-e/2)+' '+str(c[2]+V[j][2]-e/2)]

def rectangle3D(c,e,RGB): # c - center, e - width of edges, RGB - color
  global vertices, faces
  F = [[0,4,5,1],[0,1,3,2],[0,2,6,4],[1,5,7,3],[2,3,7,6],[4,6,7,5]]
  V = [[0,0,0],[0,0,e[2]],[0,e[1],0],[0,e[1],e[2]],[e[0],0,0],[e[0],0,e[2]],[e[0],e[1],0],[e[0],e[1],e[2]]] 
  for i in range (0,6):
    faces += ['4 '+str(F[i][0]+len(vertices))+' '+str(F[i][1]+len(vertices))+' '+str(F[i][2]+len(vertices))+
    ' '+str(F[i][3]+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  for j in range (0,8):
    vertices += [str(c[0]+V[j][0]-e[0]/2)+' '+str(c[1]+V[j][1]-e[1]/2)+' '+str(c[2]+V[j][2]-e[2]/2)]

def cylinder(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
  global vertices, faces
  for i in range (1,k):
    faces += ['4 '+str(2*i-2+len(vertices))+' '+str(2*i+len(vertices))+' '+str(2*i+1+len(vertices))+
    ' '+str(2*i-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['3 '+str(2*i+len(vertices))+' '+str(2*i-2+len(vertices))+' '+str(2*k+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['3 '+str(2*i-1+len(vertices))+' '+str(2*i+1+len(vertices))+' '+str(2*k+1+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['4 '+str(2*k-2+len(vertices))+' '+str(0+len(vertices))+' '+str(1+len(vertices))+
  ' '+str(2*k-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['3 '+str(0+len(vertices))+' '+str(2*k-2+len(vertices))+' '+str(2*k+len(vertices))+
  ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['3 '+str(1+len(vertices))+' '+str(2*k+1+len(vertices))+' '+str(2*k-1+len(vertices))+
  ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  if A[0]==B[0] and A[1]==B[1]:
    p1=-math.sqrt(2)*r/2
    p2=(B[2]-A[2])/abs(B[2]-A[2])*p1
    p3=-p1
    p4=p2
    p5=0
  else:
    d=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
    f=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2))
    p1=-r*(B[1]-A[1])/f
    p2=-r*(B[0]-A[0])*(B[2]-A[2])/(d*f)
    p3=r*(B[0]-A[0])/f
    p4=-r*(B[1]-A[1])*(B[2]-A[2])/(d*f)
    p5=r*f/d
  for i in range (1,k+1):
    sinn=math.sin(i/k*2*math.pi)
    coss=math.cos(i/k*2*math.pi)
    q1=coss*p1+sinn*p2
    q2=coss*p3+sinn*p4
    q3=sinn*p5
    vertices += [str(A[0]+q1)+' '+str(A[1]+q2)+' '+str(A[2]+q3)] + [str(B[0]+q1)+' '+str(B[1]+q2)+' '+str(B[2]+q3)]
  vertices += [str(A[0])+' '+str(A[1])+' '+str(A[2])] + [str(B[0])+' '+str(B[1])+' '+str(B[2])]

def cylinder2(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
  global vertices, faces
  for i in range (1,k):
    faces += ['4 '+str(2*i-2+len(vertices))+' '+str(2*i+len(vertices))+' '+str(2*i+1+len(vertices))+
    ' '+str(2*i-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['4 '+str(2*k-2+len(vertices))+' '+str(0+len(vertices))+' '+str(1+len(vertices))+
  ' '+str(2*k-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  if A[0]==B[0] and A[1]==B[1]:
    p1=-math.sqrt(2)*r/2
    p2=(B[2]-A[2])/abs(B[2]-A[2])*p1
    p3=-p1
    p4=p2
    p5=0
  else:
    d=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
    f=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2))
    p1=-r*(B[1]-A[1])/f
    p2=-r*(B[0]-A[0])*(B[2]-A[2])/(d*f)
    p3=r*(B[0]-A[0])/f
    p4=-r*(B[1]-A[1])*(B[2]-A[2])/(d*f)
    p5=r*f/d
  for i in range (1,k+1):
    sinn=math.sin(i/k*2*math.pi)
    coss=math.cos(i/k*2*math.pi)
    q1=coss*p1+sinn*p2
    q2=coss*p3+sinn*p4
    q3=sinn*p5
    vertices += [str(A[0]+q1)+' '+str(A[1]+q2)+' '+str(A[2]+q3)] + [str(B[0]+q1)+' '+str(B[1]+q2)+' '+str(B[2]+q3)]

def clear():
  global vertices, faces
  vertices = []
  faces = []

def off(mesh): # mesh - off file
  global vertices, faces
  file = open(mesh, 'w')
  file.write('%s\n%d %d %d\n' % ('OFF',len(vertices),len(faces),0))
  for i in range (len(vertices)):
    file.write('%s\n' % vertices[i])
  for j in range (len(faces)):
    file.write('%s\n' % faces[j])
  file.close()
  clear()

# Riedlentes deck'o matmenys    
deck_length = 22  # Ilgis
deck_width = 10  # Plotis
deck_height = 1
deck_color = [106,90,205]  # Ruda
deck_color_top = [30,40,50]    # Juoda
deck_height_top = 0.1

# Riedlentes centras
deck_center = [0, 0, 0]

# Sukuria riedlentes deck'a
for i in range(-deck_length//2, deck_length//2):
    for j in range(-deck_width//2, deck_width//2):
        # Sureguliuoja z koordinate, kad butu sukurta kreive
        z = deck_center[2] + (i / deck_length) ** 2 * deck_height
        # Sukeicia y ir z koordinates
        cube([deck_center[0] + i, z, deck_center[1] + j], deck_height, deck_color)
        
# Sukuria kitokios spalvos riedlentės deck'o griptape'a (uzdeda plona juoda sluoksni ant virsaus)
for i in range(-deck_length//2, deck_length//2):
    for j in range(-deck_width//2, deck_width//2):
        # Sureguliuoja z koordinatę, kad butu sukurta kreive
        z = deck_center[2] + (i / deck_length) ** 2 * deck_height
        # Sukeičia y ir z koordinates
        rectangle3D([deck_center[0] + i, z + deck_height + deck_height_top-0.5, deck_center[1] + j], [1, deck_height_top, 1], [30,40,50])

for i in range(0,10):
    rectangle3D([11+i*0.2, 0.3, -0.5], [1, 1, 10-i*0.9], deck_color)

for i in range (0,10):
    rectangle3D([-12-i*0.2, 0.8, -0.5], [1, 0.1, 10-i*0.9], deck_color_top)

for i in range(0,10):
    rectangle3D([-12-i*0.2, 0.3, -0.5], [1, 1, 10-i*0.9], deck_color)

for i in range(0,10):
    rectangle3D([11+i*0.2, 0.8, -0.5], [1, 0.1, 10-i*0.9], deck_color_top)

# Sujungia riedlentes skirtingas dalis
cylinder([-7,-3,3],[-7,-3,-4],0.7,100,[255, 255, 255])
cylinder([7,-3,-4],[7,-3,3],0.7,100,[255, 255, 255])

# Riedlentes ratu spalvos
wheel_color = [255, 253, 208]
out_wheel_color = [204, 204, 204]

# Priekiniai ratai
cylinder2([7, -3, -5], [7, -3, -4], 1.5, 100, out_wheel_color)
cylinder([7, -3, -4.8], [7, -3, -4], 1.45, 100, wheel_color)
cylinder2([7, -3, 4], [7, -3, 3], 1.5, 100, out_wheel_color)
cylinder([7, -3, 3.8], [7, -3, 3], 1.45, 100, wheel_color)

cylinder([7,-3,-5.1],[7,-3,-5],0.6,100,out_wheel_color)
cylinder([7,-3,4.1],[7,-3,4],0.6,100,out_wheel_color)

# Galiniai ratai
cylinder2([-7, -3, -5], [-7, -3, -4], 1.5, 100, out_wheel_color)
cylinder([-7, -3, 3.8], [-7, -3, 3], 1.45, 100, wheel_color)
cylinder2([-7, -3, 4], [-7, -3, 3], 1.5, 100, out_wheel_color)
cylinder([-7, -3, -4.8], [-7, -3, -4], 1.45, 100, wheel_color)

cylinder([-7,-3,-5.1],[-7,-3,-5],0.6,100,out_wheel_color)
cylinder([-7,-3,4.1],[-7,-3,4],0.6,100,out_wheel_color)


# Riedlentes priekis ir galas
rectangle3D([7,-0.2,-0.5], [4,0.7,3], [255, 255, 255])
rectangle3D([-7,-0.2,-0.5], [4,0.7,3], [255, 255, 255])

# 2 jungtys tarp deck'o ir ratu jungties (ilgas cilindras)
cylinder([6,0,-0.5],[7,-3,-2.5],0.5,100,[255, 255, 255])
cylinder([6,0,-0.5],[7,-3,1.5],0.5,100,[255, 255, 255])

cylinder([-6,0,-0.5],[-7,-3,-2.5],0.5,100,[255, 255, 255])
cylinder([-6,0,-0.5],[-7,-3,1.5],0.5,100,[255, 255, 255])

# 2 jungtys tarp deck'o ir ratu jungties (trumpas cilindras)
cube([6,-0.4,-0.5],1.8,[255, 255, 255])
cube([-6,-0.4,-0.5],1.8,[255, 255, 255])

# Issaugoja modeli i .off faila
off('modelis.off')