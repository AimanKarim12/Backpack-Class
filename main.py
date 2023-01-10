# TASK 1
class Backpack:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False
    
    def openBag(self):
        self.open = True
        print("Backpack is now open.")
        
    def closeBag(self):
        self.open = False
        print("Backpack is now closed.")
        
    def putin(self, item):
        if self.open:
            self.items.append(item)
            print(f"{item} has been added to the backpack.")
        else:
            print("Backpack is closed. Please open it first.")
            
    def takeout(self, item):
        if self.open:
            if item in self.items:
                self.items.remove(item)
                print(f"{item} has been removed from the backpack.")
            else:
                print(f"{item} is not in the backpack.")
        else:
            print("Backpack is closed. Please open it first.")

# TASK 2
small_blue_backpack = Backpack("blue", "small")
medium_red_backpack = Backpack("red", "medium")
large_green_backpack = Backpack("green", "large")

# TASK 3
small_blue_backpack.openBag()
small_blue_backpack.putin("lunch")
small_blue_backpack.putin("jacket")
small_blue_backpack.closeBag()
small_blue_backpack.openBag()
small_blue_backpack.takeout("jacket")
small_blue_backpack.closeBag()