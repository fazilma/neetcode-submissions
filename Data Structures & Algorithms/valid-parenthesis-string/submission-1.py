class Solution:
    def checkValidString(self, s: str) -> bool:
        Omin = 0
        Omax = 0
        for i in s:
            if (i=='('):
                Omin +=1
                Omax +=1
            elif(i==')'):
                Omin = max(0, Omin-1)
                if(Omax<=0):
                    return False
                Omax = max(0, Omax-1)
            else:
                Omin = max(0, Omin-1)
                Omax +=1
        print(Omin, Omax)
        if Omin ==0:
            return True
        return False


        
        
            
