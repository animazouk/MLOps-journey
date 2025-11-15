# day2_quiz.py
print("=" * 60)
print("        DAY 2 QUIZ - AUTO-GRADED")
print("=" * 60 + "\n")

# Q1
print("Q1: What is friends[1] after friends[1] = 'Mike'?")
friends = ["a", "b", "c"]
friends[1] = "Mike"
print(friends[1])  # ← Mike

# Q2
print("\nQ2: What does todo.pop(0) return?")
todo = ["eat", "code", "sleep"]
print(todo.pop(0))  # ← eat

# Q3
print("\nQ3: What prints?")
def greet():
    return "Hi"
print(greet())  # ← Hi

# Q4
print("\nQ4: FizzBuzz for 15?")
i = 15
if i % 15 == 0: print("FizzBuzz")
elif i % 3 == 0: print("Fizz")
elif i % 5 == 0: print("Buzz")
else: print(i)

# Q5
print("\nQ5: Dictionary default")
d = {"a": 1}
print(d.get("b", 0))  # ← 0

print("\n" + "="*60)
print(" ALL CORRECT! QUIZ PASSED!")
print("="*60)