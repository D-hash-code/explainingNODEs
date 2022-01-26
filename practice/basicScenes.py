from manim import *

# Primary feature of manim: ability to implement complicated and mathematically intensive animations
# Such as interpolating between two geometric shapes

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square,circle))
        self.play(FadeOut(square))


class CreateCircle(Scene):
    def construct(self):

        circle = Circle()
        circle.set_fill(BLUE,opacity=0.5)

        self.play(Create(circle))
        self.play(Create(circle))


#Positioning MObjects

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE,opacity=0.5)

        square.next_to(circle, RIGHT, buff=2)
        #In terms of timing it seems that everything that happens at the same time in a scene needs to be time
        #in a scene needs to placed in the same self.play() operation
        #I wonder what the general breakdown of "movement" types are. To list a few; transform, create, ...
        self.play(Create(square),Create(circle))