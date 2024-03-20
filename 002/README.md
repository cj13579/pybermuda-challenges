# NOT TERRIBLE FIBONACCI

While the solution [submitted](fibonacci.py) is probably more Pythonic and flashy, on my machine (a relative new one, but not top of the line) it was no faster than just using simple structures. Both solutions execute on my machine in about `0.00025` seconds.

For the recursive approach, we solve for the time complexity $O(2^n)$ by using caching to "remember" previously calculated values. To implement this in a simple way I've used [`@functools.cache`](https://docs.python.org/3/library/functools.html#functools.cache). This decorator creates a dictionary lookup for function arguments and their returned values meaning we only calculate each position once.

My original, quick and dirty implementation, did much the same thing and I think I prefer it more. Starting with a list of 2 values `[0,1]` we iterate from the next position (2) in the list to `n`. For each position we calculate the value from the previous 2 list position values and add the result to the end of the list. At the end, we return `n-1` since Python lists are zero indexed.

```python
def fibonacci(n) -> int:
    l = [0,1]
    for f in range(2,n):
        a = (l[f-1]) + (l[f-2])
        l.append(a)
    
    return l[n-1]
```
