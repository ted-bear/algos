from stack.task4 import Stack

def is_valid_brackets(brackets):
    """
    Exercise 4.5/6. Проверка скобочной последовательности

    Рефлексия: Самое сложное в этой классической задаче, продумать
    все тесты, чтобы учесть наибольшее количество вариантов, сам
    несколько раз попадался на то, что не учитывал, что может быть
    последовательность только из закрывающихся скобок и неправильно
    делал проверки

    Time complexity: O(n)
    Memory complexity: O(n)
    """
    opening = Stack()
    for bracket in brackets:
        if bracket == '(' or bracket == '[' or bracket == '{':
            opening.push(bracket)
        else:
            if opening.size() == 0:
                return False
            last_open = opening.peek()
            if (last_open == '(' and bracket == ')'
                or last_open == '[' and bracket == ']'
                or last_open == '{' and bracket == '}'):
                opening.pop()
            else:
                return False
    return opening.size() == 0