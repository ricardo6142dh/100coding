numbers = [10, 15, 3, 7]
num = 10

i = 0


while i <= len(numbers)-1:
    j = i + 1    
    while j <= len(numbers) -1:
        total = numbers[i] + numbers[j]
        print(f"numbers[{i}] + numbers[{j}] == {total}")
        if total == num:
            print("True")
            break
        else:
            j = j + 1
    i = i + 1
