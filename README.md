# Hangman
Python command-line [Hangman](https://en.wikipedia.org/wiki/Hangman_(game)) game
Author - Ramanuj Tiwari

## How to reach out to the game ?
To run this game on your system follow the steps given below:

1. Clone this repository.
2. You should have Python 3 installed on your system.
3. Select the directory Hangman and terminal in it
4. Run the command given below: -
```
$ python Hangman_Ramanuj.py
```
#### After executing the command above
![i1](https://user-images.githubusercontent.com/79203621/148575450-6aba227b-f4d7-420c-b268-084c587f2834.png)

#### Progression of Hangman game
![i2](https://user-images.githubusercontent.com/79203621/148579161-3a0f0495-f0d8-4e44-83c4-1bbfda4a0c2a.png)

(i) The player enters the first character as "a" which is not present in the winning word. So the user gets this "Sorry !!! Wrong Attempt" message on the console. Also we can see the hanging arrangement in its early stage. In the very next line we can see the message "You have 4 lives left". So the number of lives which was 5 at the start of the game is reduced by 1 to 4 because of wrong guess attempt.

(ii) The second attempt by player i.e. "d" also wrong attempt. Now the remaining lives left is 3. The hanging arrangement has some changes.

(iii) Finally a correct guess by player "o". Player gets the message "Correct Attempt!!!". Notice the number of lives left as 3 which is same as previous step because of the correct guess. Also all the occurences of the correctly guessed character is updated in the current string.

(iv) Another correct guess "e".
![i3](https://user-images.githubusercontent.com/79203621/148581463-56cb2e5f-4b9a-48c0-8ab4-46210172ce05.png)

(v) Wrong guess "n", lives remaining is now 2.

(vi) Wrong guess "p", lives remaining is now 1.

(vii) The final guess is "m" which is also incorrect so we have no lives left. Now the hanging arrangement is complete. Player gets a message "You lose!!! Better luck next time". Now the game tells the player the correct word.
### Game asks for play again choice
If the Player wants to go on with the game he can enter yes to restart the game or no otherwise.

## Additional Features that game possesses
### Checks Validity of Entered string - 
(i) More than one character case:-

![i4](https://user-images.githubusercontent.com/79203621/148583845-b289c436-3e4e-4a9d-82b1-f0500977f801.png)

The Player gets the message "Invalid Input!!! You have entered more than one character".

(ii) Special character or number entered:-

![i5](https://user-images.githubusercontent.com/79203621/148584644-68620f0c-6a96-45cf-a62c-8d59015d484d.png)

(iii) Character entered is in upper case -

![i6](https://user-images.githubusercontent.com/79203621/148585118-ce26fb87-8d3d-4044-8c25-02f9c2595588.png)

NOTE:In any of the above cases the remaining lives of Player are not deducted.

### Player re-enters the previously guessed character

#### Case 1: Correct guess repeated
The game continues with its normal flow. Player gets a message of "Already correctly guessed character".

#### Case 2: Incorrect guess repeated
In general incorrect guess, the remaining lives of player is decreased by 1. But since the live was already decreased once earlier the game does not decrease the life in this repeated wrong guess. It gives message to the user his repeated incorrect guess.

