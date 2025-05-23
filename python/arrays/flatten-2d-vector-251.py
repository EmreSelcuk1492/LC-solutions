class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.rows = len(vec) 
        self.r_ptr = 0
        self.c_ptr = 0

    def find_int(self):
        while self.r_ptr < len(self.vec) and len(self.vec[self.r_ptr]) == 0:
            self.r_ptr +=1
            self.c_ptr = 0

    def next(self) -> int:
        self.find_int()
        res = self.vec[self.r_ptr][self.c_ptr]
        if len(self.vec[self.r_ptr]) - 1 == self.c_ptr:
            self.r_ptr += 1
            self.c_ptr = 0
        else:
            self.c_ptr += 1
        return res 

    def hasNext(self) -> bool:
        self.find_int()
        if len(self.vec) <= self.r_ptr:
            return False
        elif len(self.vec) - 1 == self.r_ptr and self.c_ptr > len(self.vec[self.r_ptr]) - 1:
            return False
        else:
            return True
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()

