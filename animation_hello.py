from manim import *

class animation_hello(Scene):
    def construct(self):

        square = Square(color=BLUE)
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        circle = Circle(color=PINK)

        logo = Text("Hello ^^", color=BLUE)
        circle_logo = Circle(radius=10, color=PINK, )

        self.play(GrowFromCenter(square))
        self.play(Transform(square, circle))
        self.play(square.animate.scale(0.0))

        self.play(GrowFromCenter(circle_logo))
        self.play(GrowFromCenter(logo))

        self.wait()