import math
import random
import add

gap = 0.3
add.cube([0,0,0],1,[255,0,0])
add.cube([0,1+gap,0],0.7,[255,0,0])
add.cube2([1+gap,0,0],1,0.2,[255,255,0])
add.cube2([1+gap,1+gap,0],1,0.1,[255,255,0])
add.cube2([1+gap,2+2*gap,0],0.7,0.1,[255,255,0])
def saddle(u,v):
  x = 2+2*gap+u
  y = u*u*2 - v*v*2
  z = -v
  return ([x, y, z])
def torus(u,v):
  x = 2+2*gap+(0.5+0.2*math.cos(u))*math.cos(v)
  y = 1+gap+0.2*math.sin(u)
  z = (0.5+0.2*math.cos(u))*math.sin(v)
  return ([x, y, z])
def sphere(u,v):
  x = 2+2*gap+0.5*math.cos(u)*math.sin(v)
  y = 2+2*gap+0.5*math.cos(v)
  z = 0.5*math.sin(u)*math.sin(v)
  return ([x, y, z])
add.parametric(saddle,-0.5,0.5,20,-0.5,0.5,20,[0,255,0])
add.parametric(torus,0,2*math.pi,20,0,2*math.pi,80,[0,255,0])
add.parametric(sphere,0,2*math.pi,30,0,math.pi,30,[0,255,0])
add.sphere([3+3*gap,0,0],0.5,3,[255,0,255])
add.sphere([3+3*gap,1+1*gap,0],0.5,5,[255,0,255])
add.sphere([3+3*gap,2+2*gap,0],0.5,10,[255,0,255])
add.cone([4+4*gap,-0.5,0],[4+4*gap,0.5,0],0.5,20,[0,0,255])
add.cone([4+4*gap,1+1*gap,0.3],[4+4*gap,0.5+1+1*gap,-0.3],0.5,20,[0,0,255])
add.cone2([4+4*gap,-0.5,1+1*gap],[4+4*gap,0.5,1+1*gap],0.5,20,[0,0,255])
add.cone2([4+4*gap,1+1*gap,0.3+1+1*gap],[4+4*gap,0.5+1+1*gap,-0.3+1+1*gap],0.5,20,[0,0,255])
add.cylinder([5+5*gap,-0.5,0],[5+5*gap,0.5,0],0.5,20,[0,255,255])
add.cylinder([5+5*gap,1+1*gap,-0.3],[5+5*gap,0.5+1+1*gap,0.3],0.5,20,[0,255,255])
add.cylinder2([5+5*gap,-0.5,1+gap],[5+5*gap,0.5,1+gap],0.5,20,[0,255,255])
add.cylinder2([5+5*gap,1+1*gap,-0.3+1+gap],[5+5*gap,0.5+1+1*gap,0.3+1+gap],0.5,20,[0,255,255])
add.cylinder3([5+5*gap,-0.5,2+2*gap],[5+5*gap,0.5,2+2*gap],0.5,20,[0,255,255])
add.cylinder3([5+5*gap,1+1*gap,-0.3+2+2*gap],[5+5*gap,0.5+1+1*gap,0.3+2+2*gap],0.5,20,[0,255,255])

add.off('output.off')