# I :heart: BUILT-IN SORTING

My solution is an implementation of a merge sort. The solution recursively breaks down the passed list into many single element arrays. Once that's done it combines all the arrays back together. I used [this site](https://builtin.com/machine-learning/fastest-sorting-algorithm) pretty extensively for help.

The implementations that I found on the internet for all of the algorithms solve for ascending order. To achieve a descending list, I used the list `.reverse()` method. Arguably that's cheating as its using in-built sorting but whatever, it was allowed in the rules :stuck_out_tongue_winking_eye:.

The tests all pass in ~10 seconds:

```
chris@MACHINE:~/source/personal/pybermuda-challenges/003$ pytest -v --durations=0
================================================================================ test session starts =================================================================================
platform linux -- Python 3.10.12, pytest-8.1.1, pluggy-1.5.0 -- /home/chris/source/personal/pybermuda-challenges/003/.env/bin/python
cachedir: .pytest_cache
rootdir: /home/chris/source/personal/pybermuda-challenges/003
collected 6 items                                                                                                                                                                    

test_sort.py::test_can_sort_list_in_ascending_order PASSED                                                                                                                     [ 16%]
test_sort.py::test_can_sort_list_in_descending_order PASSED                                                                                                                    [ 33%]
test_sort.py::test_sorting_alphabetical_order PASSED                                                                                                                           [ 50%]
test_sort.py::test_sort_really_long_list PASSED                                                                                                                                [ 66%]
test_sort.py::test_sort_really_long_list_including_negative_desc PASSED                                                                                                        [ 83%]
test_sort.py::test_sort_does_not_use_sort_or_sorted PASSED                                                                                                                     [100%]

================================================================================= slowest durations ==================================================================================
5.57s call     test_sort.py::test_sort_really_long_list_including_negative_desc
5.40s call     test_sort.py::test_sort_really_long_list

(16 durations < 0.005s hidden.  Use -vv to show these durations.)
================================================================================= 6 passed in 10.99s =================================================================================
```

I haven't done a compute comparison but i'd be interested in the memory comparison for the large tests of a merge vs an insertion sort. While incredibly inefficient on the BigO scale, implementations can very memory efficient since you only need to manipulate a single list.

```python
def manual_sort(list: list, *, order: str) -> int:
  i=1
  while i<len(list):
      j=i
      while j>0 and list[j] < list[j-1]:
          k = list[j]
          list[j] = list[j-1]
          list[j-1] = k
          j-=1
      i+=1

  if order == "desc":
    list.reverse()

  return list
````


