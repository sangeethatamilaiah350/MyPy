class Solution:
    def printBoundaryView(self, root):
        # Code here
        lefts=[]
        lefts.append(root.data)
        rights=[]
        leafs=[]
        
        def left(node):
            
            while node:
                
                if not (node.left==None and node.right==None):
                    
                    lefts.append(node.data)
            
                if node.left:
                    node=node.left
                else:
                    node=node.right
                
        def right(node):
            
            while node:
                if not(node.left==None and node.right==None):
                    rights.append(node.data)
            
                if node.right:
                    node=node.right
                else:
                    node=node.left
        
                    
            
                    
        def leaf(node):
            
            if node==None:
                return 
            if node.left==None and node.right==None:
                leafs.append(node.data)
                
            leaf(node.left)
            leaf(node.right)
        
        left(root.left)
        
        right(root.right)
        
        leaf(root)    
            
        #print(lefts)
        #print(rights)
        #print(leafs)
        
        return  lefts+leafs+rights[::-1]
