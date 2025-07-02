try:
    marks={"alice":85,"kk":75,"bob":88,"tom":45}

    name=input("Enter the student's name:")

    print(f"{name}'s marks: {marks[name]}")
except Exception as e:
    print("student not found")

