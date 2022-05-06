# Trees Introduction: 
  Unlike Arrays, Linked Lists, Stack and queues, which are linear data structures, trees are hierarchical data structures.
## Tree Vocabulary: 
  The topmost node is called root of the tree. The elements that are directly under an element are called its children. The element directly above something is called its parent. For example, ‘a’ is a child of ‘f’, and ‘f’ is the parent of ‘a’. Finally, elements with no children are called leaves. 

            tree
            ----
            j    <-- root
          /   \
          f      k  
        /   \      \
      a     h      z    <-- leaves

## Why Trees? 
1. One reason to use trees might be because you want to store information that naturally forms a hierarchy. For example, the file system on a computer: 

        file system
        -----------
            /    <-- root
          /      \
        ...       home
              /          \
          ugrad        course
            /       /      |     \
          ...      cs101  cs112  cs113

2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays). 
3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists). 
4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on number of nodes as nodes are linked using pointers.

## Main applications of trees include: 
1. Manipulate hierarchical data. 
2. Make information easy to search (see tree traversal). 
3. Manipulate sorted lists of data. 
4. As a workflow for compositing digital images for visual effects. 
5. Router algorithms 
6. Form of a multi-stage decision-making (see business chess). 
Binary Tree: A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child. 
Binary Tree Representation: A tree is represented by a pointer to the topmost node in tree. If the tree is empty, then value of root is NULL. 
A Tree node contains following parts. 
1. Data 
2. Pointer to left child 
3. Pointer to right child
In C, we can represent a tree node using structures. In other languages we can use classes as part of their OOP feature.

# Binary Tree Properties

1. ### The maximum number of nodes at level *l* of a binary tree is *2<sup>l</sup>*. 
    Here level is the number of nodes on the path from the root to the node (including root and node). Level of the root is *0*. 
    This can be proved by induction. 
    For root, *l = 0*, *number of nodes = 2<sup>0</sup> = 1* 
    Assume that the maximum number of nodes on level ‘l’ is *2<sup>l</sup>* 
    Since in Binary tree every node has at most 2 children, next level would have twice nodes, i.e. *2 * 2<sup>l<sup>* 

2. ### The Maximum number of nodes in a binary tree of height *‘h’* is *2<sup>h</sup> – 1*. 
    Here the height of a tree is the maximum number of nodes on the root to leaf path. Height of a tree with a single node is considered as 1. 
    This result can be derived from point 2 above. A tree has maximum nodes if all levels have maximum nodes. So maximum number of nodes in a binary tree of height h is *1 + 2 + 4 + .. + 2<sup>h-1</sup>*. This is a simple geometric series with h terms and sum of this series is *2<sup>h</sup>– 1*. 
    In some books, the height of the root is considered as 0. In this convention, the above formula becomes *2<sup>h+1<sup> – 1* 

3. ### In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is Log2(N+1).
    This can be directly derived from point 2 above. If we consider the convention where the height of a root node is considered as 0, then above formula for minimum possible height becomes *| Log~2~(N+1) | – 1* 

4. ### A Binary Tree with L leaves has at least *| Log~2~ |+ 1*   levels. 
    A Binary tree has the maximum number of leaves (and a minimum number of levels) when all levels are fully filled. Let all leaves be at level l, then below is true for the number of leaves L.

      *L   <=  2l-1  [From Point 1]
      l =   | Log2L | + 1 
      where l is the minimum number of levels.*

5. ### In Binary tree where every node has 0 or 2 children, the number of leaf nodes is always one more than nodes with two children.

      *L = T + 1
      Where L = Number of leaf nodes
      T = Number of internal nodes with two children
      Proof:
      No. of leaf nodes (L) i.e. total elements present at the bottom of tree = 
      2<sup>h-1</sup> (h is height of tree)
      No. of internal nodes = {total no. of nodes} - {leaf nodes} = 
      { 2<sup>h</sup> - 1 } - {2<sup>h-1</sup>} = 2<sup>h-1</sup> (2-1) - 1 = 2<sup>h-1</sup> - 1
      So , L = 2<sup>h-1</sup>
          T = 2<sup>h-1</sup> - 1
      Therefore L = T + 1
      Hence proved*
