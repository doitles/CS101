# CS101
README


The program will take a command line and use Prim's minimum algorithm and run it on the graph to find the shortest path
It will show the graph size, total elements added, show the to and weight variables then print out the status, weight, and parent.

make with the program name will compile the program
make clean will clear the object file
make spotless will clear the output files

make test will compile the program and run it only if there is a text file called test.txt

------------------------------------------------------------------------------------------------------------------------------
sample output
------------------------------------------------------------------------------------------------------------------------------

make test
graph04 -P 1 test.txt
Array Size: 3
Total Elements Added: 4
Vertice: 1, Status: t, Weight: 0.000000, Parent: -1
Vertice: 2, Status: t, Weight: 1.000000, Parent: 3
Vertice: 3, Status: t, Weight: 2.500000, Parent: 1

graph04 -P 1 test2.txt
Array Size: 5
Total Elements Added: 5
Vertice: 1, Status: t, Weight: 0.000000, Parent: -1
Vertice: 2, Status: t, Weight: 4.440000, Parent: 1
Vertice: 3, Status: t, Weight: 4.560000, Parent: 2
Vertice: 4, Status: t, Weight: 2.520000, Parent: 2
Vertice: 4, Status: u, Weight: inf, Parent: -1

graph04 -P 1 test4.txt
Array Size: 5
Total Elements Added: 4
Vertice: 1, Status: t, Weight: 0.000000, Parent: -1
Vertice: 2, Status: t, Weight: 11.220000, Parent: 1
Vertice: 3, Status: u, Weight: inf, Parent: -1
Vertice: 4, Status: t, Weight: 1.111000, Parent: 2
Vertice: 5, Status: u, Weight: inf, Parent: -1

graph04 -P 1 test3.txt
Array Size: 5
Total Elements Added: 5
Vertice: 1, Status: t, Weight: 0.000000, Parent: -1
Vertice: 2, Status: u, Weight: inf, Parent: -1
Vertice: 3, Status: u, Weight: inf, Parent: -1
Vertice: 4, Status: u, Weight: inf, Parent: -1
Vertice: 5, Status: u, Weight: inf, Parent: -1
