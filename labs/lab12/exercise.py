'''
# Using break - stops when found
for number in range(10):
    print(f'Checking: {number}')
    if number > 7:
        print(f'Found first number > 7: {number}')
        break  # Stop searching

print('Search complete')
'''

# Using continue - processes all, reports only numbers > 7
for number in range(10):
    if number <= 7:
        continue  # Skip numbers <= 7
    print(f'Number greater than 7: {number}')  # Reports 8 and 9

print('Processing complete')