#Just importing -_- boring
import random

#Creating function
def estiminate_pi(n):
  #Creating variables for count points -_-
  num_point_circle = 0
  num_point_total = 0
  
  #LOOOOOOOOOOOOOOOOOOOOOOOOOOOOP
  for J in range(n):
    #Creating variables for give point an x and y options
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    #That's basicly sum of x and y squares
    distance = x**2 + y**2
    #Checking if point is inside compile
    if distance <= 1:
      #Counting points in circle
      num_point_circle+=1
    #Counting all points
    num_point_total+=1
  
  return 4 * num_point_circle/num_point_total
