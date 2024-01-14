## Write a method that displays all the numbers from 10 to 1000 that are divisible by 5 and 6. 

def display_numbers_divisible_by_5_and_6():
    # Iterate through numbers from 10 to 1000
    for num in range(10, 1001):
        # Check if the number is divisible by both 5 and 6
        if num % 5 == 0 and num % 6 == 0:
            # Display the number
            print(num)

# Call the method to display the numbers
display_numbers_divisible_by_5_and_6()
