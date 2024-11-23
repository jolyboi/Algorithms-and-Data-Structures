# def main():
#     n = int(input())
#     mistakes = 0
#     dictionary = {}
#     for i in range(n):
#         word = str(input())
#         for j in range(len(word)):  # can do that since the length of each word is 10 max
#             if word[j] != word[j].lower():
#                 position = j
#                 break
#         if word.lower() not in dictionary:
#             dictionary[word.lower()] = {position}
#         else:
#             dictionary[word.lower()].add(position)
#
#     text = str(input()).split(' ')
#     for word in text:
#         count = 0
#         position = -1
#         for j in range(len(word)):
#             if word[j] != word[j].lower():
#                 count += 1
#                 position = j
#         if count != 1:
#             mistakes += 1
#             continue
#         if word.lower() in dictionary:
#             if position not in dictionary[word.lower()]:
#                 mistakes += 1
#
#     return mistakes
#
#
# print(main())


def main():
    n = int(input())
    words = {}
    mistakes = 0

    for i in range(n):
        word = input()
        base_form = word.lower()
        if base_form not in words:
            words[base_form] = set()
        words[base_form].add(word)
    for word in input().split():
        base_form = word.lower()
        uppercase_counter = len([l for l in word if l.isupper()])
        if (base_form in words and word not in words[base_form]) or uppercase_counter != 1:
            mistakes += 1

    return mistakes


print(main())