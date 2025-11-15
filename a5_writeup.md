# Assignment 5 Write up

Assignment 5 can be broken up into the following parts:
1. Import the Necessary Modules:
- `copy`: For creating deep copies of objects
- `Stack` and `Queue`: Custom implementations for DFS and BFS operations
2. Utility Functions: 
- `remove_if_exists`: Removes a specified element from a list if it exists, which is used to remove the possibilites from a cell
3. Board Class:
- Represents the Sudoku board
- Consists of functions that will find the most constrained cell, and update the board, which eliminates possible solutions
4. DFS & BFS Functions:
- `DFS`: Uses depth-first search to solve the Sudoku puzzle. It works by trying to fill the most constrained cell with potential values until a solution is found or backtracks if a mistake is made
- `BFS`: Uses breadth-first search to solve the Sudoku puzzle in a similar fashion to DFS but explores nodes level by level
5. Main Execution:
- Defines two different sets of initial moves for Sudoku puzzles
- Uses both DFS and BFS to solve each puzzle and prints the results


After completing the assignment, answer the following reflection questions:

## Reflection Questions

1. What are some things that you learned through this assignment? Think about the concepts of backtracking, constraint satisfaction, and search algorithms. Were there any particular challenges you faced while implementing the Board class methods or the DFS/BFS functions? How did you overcome them?

This assignment really helped me understand how stacks and queues function, and I got a much better grasp on what separates Depth First Search from Breadth First Search. Most of the board class implementation went smoothly, but I hit a snag with BFS where the search wasn't working correctly. After some troubleshooting, I borrowed a few ideas from my DFS code and adapted them to fix the BFS method, which ended up solving the problem.



2. How can you apply what you learned in this assignment to future programs or projects? Consider other types of problems that involve searching through possibilities, making decisions, and backtracking when those decisions don't work out. Can you think of real-world scenarios where DFS or BFS might be useful? What about other constraint satisfaction problems?

The concepts from this project have practical applications beyond just this assignment. Search algorithms like BFS and DFS show up all over computer science—whether I'm working on pathfinding problems or optimizing solutions. The board structure itself could easily be modified for other grid-based games like chess or checkers. In real-world terms, these search methods are critical in networking applications. When you need to traverse connected nodes or find paths through a network, choosing between BFS and DFS depends on whether you need to explore broadly or dive deep into specific branches first.


3. Explain how the Stack and Queue classes work and why they are important for DFS and BFS algorithms. Describe the difference between LIFO (Last In First Out) and FIFO (First In First Out) data structures. How does using a Stack versus a Queue change the way the search algorithm explores possible solutions? Why is one data structure better suited for depth-first search and the other for breadth-first search?

Stacks operate on a "last in, first out" principle—you can only add or remove items from the top, pushing everything else down as you go. Queues work differently: new items join at the back, but removals happen at the front, creating a "first in, first out" system. This distinction is crucial for search algorithms. DFS relies on a stack to explore paths deeply before backtracking, while BFS uses a queue to systematically check all neighbors at the current level before moving deeper. The LIFO structure of stacks makes them ideal for DFS because you fully explore one path before considering alternatives. Meanwhile, FIFO queues support BFS's level-by-level approach, ensuring you examine all immediate options before going further. Essentially, stacks lead to thorough, depth-oriented exploration, while queues enable broader, more systematic searching across possibilities.