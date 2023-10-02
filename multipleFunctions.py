class multipleFunctions:
    def Subfields():
        print("Sub-fields in AI are:")
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for val in list:
            print(val)

       
    def OddEven():
        num = int(input("Enter a number: "))
        if((num%2)==0):
            print("{0} is Even Number".format(num))
        else:
            print("{0} is Odd Number".format(num))
            
    def Eligible():
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        if(gender=='Male'):
            if(age>21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(gender=='Female'):
            if(age>18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("GIVE VALID INPUT DATA")
            
    def percentage():
        mark1 = int(input("Subject1= "))
        mark2 = int(input("Subject2= "))
        mark3 = int(input("Subject3= "))
        mark4 = int(input("Subject4= "))
        mark5 = int(input("Subject5= "))
        Total = mark1+mark2+mark3+mark4+mark5
        print("Total : ",Total)
        Percent = (Total/500)*100
        print("Percentage : ",Percent) 
        
    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(Height*Breadth)/2)
        Height1 = int(input("Height1:"))
        Height2 = int(input("Height2:"))
        Breadth = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Height1+Height2+Breadth)




















