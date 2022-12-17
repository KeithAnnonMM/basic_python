class Worker:
    def __init__(self,name):
        self.name = name
    
    def get_worker_name(self):
        print('Worker name:',self.name)

    def getWorker_sector(self):
        print('No sector yet')

class Manager(Worker):

    def __init__(self,name,sector):
        super().__init__(name)
        self.sector = sector

    def getWorker_sector(self):
        print(self.name,'is the manager of the',self.sector,'department')

class Hr(Manager):
    def __init__(self,name,sector):
        super().__init__(name,sector)

    def __init__(self,name):
        self.name = name
        self.sector = 'HR'

def getWorker(value):
    value.getWorker_sector()
    value.get_worker_name()

class Cleaner(Worker):
    def __init__(self,name,sector):
        super().__init__(name)
        self.sector = sector

    def getWorker_sector(self):
        print(self.name,'is part of the',self.sector,'department')
        


human_resource = Hr('Alex Rukundo')
cleaner = Cleaner('Diana Nakkidde','Bathroom Cleaning')
ceo = Manager('Mukanu Dennis','Technology')

workers = [human_resource,cleaner,ceo]
for worker in workers:
    getWorker(worker)