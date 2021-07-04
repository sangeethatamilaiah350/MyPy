def countSubtreesWithSumX(root, x):
    c=0
    def fun(root):
        nonlocal c
        if root==None:
            return 0
        if root:
            cur=root.data+ fun(root.left)+fun(root.right)
            if cur==x:
                c+=1
            return cur
        
    fun(root)
    return c
    
