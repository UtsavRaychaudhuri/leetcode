def rectangleBoxes(operations):
    boxes=[]
    rectangles=[]
    res=[]
    def checkboxes(rectangles,boxes):
        for i in boxes:
            canfit=True
            for j in rectangles:
                if (j[0]<=i[0] and j[1]<=i[1]) or (j[1]<=i[0] and j[0]<=i[1]):
                    pass
                else:
                    canfit=False
            if canfit:
                res.append(True)
            else:
                res.append(False)
        return res
    for i in operations:
        if i[0]==0:
            rectangles.append([i[1],i[2]])
        else:
            boxes.append([i[1],i[2]])
            res.append(checkboxes(rectangles,boxes))
    if len(rectangles)==0:
        return [True]*len(boxes)
    return res



    

rectangleBoxes([[0,10,8], 
 [0,4,4], 
 [0,4,9], 
 [1,10,10], 
 [1,9,6], 
 [1,4,1], 
 [0,12,8], 
 [0,10,8], 
 [0,1,20], 
 [0,5,5]])