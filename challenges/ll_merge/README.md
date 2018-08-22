# Merge two Linked Lists
Merge two linked lists.
## Challenge
The challenge is to merge two linked lists together. Note that each are assumed to be unsorted. The way we approached this is to identify the heads on each of the linked lists. We'll say ll1 and ll2 from now on. We also have temp nodes for each on the next value from the current on each. We will be calling each tmp1 and tmp2. So the temps will find out if the next one is null and if it is, the nodes from the second list will be added to the first list iteratively via while loop.
Once completed through the while loop with the condition both tmp1 and tmp2 point to None, assign the last node back to the main list again so it is not left hanging. Return the first current node again.

## Solution
![MergeLL](../../assets/merge_ll.jpg)​

## Acknowledgements
Worked with Madeline Peters, Nick Damberg, Christopher Chapman, and me, Stephen Harper
