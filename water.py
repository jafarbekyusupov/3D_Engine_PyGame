import numpy as np
import pygame as pg
from matrix_functions import *
from object_3d import Object3D
import time

class Water(Object3D):
    def __init__(self, render, width=20, height=20, resolution=20):
        # gen grid mesh for water
        vertexes = []
        faces = []
        
        # create vertices
        for z in range(resolution + 1):
            for x in range(resolution + 1):
                # normalize coords
                nx = (x / resolution) * width - width / 2
                nz = (z / resolution) * height - height / 2
                # flat surface (y=0)
                vertexes.append([nx, 0, nz, 1])
        
        # create faces (triangles)
        for z in range(resolution):
            for x in range(resolution):
                # calc vertex indices
                i = z * (resolution + 1) + x
                # two triangles per cell
                faces.append([i, i + 1, i + resolution + 1])
                faces.append([i + 1, i + resolution + 2, i + resolution + 1])
        
        # init parent class
        super().__init__(render, vertexes, faces)
        
        # save orig positions
        self.original_vertexes = np.copy(self.vertexes)
        self.resolution = resolution
        
        # wave params
        self.time = 0
        self.wave_speed = 0.03
        self.wave_height = 0.2
        
        # blue color
        water_color = pg.Color(64, 164, 223, 150)
        self.color_faces = [(water_color, face) for face in self.faces]
        
        # don't auto-rotate
        self.movement_flag = False

    def update(self):
        # time increment
        self.time += self.wave_speed
        
        # update vertex pos
        for i, vertex in enumerate(self.vertexes):
            # get orig x,z
            x, _, z, _ = self.original_vertexes[i]
            
            # calc waves
            wave1 = math.sin(x * 0.5 + self.time) * self.wave_height
            wave2 = math.sin(z * 0.3 + self.time * 0.7) * self.wave_height * 0.5
            wave3 = math.sin((x * 0.2 + z * 0.3) * 0.5 + self.time * 1.2) * self.wave_height * 0.3
            
            # update height
            self.vertexes[i][1] = wave1 + wave2 + wave3

    def draw(self):
        # update waves
        self.update()
        # parent draw
        super().draw()
