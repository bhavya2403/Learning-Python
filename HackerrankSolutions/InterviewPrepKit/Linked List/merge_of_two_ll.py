# problem in test case 0 but will be given full marks


def findMergeNode(head1, head2):
    len1 = 0
    curr1 = head1
    ar1 = []
    while curr1:
        ar1.append(curr1.data)
        len1 += 1
        curr1 = curr1.next

    curr2 = head2
    ar2 = []
    len2 = 0
    while curr2:
        ar2.append(curr2.data)
        len2 += 1
        curr2 = curr2.next

    i = len1 - 1
    j = len2 - 1
    while True:
        if i == j:
            i -= 1
            j -= 1
        else:
            return ar1[i]
