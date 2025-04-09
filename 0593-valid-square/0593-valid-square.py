class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dist(x,y):
            return math.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))
        
        if p1==p2==p3==p4:
            return False
        
        lst = [
            dist(p1, p2),
            dist(p1, p3),
            dist(p1, p4),
            dist(p2, p3),
            dist(p3, p4),
            dist(p2, p4)
        ]
        lst.sort()
        return lst[0] == lst[1] == lst[2] == lst[3] and lst[4] == lst[5]