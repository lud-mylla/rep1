def maior (x, y, z):
   print("Digite três números:")
   x = int(input())
   y = int(input())
   z = int(input())
   
   if x > y and x > z:
      print(x, "é o maior número")
   elif y > x and y > z:
      print(y, "é o maior número ")
   elif z > x and z > y:
      print(z, "é o maior número ")
   else:
      print("Os números são iguais")


maior(10,20,40)
