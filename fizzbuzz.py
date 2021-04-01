# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the 
# number and for the multiples of five print “Buzz”. For 
# numbers which are multiples of both three and five print
# “FizzBuzz”.

def fizzbuzz(i):
        fizz = ((i)%3 == 0)
        buzz = ((i)%5 == 0)
        if fizz and buzz:
            return "fizzbuzz"
        elif fizz:
            return "fizz"
        elif buzz:
            return "buzz"
        else:
            return i

if __name__ == '__main__':
    for i in range(1,101):
        print(fizzbuzz(i))