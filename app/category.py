class BaseCategory:
    def __init__(self, name, probability,position,canvas,color):
        self._name = name
        self._probability = probability
        self._x = position[0]
        self._y = position[1]
        self.canvas = canvas
        self.color = color
        self._sim_category = probability
        self.item = self.canvas.create_text(self.x, self.y, anchor="n",fill=self.color,text= f"{self.name} ({int(self.sim_category*100)} %)",font=("Purisa", 14))
        #self.fence = self.canvas.create_oval(self.x-20, self.y-20, self.x+20, self.y+20, outline=self.color, width=3)
    
    def draw(self):
        pass
        #self.canvas.after(1, self.draw)

    
    x = property(lambda self: self._x,None,None,"Gets x")
    y = property(lambda self: self._y,None,None,"Gets y")
    def _set_sim_category(self, probability):
        self._sim_category = probability
        self.canvas.itemconfig(self.item, text= f"{self.name} ({int(self.sim_category*100)} %)")
    @classmethod
    def colors(cls,i=None):
        colors = ["navy","teal","aqua","red","green","blue","orange","purple","pink","brown","black","grey","cyan","magenta","gold","torquoise","olive","maroon"]

        if i is not None:
            return colors[i%len(colors)]
        else:
            return colors
        #add 20 different colors
        return ["navy","teal","aqua","red","green","blue","yellow","orange","purple","pink","brown","black","white","grey","cyan","magenta","gold","torquoise","olive","maroon"]
    name = property(lambda self: self._name,None,None,"Gets name")
    probability = property(lambda self: self._probability,None,None,"Gets probability")
    sim_category = property(lambda self: self._sim_category,_set_sim_category,None,"Gets sim_category")