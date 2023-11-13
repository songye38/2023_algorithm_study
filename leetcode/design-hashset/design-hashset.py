class MyHashSet:

    bucket_size = 100

    def __init__(self):
        self.bucket = [[] for _ in range(100)]
        

    def add(self, key: int) -> None:
        index = key % MyHashSet.bucket_size
        if not self.contains(key):
            self.bucket[index].append(key)
          

    def remove(self, key: int) -> None:
        index = key % MyHashSet.bucket_size
        for i in range(len(self.bucket[index])):
            if self.bucket[index][i]==key:
                self.bucket[index].remove(key)
                break
        

    def contains(self, key: int) -> bool:
        index = key % MyHashSet.bucket_size
        for i in range(len(self.bucket[index])):
            if self.bucket[index][i]==key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)