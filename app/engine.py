import math
from category import BaseCategory
from particle import BaseParticle
import numpy as np
class BaseEngine:
    def __init__(self,num_particles,classes,config, canvas,debug=True):
        self.hours = 0
        self.minutes = -5
        self.canvas = canvas
        self.config = self.set_config(config)
        self.particle_count = num_particles
        self.debug=debug
        self.particles = self._create_particles()
        self.categories = self.create_categories(classes)
        self.new_hours = True
        self.timeid = self.canvas.create_text(50,50,anchor="nw",text=f"{int(self.hours)} hours",font=("Purisa", 14))
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
        particles = [BaseParticle(self.config["center"],"red",3,canvas) for _ in range(self.particle_count)]
        if(self.debug):
            y= 100
            self.particles_text = [self.canvas.create_text(50, y+15*i, anchor="nw", 
                        text=f"{p}", 
                        font=("Purisa", 10)) for i, p in enumerate(particles)]
            #self.particles_text = [self.canvas.create_text(50,y+10*i,anchor="nw",text=f"part {i}: ({p.x:.2f},{p.y:.2f}) speed: ({p.speed_x:.2f,p.speed_y:.2f}) acc: ({p.acc_x:.2f},{p.acc_x:.2f})",font=("Purisa", 12)) for i,p in enumerate(particles)]
        return particles
        

    def speed(self, speed):
        for particle in self.particles:
            particle.speed = speed

    def probability_generator(self,num_classes):
        probabilities = np.random.random(num_classes)
        probabilities /= probabilities.sum()
        return probabilities

    def calculate_probability(self):
        
        probabilities = self.probability_generator(len(self.categories))
        probabilities /= probabilities.sum()
        for particle in self.particles:
            category = np.random.choice(self.categories,p=probabilities)
            particle.move_to((category.x,category.y), category.color)
            particle.category = category
        #for particle in self.particles:
        for category in self.categories:
            category.sim_category = sum([p.category == category for p in self.particles])/len(self.particles)

    def draw_particle_debug(self):
        if(self.debug):
            for i,p in enumerate(self.particles):
                self.canvas.itemconfig(self.particles_text[i],text=f"{p}")


    def draw_hours(self):
        self.canvas.itemconfig(self.timeid,text=f"{int(self.hours)} hours")
    def update(self):
        self.hours += 1/120
        self.minutes += 1
        if(self.minutes%120 == 0):
            self.calculate_probability()

        self.draw_particle_debug()
        self.draw_hours()
        self.handle_colisions()
        for particle in self.particles:
            particle.update()
            particle.draw()
        for category in self.categories:
            category.draw()
        
        self.canvas.after(20, self.update)
    
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
            x = centerx + self.config["radius"] * math.cos(math.radians(current_angle))
            y = centery + self.config["radius"] * math.sin(math.radians(current_angle))

            cat = BaseCategory(name,cat,(x,y),canvas,BaseCategory.colors()[i])
            
            lst_cat.append(cat)
        return lst_cat
        



    
