class BareMinimumClass:
    pass

class Complex:
    def __init__(self, realpart, imagpart):
        """Constructor for Complex numbers"""
        
        self.r = realpart
        self.i = imagpart
        
    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i
        
    def __repr__(self):
        return '({},{})'.format(self.r, self.i)
        
        
class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)
    
    def receive_upvote(self):
        self.upvotes += 1
        
    def is_popular(self):
        return self.upvotes > 100
        




class Firearms:
    #General firearm class
    def __init__ (self, name, cal, country, sel=0):
        self.name = str(name)
        self.cal = float(cal)
        self.sel = sel
        self.country = str(country)
    #safety description   
    def selector_safety(self):
        self.sel = 0
        return 'Safety is on.'
        
        
    def selector_fire(self):
        self.sel = 1 
        return 'Semi'
        
    #info about firearm   
    def info(self):
        return (self.name, self.country, self.cal, self.sel)
        
class Rifles(Firearms):
    def __init__(self, name, cal, country, sel=0):
        super().__init__(name, cal, country, sel)
      
    #Rifles class has one extra parameter: selector can go to full auto position    
    def full_auto(self):
        self.sel = 2
        return 'Full auto'
    