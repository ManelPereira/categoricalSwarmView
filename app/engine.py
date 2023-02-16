import math
from category import BaseCategory
from particle import BaseParticle
import numpy as np
class BaseEngine:
    def __init__(self,num_particles,classes,config, canvas):

        self.canvas = canvas
        self.config = self.set_config(config)
        self.particle_count = num_particles
        self.particles = self._create_particles()
        self.categories = self.create_categories(classes)
        self.new_hours = True
    def set_canvas(self,canvas):
        self.canvas = canvas

    def set_config (self, config):
        default_config = {'radius':200, 'center':(0,0)}
        for key in default_config:
            if key not in config:
                config[key] = default_config[key]
        return config
    

    def _create_particles(self):
        canvas = self.canvas
        return [BaseParticle(self.config["center"],"red",3,canvas) for _ in range(self.particle_count)]

    def speed(self, speed):
        for particle in self.particles:
            particle.speed = speed

    def calculate_probability(self):
        probabilities = np.array([category.probability for category in self.categories])
        probabilities /= probabilities.sum()
        for particle in self.particles:
            category = np.random.choice(self.categories,p=probabilities)
            particle.move_to((category.x,category.y), category.color)
            particle.category = category
        #for particle in self.particles:
        for category in self.categories:
            category.sim_category = sum([p.category == category for p in self.particles])/len(self.particles)


    
    def update(self):
        self.handle_colisions()
        if self.new_hours:
            self.new_hours = False
            self.calculate_probability()
        for particle in self.particles:
            particle.update()
            particle.draw()
        for category in self.categories:
            category.draw()
        
        self.canvas.after(1, self.update)
    
    def handle_colisions(self):
        for p in self.particles:
            colisions = p.find_colisions(self.particles)
            for c in colisions:
                c.nudge_away_from(p)    

    def move_all_to(self,new_pos =(300,300), color="green"):
        for p in self.particles:
            p.move_to(new_pos, color)

    def create_categories(self,categories):
        #the x and y coordinates of each category are calculated using the formula:
        #x = center_x + radius * cos(angle)
        #y = center_y + radius * sin(angle)
        positions = len(categories)
        angle = 360/positions
        lst_cat = []
        canvas = self.canvas
        for i, (name,cat) in enumerate(categories.items()):
            current_angle = angle * i
            centerx, centery = self.config["center"]
            x = centerx + self.config["radius"] * math.cos(current_angle)
            y = centery + self.config["radius"] * math.sin(current_angle)

            cat = BaseCategory(name,cat,(x,y),canvas,BaseCategory.colors()[i])
            lst_cat.append(cat)
        return lst_cat
        



    
