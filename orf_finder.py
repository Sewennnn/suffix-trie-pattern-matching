
from node import Node
from trie import Trie


class OrfFinder:
    def __init__(self, genome):
        """
        This is the init function of my OrfFinder class.
        
        Written by Choong Yu Xin

        Precondition: genome is not None and length of genome is > 0
        Postcondition: After all attributes are initialized, terminate

        Input: genome, which is the string of DNA i want to look at.
            
        Return: Return nothing
            

        Time complexity: 
            Best case analysis: O(n^2), where n is length of genome , since i build a suffix trie from the genome, so complexity is O(N^2) 
            
            Worst case analysis: O(n^2), where n is length of genome , since i build a suffix trie from the genome, so complexity is O(N^2) 

        Space complexity: 
            Input space analysis: O(n), where n is the length of the genome
            Aux space analysis: O(n^2), where n is length of genome, because i build a suffix trie which is O(n)
        """
        self.genome = genome
        self.suffix_trie = Trie()
        self.suffix_trie.build_suffix_trie(genome)
        


    def find(self, start, end):
        """
        This is the find function to find all substrings which start and end with the params given. 
        In my find function, i traverse the suffix trie to find all the occurences of my start and end strings,
        then loop through the occurences(i store them as list of indexes) to find valid substrings. Logic conditions are put in
        place to make sure loop breaks when a certain condition is not met, so that i can maintain complexity required.
        
        Written by Choong Yu Xin

        Precondition: length of start and end strings > 0
        Postcondition: Gives all substrings which start and end with the given params

        Input: genome, which is the string of DNA i want to look at.
            
        Return: Returns a list of all substrings which start and end with the given params
            

        Time complexity: 
            Best case analysis: O(T + U + V) , where T is length of string start, U is length of string end, and V is total number of characters in output list.
            
            Worst case analysis: O(T + U + V) , where T is length of string start, U is length of string end, and V is total number of characters in output list.

        Space complexity: 
            Input space analysis: O(T + U), where T is length of string start, U is length of string end
            Aux space analysis: O(V), where V is total number of characters in valid_substrings list(output)
        """
      
        start_positions = self.suffix_trie.search(start)
        end_positions = self.suffix_trie.search(end)
       
    
        if len(start_positions) == 0 or len(end_positions) == 0:  
            return []
        
        valid_substrings = []
        stop_flag = False
        min_index = -1  
        for i in range(len(start_positions)):
            start_index = start_positions[i] 
            for j in range(len(end_positions) - 1, min_index , -1):  
                end_index = end_positions[j]
                if start_positions[i] + len(start) - 1 < end_index:
                    valid_substrings.append(self.genome[start_index:end_index + len(end) ])
                else:
                    min_index = j
                    if j == len(end_positions) - 1:
                        stop_flag = True
                    break
            if stop_flag:
                break

        return valid_substrings


       

    

if __name__ == "__main__":
    genome = OrfFinder('AAAAAABBBBB')
    print(genome.find('C', 'A'))
    # genome = OrfFinder('AAABBAAABBAAA')
    # assert sorted(genome.find('AA', 'AB')) == sorted(['AAABBAAAB', 'AAAB', 'AABBAAAB', 'AAAB'])

    # genome = OrfFinder('DCDCADCDC')
    # assert sorted(genome.find('DC', 'AD')) == sorted(['DCDCAD', 'DCAD'])

    # genome = OrfFinder("A")
    # assert genome.find('A', 'A') == []

    # genome = OrfFinder('DDDAAADDD')
    # assert (sorted(genome.find('D', 'A')) == sorted(['DDDAAA', 'DDDAA', 'DDDA', 'DDAAA', 'DDAA', 'DDA', 'DAAA', 'DAA', 'DA']))

    # genome = OrfFinder('DDDAAADDD')
    # assert (sorted(genome.find('D', 'AA')) == sorted(['DDDAAA', 'DDDAA', 'DDAAA', 'DDAA', 'DAAA', 'DAA']))

    # genome = OrfFinder('DDDAAADDD')
    # assert (sorted(genome.find('DD', 'AA')) == sorted(['DDDAAA', 'DDDAA', 'DDAAA', 'DDAA']))

    # genome = OrfFinder('DDDAAADDD')
    # assert (sorted(genome.find('DD', 'DD')) == sorted(['DDDAAADDD', 'DDDAAADD', 'DDAAADDD', 'DDAAADD']))

    # genome = OrfFinder('DDDAAADDD')
    # assert (sorted(genome.find('D', 'D')) == sorted(['DDDAAADDD', 'DDDAAADD', 'DDDAAAD', 'DDD', 'DD', 'DDAAADDD', 'DDAAADD', 'DDAAAD', 'DD', 'DAAADDD', 'DAAADD', 'DAAAD', 'DDD', 'DD', 'DD']))
    # genome = OrfFinder('BADCABDADB')
    # assert sorted(genome.find('D', 'C')) == sorted(['DC'])
    # genome1 = OrfFinder("AAABBBCCC")
    # genome1.find("AAAB","BBB")
    # genome = OrfFinder('AAAAAABBBBBB')
    # print(genome.find("B", "A"))
    # genome = OrfFinder('AAABBAAABBAAA')
    # print(genome.find("AA", "AB"))
    # finder = OrfFinder("AAABBB")
    # print("start find")
    # print(finder.find("AA", "BB"))
    # print("start find")
    # print(finder.find("B","A"))
    # # print(trie.search("ll"))
    # # print(trie.search("l"))
    # print("start find")
    # # genome = OrfFinder("AA")
    # # assert(genome.find("AA", "A") == [])
    # genome = OrfFinder("AAAAAAA")
    # expected_res = ["A"*2]*6 + ["A"*3]*5 + ["A"*4]*4 + ["A"*5]*3 + ["A"*6]*2 + ["A"*7]*1
    # assert(sorted(genome.find("A", "A")) == sorted(expected_res))
    # genome = OrfFinder("AAB")
    # print(genome.find("AA", "AB"))
