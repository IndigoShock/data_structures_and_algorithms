from .node import Node


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
