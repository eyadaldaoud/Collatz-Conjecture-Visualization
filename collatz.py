import matplotlib.pyplot as plt

# This algorithm made to visualize The Simplest Math Problem No One Can Solve - Collatz Conjecture

# Made by Eyad Zoubi

def Simplest_Math_Problem():
  
  # ask the user a test number
  test_number = int(input("Enter a test number: "))
  
  # Keep track of loop times it took to reach 1
  loop_times = 0
  
  numbers = []
  
  # Init while loop to keep going untill it reachs 1
  while test_number > 1:
    
    # if even devide by 2
    if test_number % 2 == 0:
      x = test_number / 2
      numbers.append(test_number)

    else:
      # if odd multiply by 3 and add 1
      x = test_number * 3 + 1
      numbers.append(test_number)
    
    
    test_number = x
    loop_times += 1


  # Print out the tries it took to reach ONE
  print(f"Loops it took to reach ONE: {loop_times}")
  print(f"Highest value was: {int(max(numbers))}")
      
  # Append the final value of 1 to the list
  numbers.append(1)
  
  # Create a new figure
  fig = plt.figure()

  # Create a line plot of the Collatz sequence
  plt.plot(range(1, loop_times + 2), numbers, linestyle='-', marker='o', color='red')


  # Set the x-axis label
  plt.xlabel("Step")

  # Set the y-axis label
  plt.ylabel("Number")

  # Set the title of the plot
  plt.title("Collatz Conjecture Visualization")
 
  # Show the plot
  plt.show()
  


Simplest_Math_Problem()
