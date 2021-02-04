from vpython import *

#Initial values
G=6.67e-11 
unitMass=7.348e22

rem=384.4e6

#Drawing bodies
mA=sphere(pos=vector(0,0,0), radius=rem, color=color.yellow, make_trail=False)
mB=sphere(pos=vector(15*rem, 0, 0), radius=rem/3, color=color.green, make_trail=False)
mC=sphere(pos=vector(15.5*rem, 0,0), radius=rem/5, color=color.cyan, make_trail=False)

mA.m=6000*unitMass
mB.m=100*unitMass
mC.m=0.055*unitMass

mA.p=mA.m*vector(0,0,0)
mB.p=mB.m*vector(0,-2000,0)
mC.p=mC.m*vector(0,-180,0)

#Creating center of mass
com=sphere(pos=(mB.m*mB.pos + mA.m*mA.pos)/(mB.m+mA.m), radius=rem/4, color=color.red, make_trail=True)

#Time steps scaled to be appropriate
t=0
dt=3600
tmax=24*dt*28

#Updating position values
while t<tmax*10:
  rate(500)
  rAB=mB.pos-mA.pos
  rAC=mC.pos-mA.pos
  rBC=mC.pos-mB.pos
  
  FAB=-G*mA.m*mB.m*norm(rAB)/mag(rAB)**2
  FAC=-G*mA.m*mC.m*norm(rAC)/mag(rAC)**2
  FBC=-G*mB.m*mC.m*norm(rBC)/mag(rBC)**2
  
  mA.p=mA.p+(-FAB-FAC)*dt
  mB.p=mB.p+(FAB-FBC)*dt
  mC.p=mC.p+(FAC+FBC)*dt
  
  mA.pos=mA.pos+mA.p*dt/mA.m
  mB.pos=mB.pos+mB.p*dt/mB.m
  mC.pos=mC.pos+mC.p*dt/mC.m
  
  com.pos=(mB.m*mB.pos + mA.m*mA.pos)/(mB.m+mA.m)
  
  t=t+dt
