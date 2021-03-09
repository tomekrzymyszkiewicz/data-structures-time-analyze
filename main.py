from time import perf_counter_ns
import csv
import random
import os
import configparser
from msvcrt import getch
data_array = []
result_array = []


class Result:

    def __init__(self, data_structure, operation, size_of_structure, time_of_operation):
        self.data_structure = data_structure
        self.operation = operation
        self.size_of_structure = size_of_structure
        self.time_of_operation = time_of_operation


def save_results(result_config_file_name):
    with open(result_config_file_name, newline='', mode='w') as result_file:
        field_names = ['data_strucutre', 'operation',
                       'size_of_structure', 'time_of_operation_ns']
        result_writer = csv.DictWriter(result_file, fieldnames=field_names)
        result_writer.writeheader()
        for i in range(len(result_array)):
            result_writer.writerow({'data_strucutre': result_array[i].data_structure, 'operation': result_array[i].operation,
                                    'size_of_structure': result_array[i].size_of_structure, 'time_of_operation_ns': result_array[i].time_of_operation})


def load_data(file_name, amount):
    if os.path.exists(file_name):
        with open(file_name, mode='r') as data_file:
            data_reader = csv.reader(data_file)
            rows = list(data_reader)
            if amount > len(rows):
                return False
            for row in range(amount):
                data_array.append(int(rows[row][0]))
            return True
    else:
        return False


def generate_data(file_name, amount):
    with open(file_name, newline='', mode='w') as data_file:
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


class List(object):
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


def queue_operations(size_of_queue):
    # CREATE OPERATION
    t_start = perf_counter_ns()
    queue = []
    for i in range(size_of_queue):
        queue.append(data_array[i])
    t_stop = perf_counter_ns()
    t_create = t_stop-t_start


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


def list_operations(size_of_list):
    # CREATE OPERATION
    t_start = perf_counter_ns()
    list = List()
    for i in range(size_of_list):
        list.add(data_array[i])
    t_stop = perf_counter_ns()
    t_create = t_stop-t_start
    # ADD OPERATION
    random_value = random.randint(-1000000, 1000000)
    t_start = perf_counter_ns()
    list.add(random_value)
    t_stop = perf_counter_ns()
    t_add = t_stop-t_start
    # DELETE OPERATION (with find)
    random_index = random.randint(0, size_of_list-1)
    random_value = data_array[random_index]
    t_start = perf_counter_ns()
    list.remove(random_value)
    t_stop = perf_counter_ns()
    t_delete = t_stop-t_start
    # SEARCH OPERATION
    random_index = random.randint(0, size_of_list-1)
    random_value = data_array[random_index]
    t_start = perf_counter_ns()
    list.find(random_value)
    t_stop = perf_counter_ns()
    t_search = t_stop-t_start
    result_array.append(Result("list", "create",
                               size_of_list, t_create))
    result_array.append(Result("list", "add",
                               size_of_list, t_add))
    result_array.append(Result("list", "delete",
                               size_of_list, t_delete))
    result_array.append(Result("list", "search",
                               size_of_list, t_search))


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


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    data_config_file_name = config['data']['file_name']
    data_config_amount = int(config['data']['amount'])

    if load_data(data_config_file_name, data_config_amount):
        print("Data loaded from", data_config_file_name, "successfully")
    else:
        print("Data loading error. A new", data_config_file_name,
              "file with", data_config_amount, "elements will be generated")
        generate_data(data_config_file_name, data_config_amount)
        load_data(data_config_file_name, data_config_amount)
        print("Done")

    print()
    for i in config['tasks']:
        current_taks = config['tasks'][i].split(' ')
        task_structure = current_taks[0]
        task_start_range = int(current_taks[1])
        task_stop_range = int(current_taks[2])
        task_range_step = int(current_taks[3])
        if len(current_taks) == 5:
            task_repeat = int(current_taks[4])
        else:
            task_repeat = 1
        print("Task on", task_structure, "in data range from", task_start_range,
              "to", task_stop_range, "with step", task_range_step, "made", task_repeat, "time")
        if task_stop_range > len(data_array):
            print("Not enought loaded data to execute task")
        else:
            if task_structure == 'array':
                try:
                    for current_size_of_structure in range(task_start_range, task_stop_range, task_range_step):
                        for repeat in range(task_repeat):
                            array_operations(current_size_of_structure)
                    print("Done")
                except:
                    print("Error")
            elif task_structure == 'list':
                try:
                    for current_size_of_structure in range(task_start_range, task_stop_range, task_range_step):
                        for repeat in range(task_repeat):
                            list_operations(current_size_of_structure)
                    print("Done")
                except:
                    print("Error")
            elif task_structure == 'stack':
                try:
                    for current_size_of_structure in range(task_start_range, task_stop_range, task_range_step):
                        for repeat in range(task_repeat):
                            stack_operations(current_size_of_structure)
                    print("Done")
                except:
                    print("Error")
            elif task_structure == 'queue':
                try:
                    for current_size_of_structure in range(task_start_range, task_stop_range, task_range_step):
                        for repeat in range(task_repeat):
                            queue_operations(current_size_of_structure)
                    print("Done")
                except:
                    print("Error")
            else:
                print("Task not recognized")

    print()
    result_config_file_name = config['results']['file_name']
    save_results(result_config_file_name)
    print("Results saved to", result_config_file_name)
    print("Press any key to exit...")
    getch()


main()
