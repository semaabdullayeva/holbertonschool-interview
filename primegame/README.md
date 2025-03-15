# **PrimeGame ! :snake:**

Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a **prime number** from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game. We assume - ladies first - that Maria always goes first.

To determine which of Ben or Maria will win, we call our greek friend through the function `greek_fiesta()` which basically take advantage of the **Sieves of Eratosthene** -> we compute the list of prime numbers up to `n` (the 'amount' in each 'bucket' of the list of integers `nums`).

If number of primes is odd from 2 to n => we know Maria which always goes first wins the Game round <br>
On the other hand, if number of primes from 2 to n is even => Ben wins the game round
