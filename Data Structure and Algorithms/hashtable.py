class Hashtable:
    
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, data):

        index = self.hashfunc(key)                                   #returns the index

        while self.keys[index] is not None:                          #checks if it is already occupied(COLLISION)
            if self.keys[index] == key:                              #there is a key with the same key as this one
                self.values[index] = data                            #overwrites the new value in self.values
                return

            index = (index+1)%self.size                              #moves to the next index

        self.keys[index] = key                          
        self.values[index] = data                                    #saves the data in self.values[index]

    def get(self, key):
        
        index = self.hashfunc(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index+1)%self.size                              #moves to the next index

        return None

    def hashfunc(self, key):
        sum = 0
        for p in range(len(key)):
            sum+=ord(key[p])                                         #ord() calculates the ASCII value of this key

        return sum%self.size                                         #remainder of this will be the index that will be returned

t = Hashtable()
t.put("apple",10)

print(t.get("apple"))