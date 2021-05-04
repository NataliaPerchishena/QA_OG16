A = 45
V = 3
B = int(input('Please enter the B: '))
while B < A:
    print('No, B<A, next B=', B+V)
    B += V
    if B >= A:
        print('You are a winner!')
        break
