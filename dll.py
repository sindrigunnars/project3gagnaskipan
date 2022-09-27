
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.sentinel = Node('Sentinel')
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.current = self.sentinel
        self.ordered = True
        self.size = 0

    def __str__(self):
        ret_val = ''
        if self.ordered:
            temp = self.sentinel.next
            while temp != self.sentinel:
                ret_val += str(temp.data) + ' '
                temp = temp.next
            return ret_val
        else:
            temp = self.sentinel.prev
            while temp != self.sentinel:
                ret_val += str(temp.data) + ' '
                temp = temp.prev
            return ret_val
    
    def __len__(self):
        return self.size

    def insert(self, value):
        if self.ordered:
            nn = Node(value, self.current.prev, self.current)
            self.current.prev.next = nn
            self.current.prev = nn
            self.current = nn
            self.size += 1
        else:
            nn = Node(value, self.current, self.current.next)
            self.current.next.prev = nn
            self.current.next = nn
            self.current = nn
            self.size += 1

    def remove(self):
        if self.ordered:
            if self.current != self.sentinel:
                self.current.prev.next, self.current.next.prev  = self.current.next, self.current.prev
                self.size -= 1
                self.current = self.current.next
        else:
            if self.current != self.sentinel:
                self.current.prev.next, self.current.next.prev  = self.current.next, self.current.prev
                self.size -= 1
                self.current = self.current.prev

    def get_value(self):
        if self.size == 0:
            return None
        if self.current == self.sentinel:
            return None
        return self.current.data

    def move_to_next(self):
        if self.ordered:
            if self.current != self.sentinel:
                self.current = self.current.next
        else:
            if self.current != self.sentinel:
                self.current = self.current.prev

    def move_to_prev(self):
        if self.ordered:
            if self.current.prev != self.sentinel:
                self.current = self.current.prev
        else:
            if self.current.next != self.sentinel:
                self.current = self.current.next

    def move_to_pos(self, pos):
        if self.ordered:
            if 0 <= pos <= self.size:
                self.current = self.sentinel.next
                for _ in range(pos):
                    self.current = self.current.next
        else:
            if 0 <= pos <= self.size:
                self.current = self.sentinel.prev
                for _ in range(pos):
                    self.current = self.current.prev

    def remove_all(self, value):
        if self.ordered:
            temp = self.sentinel.next
            while temp != self.sentinel:
                if temp.data == value:
                    temp.prev.next, temp.next.prev = temp.next, temp.prev
                    self.size -= 1
                    if temp == self.current:
                        self.move_to_pos(0)
                temp = temp.next
        else:
            temp = self.sentinel.prev
            while temp != self.sentinel:
                if temp.data == value:
                    temp.prev.next, temp.next.prev = temp.next, temp.prev
                    self.size -= 1
                    if temp == self.current:
                        self.move_to_pos(0)
                temp = temp.prev

    def reverse(self):
        if self.ordered:
            self.ordered = False
        else:
            self.ordered = True
        self.move_to_pos(0)
        # if self.sentinel.next == self.sentinel:
        #     return
        # temp = self.sentinel.prev
        # while temp != self.sentinel:
        #     temp.next, temp.prev = temp.prev, temp.next
        #     temp = temp.next
        # self.sentinel.next, self.sentinel.prev, self.current = self.sentinel.prev, self.sentinel.next, self.sentinel.prev

    def sort(self):
        if self.ordered:
            if self.sentinel.next == self.sentinel:
                return
            current = self.sentinel.next
            while current != self.sentinel:
                i = current.next
                while i != self.sentinel:
                    if current.data > i.data:
                        current.data, i.data = i.data, current.data
                    i = i.next
                current = current.next
            self.move_to_pos(0)
        else:
            if self.sentinel.prev == self.sentinel:
                return
            current = self.sentinel.prev
            while current != self.sentinel:
                i = current.prev
                while i != self.sentinel:
                    if current.data > i.data:
                        current.data, i.data = i.data, current.data
                    i = i.prev
                current = current.prev
            self.move_to_pos(0)






