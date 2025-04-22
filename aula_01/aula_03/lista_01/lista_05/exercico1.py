def maior(x, y):

    x = int(input())
    y = int(input())

    if x > y:
        print(x, "é o maior número")
    elif y > x:
        print(y,"é o maior número")
    else:
        print("Os números são iguais.")

maior(40,12)