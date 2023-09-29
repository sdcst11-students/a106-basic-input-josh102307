answer = input("Who are you:")

print(f"The input was {answer}")
print(f"the input is of type: {type(answer)}")

answer = int(answer)
print(f"the answer is now of type {type(answer)}")
print(3*answer)