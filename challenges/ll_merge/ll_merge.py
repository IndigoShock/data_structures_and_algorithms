from ll_merge import Node


def merge(ll_one, ll_two):
    ll_one.current = ll_one.head
    ll_two.current = ll_two.head

    Node.tmp1 = ll_one.head
    Node.tmp2 = ll_two.head

    tmp1 = ll_one.current._next
    tmp2 = ll_two.current._next

    while tmp1 is not None and tmp2 is not None:
        print(ll_one.current)
        ll_one.current._next = ll_two.current
        ll_two.current._next = tmp1
        ll_one.current = tmp1
        ll_two.current = tmp2

    ll_one.current._next = ll_two.current

    return ll_one.current


# def ll_merge(ll_one, ll_two):
#     try:
#         ll_one_current = ll_one.head
#         ll_two_current = ll_two.head

#         while ll_one_current is not None and ll_two_current is not None:
#             ll_one_next = ll_one_current._next
#             ll_two_next = ll_two_current._next

#             ll_one_current._next, ll_two_current._next = ll_two_next, ll_one_next
#             ll_one_current = ll_one_next
#         ll_two.head = ll_two_current

#     except None:
#         'Not valid input'
