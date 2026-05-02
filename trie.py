from node import Node

class Trie:
    def __init__(self):
        """
        This is the init function for Trie class in which i have a root as starting node.
        
        Written by Choong Yu Xin

        Precondition: no precondition, no requirements needed
        Postcondition: After all attributes are initialized, terminate

        Input: No input
            
        Return: Nothing to return
            

        Time complexity: 
            Best case analysis: O(1), because i create a Node object and set that as my root, 
            and since in my implementation my Node always has size of 5 unless specified, it is constant
            Worst case analysis: O(1), because i create a Node object and set that as my root, 
            and since in my implementation my Node always has size of 5 unless specified, it is constant
        Space complexity: 
            Input space analysis: O(1), because i dont have input
            Aux space analysis: O(1), because i create a Node object of size 5(constant unless specified)
        """
        self.root = Node()


    def insert(self, suffix, suffix_index):
        """
        This is the insert function for inserting a string into my Trie structure.
        
        Written by Choong Yu Xin

        Precondition: suffix is not None and suffix_index > 0
        Postcondition: After inserting the suffix into my trie, terminate

        Input: suffix as a string(or substring, in my implementation where i use it to build suffix trie),
        and suffix_index which is the index of the character
            
        Return: Nothing to return
            

        Time complexity: 
            Best case analysis: O(n), where n is length of my suffix(ie. my key), since i loop through the suffix to insert each char until the end
            Worst case analysis: O(n), where n is length of my suffix(ie. my key), since i loop through the suffix to insert each char until the end
            
        Space complexity: 
            Input space analysis: O(n), where n is my suffix length
            Aux space analysis: O(n), because i loop through my self.current.link to insert my character for every char in suffix(ie.my key)
        """
        current = self.root
       
        for char in suffix:
           
            index = ord(char) - 65 + 1

            if current.link[index] is not None:
               
                current.link[index].indexes.append(suffix_index)
               
                current = current.link[index]

                
            else:
                current.link[index] = Node()
               
                
                current.link[index].indexes.append(suffix_index)
               
                current = current.link[index]


        if current.link[0] is not None:
            current = current.link[0]
        else:
            current.link[0] = Node()
            current = current.link[0]

       

    def search(self, key):
        """
        This is the search function to search for a particular string in my Trie structure.
        
        Written by Choong Yu Xin

        Precondition: key is not None and key is valid existing string in my Trie
        Postcondition: Gets the indexes of occurences of strings

        Input: Key (my string to search for)
            
        Return: Returns the payload stored in the current.link(in my payload i store the indexes of occurences of the key)
            

        Time complexity: 
            Best case analysis: O(1), if first char of key does not exist
            Worst case analysis: O(n), where n is length of key, since i have to loop until i find my key
            
        Space complexity: 
            Input space analysis: O(n), where n is the length of the key
            Aux space analysis: O(1), as the space used is not dependent on the input size
        """
        current = self.root
        for char in key:
            
            index = ord(char) - 65 + 1

            if current.link[index] is not None:  
               
                current = current.link[index]
             
            else:
                
                return[]
        
        return current.indexes
      
    
    def build_suffix_trie(self, text):
        """
        This is the function to build a suffix trie.
        
        Written by Choong Yu Xin

        Precondition: text is not None
        Postcondition: Suffix Trie is initialized

        Input: text(the string to build a suffix trie from)
            
        Return: Return nothing
            

        Time complexity: 
            Best case analysis: O(n^2), where n is length of text, since i will have n substrings from the text, 
            and i loop through n and call insert to insert the substring into the trie, which is n, so total complexity is o(n^2)
            Worst case analysis: O(n^2), where n is length of text, since i will have n substrings from the text, 
            and i loop through n and call insert to insert the substring into the trie, which is n, so total complexity is o(n^2)
            
        Space complexity: 
            Input space analysis: O(n), where n is the length of the text
            Aux space analysis: O(n^2), where n is length of text, because i have to insert n substrings according to input size
        """
        n = len(text)
        for i in range(n):
            self.insert(text[i:], i)