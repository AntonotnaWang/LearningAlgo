class MaxHeap(object):
    def __init__(self, elements):
        self.elements = elements
    
    def __len__(self):
        return len(self.elements)
    
    def heapify(self):
        for idx in range((len(self.elements) + 1) // 2 - 1, -1, -1):
            self._shift_down(idx)
    
    def add(self, val):
        self.elements.append(val)
        self._shift_up(len(self.elements) - 1)
    
    def pop(self):
        self.elements[0], self.elements[len(self.elements) - 1] = self.elements[len(self.elements) - 1], self.elements[0]
        max_val = self.elements.pop()
        self._shift_down(0)
        return max_val
    
    def _shift_up(self, idx):
        if idx > 0:
            parent_idx = int((idx-1)/2)
            if self.elements[parent_idx]<self.elements[idx]:
                self.elements[parent_idx], self.elements[idx] = self.elements[idx], self.elements[parent_idx]
                self._shift_up(parent_idx)
    
    def _shift_down(self, idx):
        left = idx*2 + 1
        right = idx*2 + 2
        
        if left <= len(self.elements) - 1 and self.elements[left] > self.elements[idx]:
            biggest = left
        else:
            biggest = idx
        
        if right <= len(self.elements) - 1 and self.elements[right] > self.elements[biggest]:
            biggest = right
            
        if biggest != idx:
            self.elements[biggest], self.elements[idx] = self.elements[idx], self.elements[biggest]
            self._shift_down(biggest)

if __name__ == "__main__":
    h = MaxHeap([1,2,3,4,5,6,7])
    h.heapify()

    for i in range(3):
        h.add(i)
    
    print(h.elements)
    
    for i in range(len(h.elements)):
        print(h.pop())
    