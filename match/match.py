#match 
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



