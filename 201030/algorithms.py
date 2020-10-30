# 1. Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements.
def moveZeros(arr):
    if __name__ == "__main__": 
        arr = [1, 2, 0, 4, 3, 0, 5, 0] 
    print (moveZeros(arr))

def pushZerosToEnd(arr, n): 
    count = 0
    for i in range(n): 
        if arr[i] != 0:
            arr[count] = arr[i] 
            count+=1
    while count < n: 
        arr[count] = 0
        count += 1

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
n = len(arr) 
pushZerosToEnd(arr, n) 
print("Array after pushing all zeros to end of array:") 
print(arr) 

# 2. Write a function that counts the number of times the number 7 occurs in a given integer without converting it to a string. For example the number 7,704,793 would output 3
# Note: following answer not in python3
# function countSevens(num) {
#     if (typeof num === 'number') {
#         let n = Math.abs(num) // take absolute value, store in placeholder
#         let count = 0; // initialize count
#         while (n > 0) {
#             let rem = n % 10 // find digit in ones place
#             if (rem === 7) { count ++ } // increase count if remainder equals 7
#             n = (n - rem) / 10 // remove ones place, decrease placeholder
#         }
#         console.log('Not of ${num} = ${count}')
#     }
#     else { console.log('Not a number!') }
# }
# countSevens(7704793)
# countSevens(7777)
# countSevens(508264321946)
My_number = 7704793

def seven_count(number):
    number_of_sevens = 0
    n = abs(number)
    while n > 0:
        remeinder = n % 10
        if remainder == 7:
            number_of_sevens += 1
        n = (n - remainder) / 10
    return number_of_sevens

print(seven_count(my_number))

# 3. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Examples and clarification here: https://leetcode.com/problems/two-sum/
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Because nums[0] + nums[1] == 9, we return [0, 1].

some_list = [1,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2]
target = 3
#soultion should be indices [0,1] 
def sum_of_indices(arr,n):
    new_list = list(set(arr)) #this removes duplicate values
    this_is_list = [] #this will be my returned list of indices
    for number1 in new_list: 
        for number2 in new_list:#nested loops to loop over all values
            if number1 != number2: #don't want to check the same number
                sum_list = [] #initialized each time loop is run 
                sum_list.extend([number1, number2]) # exted the list
                sum_list = sum(sum_list) #sum list
                if sum_list == n: #check if list meets target value
                    print(sum_list)
                    this_is_list.extend([some_list.index(number1), some_list.index(number2)]) #when it does, extend the list with the indices of orig list
                    print(this_is_list)
                    return this_is_list
​
​
sum_of_indices(some_list,target)
