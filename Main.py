#Program to reverse the same array
A = [1, 2, 3, 4, 5, 6]
#Initialising start and end
start = 0
end = len(A)-1

#Reverse A from start to end
while start < end:
    # Swapping the elements of an array to reverse it in the same array
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1

#Driver Code
print("Reversed array is")
print(A)
#text