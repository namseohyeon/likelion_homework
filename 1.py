def same(string):
    mylist = list(string)
    if(mylist[0]==mylist[-1]):
        print("회문입니다.")
    else: 
        print("회문이 아닙니다.")


string = input("단어를 입력하세요: ")
same(string)