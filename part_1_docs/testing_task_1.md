### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #should be '==' instead of a single '='.
      return True
    else # ':' is missing at the end of 'else'.
      return False
   

  dif highest_card(self, card1 card2): #should be 'def' instead of 'dif'. card1 and card2 need to be separated by a comma.
  if card1.value > card2.value:
    return card #should be 'card1' instead of 'card'.
  else:
    return card2
  


def cards_total(self, cards): #code needs to be indented to be within the class.
  total #total is undefined, value should be set to '0'.
  for card in cards:
    total += card.value
    return "You have a total of" + total #return is indented inside of 'for loop', should be outside of loop. This line  also needs to be written as f'{total}' to return the total within the string.
  
```
