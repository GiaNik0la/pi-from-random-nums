#Just importing -_- boring
import random

#Creating function
def calculate_pi(n):
  #Creating variables for count points -_-
  point_in_circle = 0
  point_in_square = 0
  
  #LOOOOOOOOOOOOOOOOOOOOOOOOOOOOP
  for Jemala in range(n):
    #Creating variables for give point an x and y options
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    #That's basicly sum of x and y squares
    social_distance_D = x**2 + y**2
    #Checking if point is inside compile
    if distance <= 1:
      #Counting points in circle
      point_in_circle+=1
    #Counting all points
    point_in_square+=1
  
  #CALCULATIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON
  return 4 * point_in_circle/point_in_square
