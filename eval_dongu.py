for metod in dir(list):
    if "__" not in metod:
        print(eval("list."+metod+".__doc__"))







