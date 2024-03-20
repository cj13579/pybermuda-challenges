# NOT TERRIBLE FIBONACCI

Starting with a list of 2 values `[0,1]` we iterate from the next position in the list (2, since Python lists are zero indexed) to `n`. For each position in the Fibonacci sequence we calculate the value from the previous 2 list position values and add the result to the end of the list. Once we've done that, we delete the list to only keep the last 2 positions. This keeps the memory utilization low and makes the list accessing fast. At the end, we return the last item in the list.

In my previous recursive approach, we solve for the time complexity $O(2^n)$ by using caching to "remember" previously calculated values. To implement this in a simple way I've used [`@functools.cache`](https://docs.python.org/3/library/functools.html#functools.cache). This decorator creates a dictionary lookup for function arguments and their returned values meaning we only calculate each position once.

```python
    @cache
    def f(i: int) -> int:
        if i <= 1: return i
        else: return f(i-1) + f(i-2)
    
    a = 0
    for num in range(n):  a = f(num)
    return a
```

## A retaliation to the obnoxious approach by J Robinson

James' very novel approach to solving this problem inspired my switch to the list based approach so that I could manage the memory by keeping the size of the list to 2 elements. Testing James' approach on my machine I was able to calculate the Millionth Fibonacci number in ~28 seconds:

```
Traceback (most recent call last):
  File "C:\Users\Chris\Source\cj13579\pybermuda-challenges\002\perf_analysis\elothepii.py", line 71, in <module>
    check_fibonacci()
  File "C:\Users\Chris\Source\cj13579\pybermuda-challenges\002\perf_analysis\elothepii.py", line 63, in check_fibonacci
    assert (
AssertionError: The 1000000th fibonacci number took more than 1s: it took 28.13s
```

It annoyed me how good that was since using recursion with caching ran out of memory. But simple addition and lists come good again. I was able to calculate the millionth Fibonacci number in ~5 seconds:

```
Traceback (most recent call last):
  File "C:\Users\Chris\Source\cj13579\pybermuda-challenges\002\fibonacci.py", line 67, in <module>
    check_fibonacci()
  File "C:\Users\Chris\Source\cj13579\pybermuda-challenges\002\fibonacci.py", line 59, in check_fibonacci
    assert (
AssertionError: The 1000000th fibonacci number took more than 1s: it took 4.88s
```
