#match 
x=20
y=30
listy=["apple","banana"]
tupli= ("apple","banana")
seti={"apple","banana"}
dicty={
    "fruit":["apple","banana"]
}
match listy:
    case ["apple","banana"]:
        print("the value you have given matched!!")
    case ["apple"]:
        print("the value you have given not matched!!")
    case ["banana"]:
        print("the value you have given not matched!!")
    case ["apple","banana","mango"]:
        print("the value you have given not matched!!")

match tupli:
    case ("apple","banana"):
        print("the value you have given matched!!")
    case ("apple"):
        print("the value you have given not matched!!")
    case ("banana"):
        print("the value you have given not matched!!")
    case ("apple","banana","mango"):
        print("the value you have given not matched!!")

#extra condition check
match x:
    case 20 if y>=30:
        print("It is correct")
    case 20 if y==30:
        print("It is correct1")
        #run the first case even more than one case id right


#using of pipe character to check for more than one value match in one case
match x:
    case 10|30|40:
        print("Ur ia sjfh")
    case 20:
        print("This one is corect")

