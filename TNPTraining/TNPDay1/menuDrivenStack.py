# # # # let a= [1,2,3,4,5]


# # # # function empty (){
# # # #     return a = []
# # # # }
# # # # function pushNum (n){
# # # #     return a.push(n) 
# # # # }

# # # # function popNum(n){
# # # #     if (length(a) == 0){
# # # #         return console.log("string is already empty")
# # # #     }
# # # #     return a.pop()
# # # # }

# # # # function main (){
# # # #     let operation = prompt ("enter the number ")
# # # #     if (operation == 0){
# # # #         empty()
# # # #     }if (operation == 1){
# # # #         let n = prompt ("enter the num")
# # # #         pushNum (n)
# # # #     }if (operation == 2){
# # # #         let n  = popNum()
# # # #         console.log("the poped number :" , n)
# # # #     }
# # # # }
# # # # main()






# # # class Stack:
# # #     def __init__(self, initial_list=None):
# # #         if initial_list is None:
# # #             self.list = []
# # #         else:
# # #             self.list = initial_list

# # #     def isEmpty(self):
# # #         return len(self.list) == 0

# # #     def isNull(self):
# # #         return self.list is None

# # #     def pop(self):
# # #         if self.isEmpty():
# # #             return "The list is empty"
# # #         return self.list.pop()

# # #     def peek(self):
# # #         if self.isEmpty():
# # #             return "The list is empty"
# # #         return self.list[-1]

# # #     def push(self, item):
# # #         self.list.append(item)

# # #     def size(self):
# # #         return len(self.list)

# # #     def stackMenu(self):
# # #         while True:
# # #             menu_num = int(input("Enter the menu number (0: isEmpty, 1: pop, 2: peek, 3: push, 4: size, 5: isNull, 6: exit): "))
# # #             if menu_num == 0:
# # #                 print(self.isEmpty())
# # #             elif menu_num == 1:
# # #                 print(self.pop())
# # #             elif menu_num == 2:
# # #                 print(self.peek())
# # #             elif menu_num == 3:
# # #                 item = int(input("Enter the number to push: "))
# # #                 self.push(item)
# # #             elif menu_num == 4:
# # #                 print(self.size())
# # #             elif menu_num == 5:
# # #                 print(self.isNull())
# # #             elif menu_num == 6:
# # #                 break
# # #             else:
# # #                 print("Invalid menu number. Please try again.")

# # # # Example usage:
# # # stack = Stack()
# # # stack.stackMenu()
# # # class Stack:
# # #     def __init__(self, initial_list=None):
# # #         if initial_list is None:
# # #             self.list = []
# # #         else:
# # #             self.list = initial_list

# # #     def isEmpty(self):
# # #         return len(self.list) == 0

# # #     def isNull(self):
# # #         return self.list is None

# # #     def pop(self):
# # #         if self.isEmpty():
# # #             return "The list is empty"
# # #         return self.list.pop()

# # #     def peek(self):
# # #         if self.isEmpty():
# # #             return "The list is empty"
# # #         return self.list[-1]

# # #     def push(self, item):
# # #         self.list.append(item)

# # #     def size(self):
# # #         return len(self.list)

# # #     def stackMenu(self):
# # #         while True:
# # #             menu_num = int(input("Enter the menu number (0: isEmpty, 1: pop, 2: peek, 3: push, 4: size, 5: isNull, 6: exit): "))
# # #             if menu_num == 0:
# # #                 print(self.isEmpty())
# # #             elif menu_num == 1:
# # #                 print(self.pop())
# # #             elif menu_num == 2:
# # #                 print(self.peek())
# # #             elif menu_num == 3:
# # #                 item = int(input("Enter the number to push: "))
# # #                 self.push(item)
# # #             elif menu_num == 4:
# # #                 print(self.size())
# # #             elif menu_num == 5:
# # #                 print(self.isNull())
# # #             elif menu_num == 6:
# # #                 break
# # #             else:
# # #                 print("Invalid menu number. Please try again.")

# # # # Example usage:
# # # stack = Stack()
# # # stack.stackMenu()















# class Stack:
#     def __init__(self, initial_list=None):
#         if initial_list is None:
#             self.list = []
#         else:
#             self.list = initial_list

#     def isEmpty(self):
#         return len(self.list) == 0

#     def isNull(self):
#         return self.list is None

#     def pop(self):
#         if self.isEmpty():
#             return "The list is empty"
#         return self.list.pop()

#     def peek(self):
#         if self.isEmpty():
#             return "The list is empty"
#         return self.list[-1]

#     def push(self, item):
#         self.list.append(item)

#     def size(self):
#         return len(self.list)

#     def display(self):
#         return self.list

#     def stackMenu(self):
#         while True:
#             menu_num = int(input("Enter the menu number (0: isEmpty, 1: pop, 2: peek, 3: push, 4: size, 5: isNull, 6: display, 7: exit): "))
#             if menu_num == 0:
#                 print(self.isEmpty())
#             elif menu_num == 1:
#                 print(self.pop())
#             elif menu_num == 2:
#                 print(self.peek())
#             elif menu_num == 3:
#                 item = int(input("Enter the number to push: "))
#                 self.push(item)
#             elif menu_num == 4:
#                 print(self.size())
#             elif menu_num == 5:
#                 print(self.isNull())
#             elif menu_num == 6:
#                 print(self.display())
#             elif menu_num == 7:
#                 break
#             else:
#                 print("Invalid menu number. Please try again.")













# # class TowerOfHanoi:
# #     def __init__(self, num_disks):
# #         self.num_disks = num_disks
# #         self.towers = [Stack(list(range(num_disks, 0, -1))), Stack(), Stack()]

# #     def move(self, from_tower, to_tower):
# #         if self.towers[from_tower].isEmpty():
# #             print(f"Cannot move from tower {from_tower} because it is empty")
# #             return
# #         if not self.towers[to_tower].isEmpty() and self.towers[to_tower].peek() < self.towers[from_tower].peek():
# #             print(f"Cannot move to tower {to_tower} because top disk is smaller than from tower {from_tower}")
# #             return
# #         disk = self.towers[from_tower].pop()
# #         self.towers[to_tower].push(disk)
# #         print(f"Moved disk {disk} from tower {from_tower} to tower {to_tower}")

# #     def display_towers(self):
# #         for i, tower in enumerate(self.towers):
# #             print(f"Tower {i}: {tower.display()}")

# #     def solve(self, n, from_tower, to_tower, aux_tower):
# #         if n == 1:
# #             self.move(from_tower, to_tower)
# #         else:
# #             self.solve(n-1, from_tower, aux_tower, to_tower)
# #             self.move(from_tower, to_tower)
# #             self.solve(n-1, aux_tower, to_tower, from_tower)

# #     def play(self):
# #         while True:
# #             self.display_towers()
# #             from_tower = int(input("Enter the tower number to move from (0, 1, 2) or -1 to solve: "))
# #             if from_tower == -1:
# #                 self.solve(self.num_disks, 0, 2, 1)
# #                 self.display_towers()
# #                 break
# #             to_tower = int(input("Enter the tower number to move to (0, 1, 2): "))
# #             self.move(from_tower, to_tower)

# # # Example usage:
# # tower_of_hanoi = TowerOfHanoi(3)
# # tower_of_hanoi.play()




import time

class Tower:
    def __init__(self):
        self.A = []
        self.B = []
        self.C = []
    
    def tower(self, item):
        self.A.append(item)
        time.sleep(1)
        print("A =", self.A)
        print("Items in Tower A\n")

    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(1)
        print("A =", self.A, "      ", "B =", self.B, "      ", "C =", self.C)
        print("Pass One Completed=================\n")

    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(1)
        print("A =", self.A, "      ", "B =", self.B, "      ", "C =", self.C)
        print("Pass Two Completed=================\n")

    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(1)
        print("A =", self.A, "      ", "B =", self.B, "      ", "C =", self.C)
        print("Pass Three Completed=================\n")
      
    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(1)
        print("A =", self.A, "      ", "B =", self.B, "      ", "C =", self.C)
        print("Pass Four Completed=================\n")

    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(1)
        print("A =", self.A, "      ", "B =", self.B, "      ", "C =", self.C)
        print("Pass Five Completed=================\n")
  
    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(1)
        print("A =", self.A, "      ", "B =", self.B, "      ", "C =", self.C)
        print("Pass Six Completed=================\n")
   
    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(1)
        print("A =", self.A, "      ", "B =", self.B, "      ", "C =", self.C)
        print("Pass Seven Completed=================\n")

# Example usage:
obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()


find common key value pair in two dictionaries write a function to find 
