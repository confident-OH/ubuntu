class students:
    def __init__ (self, name, number, math, english, chinese, c):
        self.name = name
        self.number = number
        self.math = math
        self.english = english
        self.chinese = chinese
        self.c = c
        pass
    def cout (self):
        for i in range(15):
            print('*', end = "*")
        print("")
        print("name:", self.name)
        print("number:", self.number)
        print("math:", self.math)
        print("english:", self.english)
        print("chinese:", self.chinese)
        print("c:", self.c)
        for i in range(15):
            print('*', end = "*")
        print("")
        print("")
        pass
    def change(self, sub, ch):
        dic = {"name": self.name, "number":self.number, "math": self.math, "english": self.english, "chinese":self.chinese, "c": self.c}
        dic[sub] = ch
        self.name = dic["name"]
        self.number = dic["number"]
        self.math = dic["math"]
        self.english = dic["english"]
        self.chinese = dic["chinese"]
        self.c = dic["c"]
nummark = 0
a = []
c = input("Are you ready? (y/n)")
while (c == 'y' or c == 'Y'):
    i = int(input("1: Add an information\n2: Print all information\n3: Change an information\n4: Delete an information\n5: Sort those information\n"))
    if i == 1:
        nummark += 1
        name = input("name: ")
        number = input("number: ")
        math = input("math: ")
        english = input("english: ")
        chinese = input("chinese: ")
        c = input("c: ")
        inf = students(name, number, math, english, chinese, c)
        a.append(inf)
    if i == 2:
        for j in range(nummark):
            print("Information", j + 1)
            a[j].cout()
    if i == 3:
        n = int(input("Which one? "))
        sub = input("sub: ")
        ch = input("change:  ")
        a[n - 1].change(sub, ch)
    if i == 4:
        n = int(input("Which one? "))
        del(a[n - 1])
        nummark -= 1
    if i == 5:
        a.sort(key = lambda x : x.name)
    c = input("Again? (y/n)")
