'''
     Input: Genomes P and Q.
          (+1 +2 +3 +4 +5 +6)
          (+1 -3 -6 -5)(+2 -4)
     Output: The 2-break distance d(P, Q).
          3
     Logic:
        Think of the blocks 1,2,3,4,5,6 as having two ends, plus and minus. "+1" means the first block is in positive orientation, 
        you could think of the minus end on the left and the plus end on the right. If two blocks are arranged in order 
        with + orientation as they are in the first line of input, then the plus end of 1 is connected to the minus end of 2. 
        Of course the minus end of 1 is connected to the plus end of 1 but were going to forget about that for this problem, 
        treat the two ends as separate nodes. So the (undirected) edges for the first line of input are:
           1+,2-; 2+,3-; 3+,4-; 4+,5-; 5+,6-;
        and then circularize it by adding 6+,1-
        The second line of input has two groups:
          1+,3+; 3-,6+; 6-,5+; 5-,1-;
          2+,4+; 4-,2-;
        Now add ALL of those edges to a single graph and find cycles, there should be 3:
          1+,2-,4-,3+,back to 1+
          2+,3-,6+,1-,5-,4+, back to 2+
          5+,6-, back to 5+
        and so d(P,Q) = blocks(P,Q) - cycle(P,Q)
         = 6 - 3
         = 3
        Blue edges are for P and red edges are for Q.
        Total Blocks = 6
'''
