# Wordle

I'm terrible with words so I don't get along with real life Wordle but this was fun.

Given that with this verion of the game there are no restrictions on the number of attempts you can make, this is an interesting problem to solve as there are obviously a bunch of ways that you can do it. I thought that the easiest way to do this would be so solve letter by letter. 

To this end, my solution goes position-by-position and works out the letter in that position by iterating through each letter of the alphabet until it gets a '🟩' for that position. It then returns a letter/position `dict` that can be combined to find out the word to be guessed. 

Returning a `dict` is overkill when iterating through the positions but I wondered whether or not it would be faster if you could solve all positions concurrently. What's interesting is that for the simplicity of this problem the overhead of starting the additional threads more than negates any concurrency benefit resulting in a _slower_ parallel soltion.

For example:

```
Solution is: rebid
Iterative time taken: 0.001
Parallel time taken: 0.005
```
