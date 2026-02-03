from manim import *
import numpy as np

class waves(Scene):
    def construct(self):
        a= Axes(x_range=[-10, 10], y_range=[-5, 5])
        graph = a.plot(lambda x: np.sin(x)+np.cos(x/2)+np.sin(x*2)-np.cos(x*2),color=BLUE)
        
        s1= a.plot(lambda x: np.sin(x),color=RED)
        s2= a.plot(lambda x: np.cos(x/2),color=GREEN)
        s3= a.plot(lambda x: np.sin(x*2),color=YELLOW)
        s4= a.plot(lambda x: -np.cos(x*2),color=PURPLE)
        
        g=VGroup(s1, s2, s3, s4)
        
        text1 = Text("sin(x)+cos(x/2)+sin(x*2)-cos(x*2)", font_size=14)
        text2 = Text("sin(x), cos(x/2), sin(x*2), -cos(x*2)", font_size=14)
        self.add(text1.to_edge(UP))
        self.add(graph, a)
        self.add(text1.to_edge(UP))
        self.wait(1)
        self.play(ReplacementTransform(graph, g))
        self.remove(text1)
        self.add(text2.to_edge(DOWN))
        
        self.wait(2)
        
        #manim -p -qh waves.py waves   
        #for 1080p
        