def init(self):
        """
        initialize your data structure here.
        """
        self.p=[]


    def addNum(self, num: int) -> None:
        p=self.p
        bisect.insort(p,num)


    def findMedian(self) -> float:
        p=self.p
        if len(p)%2==1:
            return p[len(p)//2]
        else:
            return (p[len(p)//2] + p[len(p)//2 - 1])/2
