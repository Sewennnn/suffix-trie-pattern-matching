class Node:
    def __init__(self,size=5 , data=None) :
        """
        This is the init function for my Node class.
        
        Written by Choong Yu Xin

        Precondition: size > 0
        Postcondition: After all attributes are initialized, terminate

        Input: Size is 5 unless specified in params , data is None unless specified in params
            
        Return: Nothing to return
            

        Time complexity: 
            Best case analysis: O(n), where n is size(set to 5 unless specified in params)
            Worst case analysis: O(n), where n is size(set to 5 unless specified in params)
        Space complexity: 
            Input space analysis: O(1), because size is integer, and data is set to None unless specified otherwise
            Aux space analysis: O(n), where i initialise the array acoording to my size
        """
        
        self.data = data
        self.link = [None] * size
        self.indexes = []
