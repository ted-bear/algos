from stack.task4 import Stack, HeadStack


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

def evaluate_in_postfix(expression):
    """
    Exercise 4.9. Вычислить выражение в постфиксной записи

    Рефлексия: Опять спотыкаюсь о типизацию, выглядит несложно,
    но много мелких деталей, о которых нужно на забыть

    Time complexity: O(n)
    Memory complexity: O(n)
    """
    if len(expression) == 0:
        return None
    el_stack = HeadStack()
    exp_stack = place_to_stack(expression)
    cur_el = exp_stack.pop()
    while cur_el != '=':
        if cur_el == '+':
            el_1 = int(el_stack.pop())
            el_2 = int(el_stack.pop())
            new_el = el_1 + el_2
            el_stack.push(new_el)
        elif cur_el == '*':
            el_1 = int(el_stack.pop())
            el_2 = int(el_stack.pop())
            new_el = el_1 * el_2
            el_stack.push(new_el)
        else:
            el_stack.push(cur_el)
        cur_el = exp_stack.pop()
    return el_stack.pop()

def place_to_stack(expression):
    stack = HeadStack()
    arr = expression.split(' ')
    for i in range(len(arr) - 1, -1, -1):
        stack.push(arr[i])
    return stack