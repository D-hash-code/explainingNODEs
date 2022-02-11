# Quickstart Tutorial

Link: https://docs.manim.community/en/stable/tutorials/quickstart.html

- `Scene` is a Manim class used to generate video
- Use `.animate` to animate the `methods` used to transform the `mobjects`

> Most of the time, the code for scripting an animation is entirely contained within the construct() method of a Scene class. Inside construct(), you can create objects, display them on screen, and animate them.

Q: Does positioning a `mobject` come under defining it (the `mobject` definition), transforming it (the `method` definition) or animating it (the `animate` definition)?

I would assume the positioning is part of `mobject` definition as it defines a state? But I guess you could think about positioning in the context of changing states (so under transformation). Maybe I'm overthinking this 🙇

> When you prepend .animate to any method call that modifies a Mobject, the method becomes an animation which can be played using self.play

> When using .animate, Manim actually takes a Mobject’s starting state and its ending state and interpolates the two

Ofcourse one can arrive from one state to another state in various ways. And so the way animate delivers this change of state may not be exactly as expected.

Consider rotating a square 360 degrees. The initial and final states are identical 👯. If you simply call animate on these states [it collapses and expands the squares](https://docs.manim.community/en/stable/tutorials/quickstart.html) (see the last video on this page). To instead rotate the squares you need to use the Manim `Rotate()` function. Wonder what's going on under the hood with that function 🧐
