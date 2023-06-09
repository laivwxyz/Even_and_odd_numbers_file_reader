# Dela Cruz, Lailanie E. _ BSCpE 1-4
# Assignment 4
# Programming Exercises 1

# Write a Python program that reads a text file named numbers.txt that contains 20 integers. The program will create two other text file; 
# the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. The second text file will be named 
# odd.txt that will contains all odd numbers extracted from the numbers.txt.

def even_odd():
    # creating text files named numbers.txt (read), even.txt (append), odd.txt (append)
    with open("numbers.txt") as input_file, \
         open("even.txt", "a") as output_even, \
         open("odd.txt", "a") as output_odd:
        # read numbers.txt line by line
        for line in input_file:
            input_num = int(line)
            # if even,
            if input_num % 2 == 0:
                # extract it from even.txt
                output_even.write(str(input_num) + "\n")
            # if odd,
            else:
                # extract it from odd.txt
                output_odd.write(str(input_num) + "\n")

# ==start ==
even_odd()