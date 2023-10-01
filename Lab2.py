def generate_sublists(input_list):
    result = []

    for num in input_list:

        sublist = list(range(num + 1))
        result.append(sublist)

    return result

input_list = [1, 2, 3, 10]
result = generate_sublists(input_list)
print(result)

# Написать функцию, которая принимает целочисленный
# список, состоящий из n элементов, и возвращает список,
# состоящий из новых списков, элементами которых являются числа
# от 0 до значений элемента во входящем списке включительно.
# Например, входящий список имеет вид [1,2,3] на выходе будет
# список списков [[0,1], [0,1,2], [0,1,2,3]].