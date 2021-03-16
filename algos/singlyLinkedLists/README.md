**Linked Lists**

A linked list is a data structure to represent a sequence of items, but without using an array. It uses objects that are linked together in a particular order.

Linked lists are used widely in backends, frameworks, runtimes and operating systems.

How does your operating system keep track of the files in a directory? Modern systems do not do this with an array. They use a data structure called a linked list. Linked lists are easily reordered and well-suited for large data collections because (unlike arrays) they store data in small pieces of memory that “fit in the holes” between variables, rather than requiring a large chunk of contiguous memory. Linked lists are the first data structure we discuss as an object; they use references.

Linked lists provide a way to store a large amount of information without forcing the runtime to find a large contiguous chunk of memory (as arrays do). Indeed, a linked list of 1000 pieces of information could use 1000 small spaces in memory. Like an array, they keep information in a certain order. However, unlike arrays, you need not relocate everything in order to add a value to the middle! Linked lists introduce the reference concept – essentially, storing the location of the variable, instead of its value. This reference is ‘just another’ attribute in the node object that can be compared, set, etc.

Linked lists are preferable to arrays if frequently adding/removing values mid-sequence. Unlike arrays, singly linked lists directly access only the first node – to reach later ones, we traverse from one node to the next one by following the sequence of .next pointers. Singly linked lists have the ability to traverse only forward through the list, because they contain only a single link between nodes. A doubly linked list is comprised of nodes containing both .next and .prev pointers, and for this reason they are useful when we need to traverse back and forth in our sequence; that said, doubly linked lists are slightly more complicated to build and maintain (as we will see).

**runner**
So how do we work with linked lists? A common pattern is to declare a local variable called runner, set it to reference the first node, use it to access that node, then update it to point to the second node, use it to access that node, and so on until runner reaches the end of the list. To update runner to point to the next node, we would execute runner = runner.next;