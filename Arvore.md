
Lista 01

       45
      /  \
    20    60
   /  \     \
  7   30    81
     /  \     \
    8   4    97
            /
           100

Adicionando o valor 55

       45
      /  \
    20    60
   /  \     \
  7   30    81
     /  \     \
    8   4    97
            / \
           55 100

Removendo o valor 4:

       45
      /  \
    20    60
   /  \     \
  7   30    81
     /       \
    8        97
            /  \
           55  100


Árvore para Lista2:

       15
      /  \
     6   18
    / \    \
   3   7   20
        \
         16

Adicionando o valor 14:

       15
      /  \
     6   18
    / \    \
   3   7   20
  / \
 4   14
        \
         16

Removendo o valor 6:

       15
      /  \
     7   18
    / \    \
   3   4   20
        \
         14
          \
          16


Observe que a remoção na segunda árvore foi de um nó com dois filhos (o nó 6). A remoção foi feita ao trocá-lo pelo seu sucessor em ordem, que nesse caso foi o nó 7.
