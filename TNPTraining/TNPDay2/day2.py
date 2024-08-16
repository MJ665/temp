# # class Queue:
# #     def __init__(self):
# #         self.items = []

# #     def is_empty(self):
# #         return len(self.items) == 0

# #     def enqueue(self, item):
# #         self.items.append(item)

# #     def dequeue(self):
# #         if self.is_empty():
# #             raise IndexError("Dequeue from an empty queue")
# #         return self.items.pop(0)

# #     def peek(self):
# #         if self.is_empty():
# #             raise IndexError("Peek from an empty queue")
# #         return self.items[0]

# #     def size(self):
# #         return len(self.items)

# #     def __str__(self):
# #         return 'Queue: ' + str(self.items)

# # def menu():
# #     q = Queue()
# #     while True:
# #         print("\nQueue Operations Menu")
# #         print("1. Enqueue")
# #         print("2. Dequeue")
# #         print("3. Peek")
# #         print("4. Check if Empty")
# #         print("5. Size")
# #         print("6. Display Queue")
# #         print("7. Exit")

# #         choice = input("Enter your choice (1-7): ")

# #         if choice == '1':
# #             item = input("Enter item to enqueue: ")
# #             q.enqueue(item)
# #             print(f"Enqueued: {item}")
# #         elif choice == '2':
# #             try:
# #                 dequeued_item = q.dequeue()
# #                 print(f"Dequeued: {dequeued_item}")
# #             except IndexError as e:
# #                 print(e)
# #         elif choice == '3':
# #             try:
# #                 front_item = q.peek()
# #                 print(f"Front item: {front_item}")
# #             except IndexError as e:
# #                 print(e)
# #         elif choice == '4':
# #             if q.is_empty():
# #                 print("Queue is empty")
# #             else:
# #                 print("Queue is not empty")
# #         elif choice == '5':
# #             print(f"Size of queue: {q.size()}")
# #         elif choice == '6':
# #             print(q)
# #         elif choice == '7':
# #             print("Exiting...")
# #             break
# #         else:
# #             print("Invalid choice! Please choose a valid option.")

# # if __name__ == "__main__":
# #     menu()













# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self._size = 0

#     def is_empty(self):
#         return self.front is None

#     def enqueue(self, item):
#         new_node = Node(item)
#         if self.rear is None:
#             self.front = self.rear = new_node
#         else:
#             self.rear.next = new_node
#             self.rear = new_node
#         self._size += 1

#     def dequeue(self):
#         if self.is_empty():
#             raise IndexError("Dequeue from an empty queue")
#         temp = self.front
#         self.front = temp.next
#         if self.front is None:
#             self.rear = None
#         self._size -= 1
#         return temp.data

#     def peek(self):
#         if self.is_empty():
#             raise IndexError("Peek from an empty queue")
#         return self.front.data

#     def size(self):
#         return self._size

#     def __str__(self):
#         result = []
#         current = self.front
#         while current:
#             result.append(current.data)
#             current = current.next
#         return 'Queue: ' + ' -> '.join(map(str, result))

# def menu():
#     q = Queue()
#     while True:
#         print("\nQueue Operations Menu")
#         print("1. Enqueue")
#         print("2. Dequeue")
#         print("3. Peek")
#         print("4. Check if Empty")
#         print("5. Size")
#         print("6. Display Queue")
#         print("7. Exit")

#         choice = input("Enter your choice (1-7): ")

#         if choice == '1':
#             item = input("Enter item to enqueue: ")
#             q.enqueue(item)
#             print(f"Enqueued: {item}")
#         elif choice == '2':
#             try:
#                 dequeued_item = q.dequeue()
#                 print(f"Dequeued: {dequeued_item}")
#             except IndexError as e:
#                 print(e)
#         elif choice == '3':
#             try:
#                 front_item = q.peek()
#                 print(f"Front item: {front_item}")
#             except IndexError as e:
#                 print(e)
#         elif choice == '4':
#             if q.is_empty():
#                 print("Queue is empty")
#             else:
#                 print("Queue is not empty")
#         elif choice == '5':
#             print(f"Size of queue: {q.size()}")
#         elif choice == '6':
#             print(q)
#         elif choice == '7':
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice! Please choose a valid option.")

# if __name__ == "__main__":
#     menu()
















class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.val:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None or current.val == key:
            return current
        if key < current.val:
            return self._search(current.left, key)
        return self._search(current.right, key)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.val)
            self._in_order_traversal(node.right, result)

    def __str__(self):
        return 'Binary Tree In-Order: ' + ' -> '.join(map(str, self.in_order_traversal()))

def menu():
    bt = BinaryTree()
    while True:
        print("\nBinary Tree Operations Menu")
        print("1. Insert")
        print("2. Search")
        print("3. In-Order Traversal")
        print("4. Display Tree")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            key = int(input("Enter key to insert: "))
            bt.insert(key)
            print(f"Inserted: {key}")
        elif choice == '2':
            key = int(input("Enter key to search: "))
            result = bt.search(key)
            if result:
                print(f"Found: {key}")
            else:
                print(f"Key {key} not found")
        elif choice == '3':
            print("In-Order Traversal:", bt.in_order_traversal())
        elif choice == '4': 
            print(bt)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    menu()
