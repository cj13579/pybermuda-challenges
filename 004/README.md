# Zombies in the City :zombie: :cityscape:

My solution, for each day, takes a copy of the city grid using `copy.deepcopy()` to a variable called `today`. Then, for each for, we go through the value at each column looking for a `Z`. If we find one, we then go left, right, up down checking two things:

1. Is the left, right, up, and down position valid for the size of the grid? 
2. If it is, is the value at that position an `H`.

If both of those things are true then the value at the position gets turned into a `Z`.

Once we have been through each row of the grid we increase the day and overwrite the value of `city.grid` with the value of `today`.
