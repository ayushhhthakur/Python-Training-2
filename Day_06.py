#wap to check whether a number is sphenic or not
# def find_factors(number):
#     factors = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             factors.append(i)
#     return factors

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def is_sphenic(n):
#     if n < 30:
#         return False
    
#     prime_factors = []
#     for i in range(2, n+1):
#         if is_prime(i) and n % i == 0:
#             prime_factors.append(i)
#             if len(prime_factors) > 3:
#                 return False
#     return len(prime_factors) == 3

# num = int(input("Enter a number: "))
# factors = find_factors(num)
# print(f"The factors of {num} are:", factors)

# if is_sphenic(num):
#     print(f"{num} is a sphenic number.")
# else:
#     print(f"{num} is not a sphenic number.")


#wap to check if a number is neon or not
# def is_neon_number(number):
#     square = number * number
#     digit_sum = sum(int(digit) for digit in str(square))
#     return digit_sum == number

# num = int(input("Enter a number: "))

# if is_neon_number(num):
#     print(f"{num} is a neon number.")
# else:
#     print(f"{num} is not a neon number.")


#wap to check if a number is perfect or not
# def is_perfect_number(number):
#     if number <= 0:
#         return False
    
#     divisors = [1] 
    
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             divisors.append(i)
#             if i != number // i: 
#                 divisors.append(number // i)
    
#     return sum(divisors) == number

# num = int(input("Enter a number: "))

# if is_perfect_number(num):
#     print(num, "is a perfect number.")
# else:
#     print(num, "is not a perfect number.")

#wap to check if a number is autobiographical or not
def is_autobiographical(number):
    count = [0] * 10  # Since digits are from 0 to 9

    # Count the occurrences of each digit
    for digit in str(number):
        count[int(digit)] += 1

    # Compare the counts with the digits
    return count == [int(digit) for digit in str(number)]

# Get input from the user
num = int(input("Enter a number: "))

if is_autobiographical(num):
    print(num, "is an autobiographical number.")
else:
    print(num, "is not an autobiographical number.")
