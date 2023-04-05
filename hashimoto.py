class hashimoto:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def printname(self):
        if(self.first):
            print("hashimoto")
        
        if(self.last):
            print("takuya")
        
    

sensei = hashimoto(True, True)

sensei.printname()

