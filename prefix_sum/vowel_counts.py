"""
Дана неизменная строка text из маленьких английских букв и список запросов (left, right).
Для каждого запроса посчитай буквы a, e, i, o, u с индекса left по right включительно.
Верни список ответов в том же порядке.

Например, для text = "banana":
- (1, 4) выбирает "anan" → 2 гласные;
- (0, 5) выбирает "banana" → 3;
- (2, 2) выбирает "n" → 0.
Значит, для queries = [(1, 4), (0, 5), (2, 2)] ответ — [2, 3, 0]



#   b a n a n a
#[  0,0,1,0,1,0,1]
#[  0,0,1,1,2,2,3] 1 4 3 - 1

banana
(1, 4), (0, 5), (2, 2)


prefixes =

1 -> (1, 4) anan -> 1(Y), 2(N), 3(Y), 4(N)
2 -> (1, 5) banana
3 -> (2, 2) n

"""


def vowel_counts(text, queries):
    prefix = [0]
    even = ("a", "e", "i", "o", "u")

    for char in text:
        contribution = 1 if char in even else 0
        prefix.append(prefix[-1] + contribution)

    answers = []
    for left, right in queries:
        answers.append(prefix[right + 1] - prefix[left])

    return answers


assert vowel_counts("banana", [(1, 4), (0, 5), (2, 2)]) == [2, 3, 0]
