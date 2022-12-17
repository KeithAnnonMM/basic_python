class Worker:
    company = 'LBC'
    
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def getName(self):
        return self.name
    
    def get_worker_name(self):
        print('Worker name:',self.name)

    def getWorker_sector(self):
        print('No sector yet')

    def getPrefix(self):
        if self.gender.lower() == 'm'or self.gender.lower() == 'male':
            return 'He is'
        elif self.gender.lower() == 'f'or self.gender.lower() == 'female':
            return 'She is'
        else:
            return 'They are'
    

class Manager(Worker):

    def __init__(self,name,sector,gender):
        super().__init__(name,gender)
        self.sector = sector
        self.prefix = Worker.getPrefix(self)

    def getWorker_sector(self):
        print(self.prefix,'the manager of the',self.sector,'department')

class Hr(Manager):
    def __init__(self,name,sector,gender):
        super().__init__(name,sector,gender)
        self.prefix = Worker.getPrefix(self)

    def __init__(self,name,gender):
        self.name = name
        self.sector = 'HR'
        self.gender = gender
        self.prefix = Worker.getPrefix(self)

def getWorker(value):
    value.get_worker_name()
    print(value.getName(),'works for {}'.format(value.__class__.company))
    value.getWorker_sector()

class Cleaner(Worker):
    
    def __init__(self,name,sector,gender):
        super().__init__(name,gender)
        self.sector = sector
        self.prefix = Worker.getPrefix(self)


    def getWorker_sector(self):
        print(self.prefix,'part of the',self.sector,'department')
        


human_resource = Hr('Alex Rukundo','M')
cleaner = Cleaner('Diana Nakkidde','Bathroom Cleaning','F')
ceo = Manager('Mukanu Dennis','Technology','Mal')

workers = [human_resource,cleaner,ceo]
for worker in workers:
    getWorker(worker)