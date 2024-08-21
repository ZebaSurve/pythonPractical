for num in range(1,101):
    if num%3==0:
        print(f"Fizz {num}")
    elif num%5==0:
        print(f"Buzz {num}")
    if num%5==0 and num%3==0:
        print(f"FizzBuzz {num}")


