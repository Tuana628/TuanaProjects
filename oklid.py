import math

points = [(10,5), (20,25),(21,11),(36,21)]

'''letscall them a b c d, i need 6 different result, ab ac ad bc bd cd'''

'''d = √(x₂-x₁)²+(y₂-y₁)² '''
a1=0
a2 =1
b1 = 2
b2 = 1

x1 = points[a1][a1] 
y1 = points[a1][a2] 
x2 = points[b2][a1]
y2 = points [b2][a2] 

distances = []

def euclideanDistances(x1,x2,y1,y2):
    euclid = (math.sqrt((x2-x1)**2 + (y2-y1)**2))
    euclid = int(float(euclid))
    distances.insert(0,euclid)

'''found ab'''
euclideanDistances(x1,x2,y1,y2)

'''found ac ad'''

for i in range(2):
    b2 = b2 +1
    x2 = points[b2][a1]
    y2 = points [b2][a2]
    euclideanDistances(x1,x2,y1,y2) 

'''adjusted the values to find bc and bd''' 

b2 = 1
a1 = b2 
for i in range(2):
    b2 = b2 +1
    x2 = points[b2][a1]
    y2 = points [b2][a2]
    euclideanDistances(x1,x2,y1,y2) 

'''adjusted the values again to find cd'''
b2 = 3
x1 = points[b1][a1] 
y1 = points[b1][a2] 
x2 = points[b2][a1]
y2 = points [b2][a2]
euclideanDistances(x1,x2,y1,y2) 

'''this gives us the minimum number'''
min_distance = min(distances)
print(min_distance)









    



















    

