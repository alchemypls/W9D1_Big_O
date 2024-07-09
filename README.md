# Big O Notation
## Algorithm 1: Linear Search
   - Description: Given an unsorted array of integers and a target value, find the index of the first occurrence of the target value in the array. If the target value is not found, return -1.
      ```bash
      def linear_search(arr, target):
        for i in range(len(arr)):
          if arr[i] == target:
              return i
      return -1

   - Analyze the time complexity of the linear search algorithm and express it using Big O notation.
     * Because the function only runs once through the list/array I would consider this O(n).

   - Implement the linear search algorithm and test it with sample inputs.

    Index of 70: 3
    Index of 11: 4
    Index of 99: -1

   - Propose an optimization to improve the efficiency of the linear search algorithm, if possible.
     * Tbh, I think O(1) is the best you can get, and O(n) is second best, and 'ideal' in most situation. and would be hard to take away with out destorying the function.
     * That said, you could make it more 'readable'. I think I saw some where you could put in
     ```bash
     def linear_search(arr, target):
     n = len(arr)
        for i in range(n):
          if arr[i] == target:
              return i
      return -1
      ```
       so you could use n = len(arr) to 'clean' it up?


     ## Bubble Sort
   - Description: Given an unsorted array of integers, sort the array in ascending order using the bubble sort algorithm.
     ```bash
     def bubble_sort(arr):
      for i in range(len(arr)):
        for ii in range(0, len(arr)-i-1):
            if arr[ii] > arr[ii+1]:
                arr[ii], arr[ii+1] = arr[ii+1], arr[ii]
      return arr
     ```

   - Analyze the time complexity of the bubble sort algorithm and express it using Big O notation.
     * Because bubble sort is using an nested for loop, I think it becomes O(n^2).

   - Implement the bubble sort algorithm and test it with sample inputs.
     ```bash
     Sorted array: [11, 12, 22, 25, 34, 64, 90]
     Sorted array: [1, 2, 4, 5, 8]
     ```

   - Identify the inefficiencies in the bubble sort algorithm and propose an optimized version of the algorithm.
     * Some rules of thumb I've seen tell me that for most cases, O(n^2) takes took long for large data structures or if you have to run it many times.
     * Seems like 0(n^2) are only really usable for problems that only need to be run once or twice a day(?).
  ## Analysis and reasoning
   * Generally I feel like less is more, and to avoid using more than 1 nested loop.

   - Include the time complexity analysis for each algorithm, expressed using Big O notation.
     * For the linear search as  we only have to run through the array once, it would count as O(n). Make it quite useable in most cases
     * For Bubble Sort on the other hand the nested loop means we run as many loops as needed until the nested loops condition are filled so on aveage O(n^2)

   - Provide a comparison of the original and optimized versions of the algorithms, highlighting the efficiency improvements.
     * I'm still too green to offer any real optimiztions to the code, I wouldn't know how to break down the bubble sort to use less time.

   - Discuss the trade-offs, if any, in terms of time complexity, space complexity, and code readability.
     * Overall my takeaways are that, if you only need to do it a few times, O(n^2) can be usable but not ideal, while O(N) or even O(1), should be strived towards and can be acceptable for most common use cases.






   
