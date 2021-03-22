class Solution:
    stack = []
    queue = []
    
    def pushCharacter(self, data):
        self.stack.append(data)
        
    def enqueueCharacter(self, data):
        self.queue.insert(0, data)
        
    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        return self.queue.pop()
