class MedianFinder(object):

    def __init__(self):
        self.leftpq = []
        self.rightpq = []
        
    def balance(self):
        if len(self.leftpq) > len(self.rightpq) +1:
            node = heapq.heappop(self.leftpq)
            heapq.heappush(self.rightpq, -node)
            
        if len(self.rightpq) > len(self.leftpq) + 1:
            node = heapq.heappop(self.rightpq)
            heapq.heappush(self.leftpq, -node)
        

    def addNum(self, num):
        if not self.leftpq:
            self.leftpq.append(-num)
            return
        
        if num <= -self.leftpq[0]:
            heapq.heappush(self.leftpq, -num)
        else:
            heapq.heappush(self.rightpq, num)
        
        self.balance()
            
    def findMedian(self):
        if len(self.leftpq) == len(self.rightpq):
            return (-self.leftpq[0] + self.rightpq[0]) / 2
        elif len(self.leftpq) > len(self.rightpq):
            return -self.leftpq[0]
        else:
            return self.rightpq[0]