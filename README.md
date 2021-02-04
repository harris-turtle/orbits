# orbits
Visualization of different orbital systems
## Basic star-planet system
A basic approximation made in many basic orbital models is assuming the body being oribted, usually a star, is many order of magnitudes more massive than the orbiting body. This leads to simpler calculations since the center body is too massive to be accelerated a noticable amount and assumed stationary. Below is a visualization of this scenario.

<a href="https://i.imgur.com/8NwyCOw.gif"><img src="https://i.imgur.com/8NwyCOw.gif" title="Basic"/></a>

In systems like this there is a specific tangential velocity for the orbiting body depending on its distance from the center body that provides it a circular orbit. The more the velocity varys from that above or below causes the orbit to become a more eccentric ellipse with the center body as one foci. A special case exists when the velocity increases to escape velocity or greater creating a hyperbolic trajectory. 
## Accounting for the force on both bodies
If we take into account the force on both bodies since the acceleration of the big body is no longer negligible, we realize that they both orbit their shared center of mass as seen below. The center of mass is represented with the red sphere.

<a href="https://i.imgur.com/2qQy1rX.gif"><img src="https://i.imgur.com/2qQy1rX.gif" title="2 real bodies"/></a>

Since the net momentum of the two body system is towards the right, the center of mass moves in that direction. Despite that, both bodies are orbiting around this center.
## Binary star system
Just thought it would look cool seeing to stars orbit around each other. In this case because of symmetry the net momentum is zero meaning the center of mass stays constant.

<a href="https://i.imgur.com/Xu5fCIz.gif"><img src="https://i.imgur.com/Xu5fCIz.gif" title="Binary Stars"/></a>

## Three body problem
In the previous examples there was only two bodies, when we try to analyze more something stranges happens. The two-body systems all have analytic solutions that can be derived. That means there are equations where you can put in the initial conditions and time to recive a solution to where the bodies will be. At three bodies or more these analytic solutions are very rare and only work for a few very specific situations. That means most systems like our solar system, and even just the Sun, Earth, Moon system require computational methods to solve. These kinds of systems tend to also be chaotic meaning small changes to initial conditions leads to a completly different outcome much later in time. Since we can only measure so much percision even our own model for the solar system will diverge heavily from reality in large time scales. Thankfully in human scales it appears to be stable. 

## Sun, Earth, Moon system
Just for fun here is a simple approximation of the Sun, Earth, Moon system.

<a href="https://i.imgur.com/682SqbT.gif"><img src="https://i.imgur.com/682SqbT.gif" title="Sun, Earth, Moon"/></a>
