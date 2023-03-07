import random
#To make the database which has 10000 combinations for 4 numbers that equal 10 includes repitions
def makequestion():
    file = open("D:\PROFILE BACKUP\Desktop/4=10.txt","w")
    nums = []
    ops = "*-+/"
    flag = True
    i = 0
    while flag:
        for x in range(4):
            nums.append(f"{random.randint(1,9)}")
            nums.append(f"{random.choice(ops)}")  
        sum = eval("".join(nums[:-1]))
        if sum == 10:
            file.write(f"{str(nums[:-1])}\n")
            i+=1
        if i == 10000:
            flag = False
        nums.clear()   
        sum = 0 
file2 = open("D:\PROFILE BACKUP\Desktop/4=10.txt","r")
flrd = file2.readlines()
rand = random.choice(flrd)
ques = eval("".join(rand[::2].split("'")))
# print("".join(eval(rand))) #developer access only
print(ques)
flag = True
while flag:
    try:
        def game():
            global flag
            val = input("Enter the 3 operators: ")
            val = val+" "
            answer = ""
            for x in range(4):
                answer = answer + f"{ques[x]}{val[x]}"
            if eval(answer) == 10:
                print("You won!!")
                print(f"{answer} = 10")
                flag = False
            elif eval(answer) != 10:
                print(f"Try Again\n{answer} does not equal to 10!")
                pass
        game()
    except IndexError:
        print("Invalid Input Try Again")
        game()
    except SyntaxError:
        print("Invalid Input Try Again")
        game()