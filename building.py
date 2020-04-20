import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, owner):
        self.owner = owner

    def output(self):
        story = ""
        if self.stories == 1:
            story = "story"
        else:
            story = "stories"
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} {story}.")

bigBuilding = Building("123 Main Street", 16)
bigBuilding.purchase("Matt")
bigBuilding.construct()
bigBuilding.output()

print("")

smallBuilding = Building("301 West Deer Park", 1)
smallBuilding.purchase("Bobby")
smallBuilding.construct()
smallBuilding.output()

print("")

mediumBuilding = Building("170 Hillcrest Rd", 2)
mediumBuilding.purchase("Karen")
mediumBuilding.construct()
mediumBuilding.output()