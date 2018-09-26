# First repeated word
Find the first repeated word in a book.

## Challenge
The challenge is to find the repeated word. A hashtable is used for this problem because it is easier to organize the words in the book. The hashtable holds key-value pairs. In this case, the key is the word while the counter is the value. While any key's value in the hashtable is less than 2, continue pushing the words into the hashtable. Once any of the key's value reaches 2, then return that word. If none of the words have any repeats, then return a message saying no repeats. This is assuming the book is not empty.

## Solution
![RepeatedWord](../../assets/repeated_word.jpg)​
