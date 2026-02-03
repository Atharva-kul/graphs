from manim import *
import numpy as np

class waves(ThreeDScene):
    def construct(self):
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=-145 * DEGREES, zoom=0.9)
        
        a= ThreeDAxes(x_range=[-10, 10], y_range=[-5, 5], z_range=[-5, 5], axis_config={"include_tip": True})
        x_label = a.get_x_axis_label(Text("x")).scale(0.7)
        y_label = a.get_y_axis_label(Text("y")).scale(0.7)
        z_label = a.get_z_axis_label(Text("z")).scale(0.7)
        self.add(x_label, y_label, z_label)
        
        graph = a.plot(lambda x: np.sin(x)+np.cos(x/2)+np.sin(x*2)-np.cos(x*2),color=BLUE)
        
        s1= a.plot(lambda x: np.sin(x),color=RED)
        s2= a.plot(lambda x: np.cos(x/2),color=GREEN)
        s3= a.plot(lambda x: np.sin(x*2),color=YELLOW)
        s4= a.plot(lambda x: -np.cos(x*2),color=PURPLE)
        
        g=VGroup(s1, s2, s3, s4)
        
        text1 = Text("sin(x)+cos(x/2)+sin(x*2)-cos(x*2)", font_size=28)
        text2 = Text("sin(x), cos(x/2), sin(x*2), -cos(x*2)", font_size=28)
        
        self.add(graph, a)
        self.add_fixed_in_frame_mobjects(text1.to_edge(UP, buff=0.5))
        self.wait(1)
        self.play(
            ReplacementTransform(graph, g),
            text1.animate.set_opacity(0),
            run_time=2
        )
        self.remove(text1)
        self.add_fixed_in_frame_mobjects(text2.to_edge(DOWN, buff=0.5))
        
        self.wait(2)
        
        #manim -p -qh waves.py waves   
        #for 1080p
        