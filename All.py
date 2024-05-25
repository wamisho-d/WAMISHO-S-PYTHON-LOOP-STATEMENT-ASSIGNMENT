# Question 1 Task 1: Your Mood Today
import random
moods = ["Happy", "Sad", "Energetic", "Calm"]
the_days_of_the_week = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
for day in the_days_of_the_week:
 mood = random.choice(moods)
print(f"On {day}, You were feeling {mood.lower()}.")

# Question 2 Task 1: Your Mood Tracker
import random
moods = ["Happy", "Sad", "Energetic", "Calm"]
the_days_of_the_week = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
times_of_the_day =["morning", "afternoon", "evening"] 
for day in the_days_of_the_week:
 for time in times_of_the_day:
  mood = random.choice(moods)
  print(f"On {day} {time} You were {mood}")
# Question 3 Task 1:Loop Condition Exploration
  counter = 0
  while True:
    print("an infinite loop iteration")
    counter += 1
    if counter >= 5:
        break
    
# Question 3 Task 2:Conditional Exit
  counter = 0
  while counter < 5:
    print("the loop will terminate once the condition met")
    counter += 1
 
# Question 4 Task 1:Random Choice Game
  import random
  def random_choice_game():
     items = ['apple', 'banana', 'cherry', 'orange']
     selected_item = random.choice(items)
     print('guess which item in the list was selected.')
     print(items)
     user_guess = input("Enter your guess:").strip.lower()
     if user_guess == selected_item:
      print("you guessed correctly")
else:
    print(f"you guessed incorrectly. the correct item was {'selected_item'}")
  
# Quuestion 5 Task 1: The for Loop DJ Set
# Our playlist of genre
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
number_of_the_track = 1
for genre in genres:
    print(f"track {number_of_the_track}: playing {genre}")
    number_of_the_track += 1
# Question 5 Task 2:The Remix Artist with while
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
i = 0
while i < len(genres):
    genre = genres[i]
    print(f"playing {genre}")
    if genre == 'Rock':
        break
    i += 1

# Question 5 Task 3: Light Show Technician Loop
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for index in range(len(genres)):
    if genres[index] == 'Rock':
       continue 
    print(f"track{index + 1}: the light show is ready for {genres[index]} genre")
  
# Question 6 Task 1: The Selective DJ
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
sublist_of_genres = genres[1:4]
for genres in sublist_of_genres:
   print(genres)

# Question 6 Task 2: The One-Liner Band with List Comprehensions

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
new_list = [genre + ' music' for genre in genres]
print(new_list)

# Question 6 Task 3: Numerical Beats with range
for index in range(10,0,-1):
    print(index)
    print("The beat drops now!")



