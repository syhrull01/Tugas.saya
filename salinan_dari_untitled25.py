# -*- coding: utf-8 -*-
"""Salinan dari Untitled25.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o4ti_iRU2i-LMT0p1P39Ug6-KUnWqtyf
"""

list = ["pulpen", "buku", "pensil", "meja"]
print (list)

#mengambil item pada list
list [1]
#mengubah item pada list
list [3] = "kursi"
print(list)
#menambahkan item pada list
list.append("meja")
print(list)
#menyisipkan item tertentu pada index tertentu
list.insert(1, "penghapus")
print(list)
#menghapus item tertentu
list.remove("meja")
print(list)
#menghilangkan item pada imdex tertentu
list.pop(1)
print(list)