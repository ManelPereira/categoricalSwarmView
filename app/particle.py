import random
class BaseParticle:
    def __init__(self, pos, color, radius, canvas):
        self._color = color
        self.x = pos[0]
        self.y = pos[1]
        self.canvas = canvas
        self.radius = radius
        self.thickness = 3
        self.speed = 2
        top_leftx, top_lefty, bottom_rightx, bottom_righty = self.draw_info()
        self.item = self.canvas.create_oval(top_leftx, top_lefty, bottom_rightx, bottom_righty, fill=color, outline=self.color, width=self.thickness)
        self._category = None
    
    def _set_category(self, category):
        self._category = category
    category = property(lambda self: self._category,_set_category,None,"Gets category")
    def draw_info(self):
        return (self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius)

    def draw(self):
        top_leftx, top_lefty, bottom_rightx, bottom_righty = self.draw_info()
        #self.item = self.canvas.move(self.item,(self.x,self.y))

        #self.canvas.after(1, self.draw)

    def is_in_fence(self,pos, radius):
        return (self.x - pos[0])**2 + (self.y - pos[1])**2 < (self.radius + radius)**2

    def update(self):
        if not hasattr(self, 'new_pos') or self.is_in_fence(self.new_pos, 20) :
            return
        if(self.x < self.new_pos[0]):
            x_modifier = 1
        else:
            x_modifier = -1
        if(self.y < self.new_pos[1]):
            y_modifier = 1
        else:
            y_modifier = -1
        
        self.x += self.speed*x_modifier
        self.y += self.speed*y_modifier
        self.canvas.move(self.item, self.speed*x_modifier, self.speed*y_modifier)
        self.draw()
    
    def is_coliding(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2 < (self.radius + other.radius)**2 and self != other
    
    def find_colisions(self,others):
        return [other for other in others if self.is_coliding(other)]
    
    def move_to(self, new_pos, color):
        self.color = color
        self.new_pos = new_pos
    
    def nudge_away_from(self,other):
        diff = (self.x - other.x, self.y - other.y)
        self.x = self.x - diff[0] * random.uniform(0, 5)

        self.y = self.y - diff[1] * random.uniform(0, 5)


    def _set_color(self, color):
        self.canvas.itemconfig(self.item, fill=color, outline=color)
        self._color = color

    color = property(lambda self: self._color,_set_color,None,"Gets and sets color")
