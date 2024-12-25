def maxArea(height):
        i = 0
        j = len(height)-1
        finalarea = 0
        while i < j:
            minval = min(height[i],height[j])
            area = minval * (j-i)
            if area > finalarea:
                finalarea = area
            if minval == height[i]:
                i+=1
            else:
                j-=1
        return finalarea

