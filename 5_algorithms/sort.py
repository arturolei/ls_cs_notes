from book import Book
import time
import csv

def insertion_sort(books):
    # TO-DO: implement insertion sort 
    # Assume input "books" is a list 
    # created sorted list with item at index 0 of books
    # Take next one and start looping over books from index 1 to len(books) - 1 --> For Loop
        # Compare element to LHS while element is smaller, swap! --> WHile loop
        # If at front or element not smaller, got to top of loop
        # This should be done iteratively over the LHS
    # Grab last element, swap if need be (iterate)
    for i in range (1, len(books)):
        #compare each element to LHS, while element is smaller, swap
        j = i
        while j >= 1 and books[j].title < books[j-1].title:
            #swap
            temp = books[j]
            book[j] = books[j-1]
            books[j-1] = temp
            j-=1

    return books


# Version A: Conventional, recursive Quick Sort
def quick_sort_A( books, low, high ):
    # TO-DO: implement Quick Sort

    return books


# Version B:
# NOT done in place because for large inputs, we
# exceed Python's maximum recursion depth with 
# in-place Quick Sort
def quick_sort_B( books ):
    # STRETCH: implement Quick Sort for larger datasets

    return books


def book_sort(books):
    # STRETCH: combine Insertion & Quick Sort for
    # an improved sorting algorithm
    
    return books

# Read in book data from CSV file
# provided by https://github.com/uchidalab/book-dataset
with open('book_data.csv', encoding='utf8') as csvfile:
    my_books_long = []
    data = csv.DictReader(csvfile)
    for book in data:
        #print(book['title'], book['author'], book['genre'])
        my_books_long.append(Book(book['title'], book['author'], book['genre']))
    my_books_medium = my_books_long[0:997]
    my_books_short = my_books_long[0:10]

print("***********~Test with 10 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_short)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = quick_sort_A(my_books_short, 0, len(my_books_short))
# end = time.time()
# print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")


print("\n***********~Test with ~1,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_medium)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = quick_sort_A(my_books_medium, 0, len(my_books_medium))
# end = time.time()
# print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")


print("\n**********~Test with +2,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_long)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = quick_sort_B(my_books_long)
# end = time.time()
# print("Quick Sort (B) took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = book_sort(my_books_long)
# end = time.time()
# print("Book Sort took:       " + str((end - start)*1000) + " milliseconds\n")

# Breakout Room, How to Organize?
#  
# Bubble Sort (Not the fastest but mentally/physically easiest)
# 1. Put all books on the shelf 
# 2. Look at first two. Put book that goes first on left
# 3. Continue swapping like so until all are swapped
#
# Questions:
# How are these books organized? What is organization of the store? 
# What is the end goal where are these books going? Broken done into categories? 
# Are there multiple copies of the same book? (If these are books for college courses)
# 