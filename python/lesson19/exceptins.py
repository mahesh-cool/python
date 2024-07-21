class JustNotcoolerror(Exception):
    pass
x =2
# print(x/0)
try:
    raise JustNotcoolerror("This just is't cool, man")
    raise Exception("I' am a custom exception!")


    # print(x/0)
    if not type(x) is str:
        raise TypeError("only strings are allowed")
except NameError:
    print('NameError means something is probably undefined')
    #defining the error definition manually
except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I' am going to  print with or without an error.")


    
    

