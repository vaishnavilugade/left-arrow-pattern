def leftarow(a):
      for i in range(a,0,-1):
           for j in range(i,0,-1):
                print("* ", end="")
           print("<")
      for i in range(2,a+1):
          for j in range(i,0,-1):
               print("* ", end="")
          print("<")
 
pattern(4)
 