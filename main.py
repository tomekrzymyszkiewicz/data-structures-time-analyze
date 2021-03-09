from time import perf_counter_ns
import csv
import random
import array as arr
import os
from msvcrt import getch
data_array = []
result_array = []
menu_message = """==========================================
### PRORGAM DO ANALIZY STRUKTUR DANYCH ###
###    AUTOR: TOMASZ RZYMYSZKIEWICZ    ###
==========================================
1. GENERUJ DANE DO PLIKU CSV
2. WCZYTAJ DANE Z PLIKU CSV
3. ZAPISZ WYNIKI DO PLIKU CSV
4. PRZEPROWADŹ TEST OPERACJI NA TABLICY
5. PRZEPROWADŹ TEST OPERACJI NA LIŚCIE
6. PRZEPROWADŹ TEST OPERACJI NA STOSIE
7. PRZEPROWADŹ TEST OPERACJI NA KOLEJCE
ESC. WYJDŹ Z PROGRAMU"""


class Result:
    data_structure = "null"
    operation = "null"
    size_of_structure = 0
    time_of_operation = 0

    def __init__(self, data_structure, operation, size_of_structure, time_of_operation):
        self.data_structure = data_structure
        self.operation = operation
        self.size_of_structure = size_of_structure
        self.time_of_operation = time_of_operation


def save_results():
    with open('results.csv', newline='', mode='w') as result_file:
        field_names = ['data_strucutre', 'operation',
                       'size_of_structure', 'time_of_operation']
        result_writer = csv.DictWriter(result_file, fieldnames=field_names)
        result_writer.writeheader()
        for i in range(len(result_array)):
            result_writer.writerow({'data_strucutre': result_array[i].data_structure, 'operation': result_array[i].operation,
                                    'size_of_structure': result_array[i].size_of_structure, 'time_of_operation': result_array[i].time_of_operation})


def load_data(amount):
    with open('data.csv', mode='r') as data_file:
        data_reader = csv.reader(data_file)
        rows = list(data_reader)
        if amount > len(rows):
            return False
        for row in range(amount):
            data_array.append(int(rows[row][0]))
        return True


def generate_data(amount):
    with open('data.csv', newline='', mode='w') as data_file:
        data_writer = csv.writer(
            data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(amount):
            random_number = random.randint(-1000000, 1000000)
            data_writer.writerow([random_number])


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def remove(self, data):
        this_node = self.head
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head = this_node
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, data):
        this_node = self.head
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None

    def print(self):
        temp = self.head
        while (temp):
            print(temp.data, " -> ", end='')
            temp = temp.next_node
        print("")


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)
        return data

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def is_empty(self):
        return len(self.elements) == 0


def stack_operations(size_of_stack):
    # CREATE OPERATION
    t_start = perf_counter_ns()
    stack = Stack()
    for i in range(size_of_stack):
        stack.push(data_array[i])
    t_stop = perf_counter_ns()
    t_create = t_stop-t_start
    # PUSH OPERATION
    random_value = random.randint(-1000000, 1000000)
    t_start = perf_counter_ns()
    stack.push(random_value)
    t_stop = perf_counter_ns()
    t_push = t_stop-t_start
    # POP OPERATION
    t_start = perf_counter_ns()
    stack.pop()
    t_stop = perf_counter_ns()
    t_pop = t_stop-t_start
    # PEEK OPERATION
    t_start = perf_counter_ns()
    stack.peek()
    t_stop = perf_counter_ns()
    t_peek = t_stop-t_start
    result_array.append(Result("stack", "create", size_of_stack, t_create))
    result_array.append(Result("stack", "push", size_of_stack, t_push))
    result_array.append(Result("stack", "pop", size_of_stack, t_pop))
    result_array.append(Result("stack", "peek", size_of_stack, t_peek))


def linked_list_operations(size_of_linked_list):
    # CREATE OPERATION
    t_start = perf_counter_ns()
    linked_list = LinkedList()
    for i in range(size_of_linked_list):
        linked_list.add(data_array[i])
    t_stop = perf_counter_ns()
    t_create = t_stop-t_start
    # ADD OPERATION
    random_value = random.randint(-1000000, 1000000)
    t_start = perf_counter_ns()
    linked_list.add(random_value)
    t_stop = perf_counter_ns()
    t_add = t_stop-t_start
    # DELETE OPERATION (with find)
    random_index = random.randint(0, size_of_linked_list-1)
    random_value = data_array[random_index]
    t_start = perf_counter_ns()
    linked_list.remove(random_value)
    t_stop = perf_counter_ns()
    t_delete = t_stop-t_start
    # SEARCH OPERATION
    random_index = random.randint(0, size_of_linked_list-1)
    random_value = data_array[random_index]
    t_start = perf_counter_ns()
    linked_list.find(random_value)
    t_stop = perf_counter_ns()
    t_search = t_stop-t_start
    result_array.append(Result("linked_list", "create",
                               size_of_linked_list, t_create))
    result_array.append(Result("linked_list", "add",
                               size_of_linked_list, t_add))
    result_array.append(Result("linked_list", "delete",
                               size_of_linked_list, t_delete))
    result_array.append(Result("linked_list", "search",
                               size_of_linked_list, t_search))


def array_operations(size_of_array):
    # CREATE OPERATION
    t_start = perf_counter_ns()
    array = [0]*size_of_array
    for i in range(size_of_array):
        array[i] = data_array[i]
    t_stop = perf_counter_ns()
    t_create = t_stop-t_start
    # PUT OPERATION
    random_index = random.randint(0, size_of_array-1)
    t_start = perf_counter_ns()
    array[random_index] = 0
    t_stop = perf_counter_ns()
    t_put = t_stop-t_start
    # ADD OPERATION
    random_value = random.randint(-1000000, 1000000)
    t_start = perf_counter_ns()
    new_array = [0]*(size_of_array+1)
    for i in range(size_of_array):
        new_array[i] = array[i]
    new_array[size_of_array] = random_value
    array = new_array
    t_stop = perf_counter_ns()
    t_add = t_stop-t_start
    # SEARCH OPERATION
    random_index = random.randint(0, size_of_array-1)
    searched_value = array[random_index]
    t_start = perf_counter_ns()
    for i in range(size_of_array):
        if(searched_value == array[i]):
            t_stop = perf_counter_ns()
            break
    t_search = t_stop-t_start
    # DELETE OPERATION
    random_index = random.randint(0, size_of_array-1)
    t_start = perf_counter_ns()
    new_array = [0]*(size_of_array-1)
    for i in range(0, random_index):
        new_array[i] = array[i]
    for i in range(random_index+1, size_of_array-1):
        new_array[i] = array[i+1]
    array = new_array
    t_stop = perf_counter_ns()
    t_delete = t_stop-t_start
    # RESULT SECTION
    result_array.append(Result("array", "create", size_of_array, t_create))
    result_array.append(Result("array", "put", size_of_array, t_put))
    result_array.append(Result("array", "add", size_of_array, t_add))
    result_array.append(Result("array", "delete", size_of_array, t_delete))
    result_array.append(Result("array", "search", size_of_array, t_search))


def read_range():
    s = ""
    print(s.join((
        "Podaj zakres danych, na których chcesz przeprowadzić test operacji [1,", str(len(data_array)), "]")))
    range_beginning = int(input("Podaj początek zakresu (min. 1): "))
    range_end = int(
        input(s.join(("Podaj koniec zakresu (max. ", str(len(data_array)), "): "))))
    if range_beginning < 1 | len(data_array) < range_end:
        print("Wybrany zakres jest nieprawidłowy")
        print("Naciśnij ENTER, aby kontytnuować...")
        input()
        return [-1]
    else:
        return [range_beginning, range_end]


def main():
    while True:
        os.system('cls')
        print(menu_message)
        key = ord(getch())
        if key == 27:  # ESC
            quit()
        elif key == 49:  # 1
            amount = int(input("Ilość liczb do wygenerowania: "))
            if amount < 1:
                print("Wybrana wartość jest nieprawidłowa")
                print("Naciśnij ENTER, aby kontytnuować...")
                input()
            else:
                generate_data(amount)
                print("Wygenerowano ", amount, "liczb i zapisano w pliku CSV")
                print("Naciśnij ENTER, aby kontytnuować...")
                input()
        elif key == 50:  # 2
            amount = input("Ilość liczb do załadowania: ")
            if load_data(int(amount)):
                print("Wczytano", amount, "liczb z pliku")
            else:
                print("Nie można wczytać podanej ilości liczb")
            print("Naciśnij ENTER, aby kontytnuować...")
            input()
        elif key == 51:  # 3
            save_results()
            print("Zapisano wszystkie wyniki wygenerowane w tej sesji działania programu")
            print("Naciśnij ENTER, aby kontytnuować...")
            input()
        elif key == 52:  # 4
            input_range = read_range()
            if input_range[0] != -1:
                for i in range(input_range[0], input_range[1]+1):
                    array_operations(i)
                print("Testy ", input_range[1]-input_range[0]+1,
                      " elementów przeprowadzono prawidłowo")
                print("Naciśnij ENTER, aby kontytnuować...")
                input()
        elif key == 53:  # 5
            input_range = read_range()
            if input_range[0] != -1:
                for i in range(input_range[0], input_range[1]+1):
                    linked_list_operations(i)
                print("Testy ", input_range[1]-input_range[0]+1,
                      " elementów przeprowadzono prawidłowo")
                print("Naciśnij ENTER, aby kontytnuować...")
                input()
        elif key == 54:  # 6
            input_range = read_range()
            if input_range[0] != -1:
                for i in range(input_range[0], input_range[1]+1):
                    stack_operations(i)
                print("Testy ", input_range[1]-input_range[0]+1,
                      " elementów przeprowadzono prawidłowo")
                print("Naciśnij ENTER, aby kontytnuować...")
                input()


main()
