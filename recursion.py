# def say_hello(name):
#     print('Hello, {}'.format(name))
#     say_hello(name)

# say_hello('Rome')

# def countdown(num):
#     # base case
#     if num == 0:
#         print("Blast off!")
#         return
#     # recursive step
#     print(num)
#     countdown(num - 1)

# countdown(10)

# def countdown(num):
#     #base case
#     if num == 0:
#         print('Blast off!')
#         return
#     elif num < 0:
#         print('Please add a positive and try again')
#         return
    
#     # recursive step
#     print(num)
#     countdown(num -1)

# countdown(100)
# countdown(-10)

number = [1,2,3,4,5]
def add_number(numbers_array, result=0):
    # result = 0
    #return what u took out
    num = numbers_array.pop()
    result += num
    #base case
    print('The length of array is {}'.format(len(numbers_array)))
    if len(numbers_array) == 0:
        print(result)
        return result
    
    # recursive step
    return add_number(numbers_array, result)

print(add_number(number))