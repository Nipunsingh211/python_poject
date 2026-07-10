while True:
      print("=====calculater====")
      print("1.addition")
      print("2.subraction")
      print("3.mulipucation")
      print("4.division")
      print("5.Exist")
      ch=input("enter the your choice:")
      if ch=="1":
       num1=float(input("enter the no 1"))
       num2=float(input("enter the no 2"))
       solve=num1+num2
      elif ch=="2":
          num1=float(input("enter the no 1"))
          num2=float(input("enter the no 2"))
          solve=num1-num2
      elif ch=="3":
          num1=float(input("enter the no 1"))
          num2=float(input("enter the no 2"))
          solve=num1*num2
      elif ch=="4":
          num1=float(input("enter the no 1"))
          num2=float(input("enter the no 2"))
          if num2=="0":
              print("THE NO ZERO IS THE INVALID")
          else:
              solve=num1/num2
      elif ch=="5":
          solve="THE PORGRAM IS EXIST"
      else:
            print("THE INVALID NUMBER OR KEY")
      print(solve)