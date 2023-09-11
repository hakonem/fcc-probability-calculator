import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):      #colour and number of balls
    self.contents = []
    for i, j in balls.items():
      for k in range(j):          
        self.contents.append(i)    #append appropriate colour element to contents list for each ball passed

  def draw(self, number):
    if len(self.contents) >= number:
      chosen_balls = []
      for n in range(number):
        random_ball = random.choice(self.contents) # choose random ball,
        chosen_balls.append(random_ball)  #append it to chosen list
        self.contents.remove(random_ball)    # and remove from hat contents
      return chosen_balls
    else:
      return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0      # how many times the expected balls are drawn
 
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)    # start each experiment with fresh hat
    drawn = hat_copy.draw(num_balls_drawn)  # list of drawn balls
    match = True
    for i, j in expected_balls.items():
      if drawn.count(i) < j:   #compare number of each colour drawn with expected number of that colour
        match = False
        break
    if match:  
      M += 1

  return M/num_experiments
