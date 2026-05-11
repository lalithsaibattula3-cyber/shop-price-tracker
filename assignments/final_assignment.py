# -----student performance tracker-----
def student_performance():
    student = {
        "lalith": {"math": 85, "science": 90, "english": 78},
        "shashank": {"math": 95, "science": 90, "english": 80},
        "kc": {"math": 90, "science": 89, "english": 88},
        "prashan": {"math": 90, "science": 85, "english": 85}
    }

    averages = {}
    for name,subjects in student.items():
        marks = [m for m in subjects.values()if m is not None]
        avg = sum(marks)/ len(marks) if marks else 0
        averages[name] = round(avg,2)
        print(f"average = {averages[name]}")
        
    topper = max(averages,key=averages.get)
    print(f"\ntopper: {topper} with average {averages[topper]}")

student_performance()

#-----online shopping cart-----
def shopping_cart():
    cart = [
        {"item": "Dal",        "price": 120,  "qty": 2},
        {"item": "Rice",       "price": 60,   "qty": 5},
        {"item": "Oil",        "price": 180,  "qty": 1},
        {"item": "Masala",     "price": 85,   "qty": 3},
        {"item": "Atta",       "price": 55,   "qty": 2},
        {"item": "Soaps",      "price": 40,   "qty": 4},
        {"item": "Chocolates", "price": 50,   "qty": 6},
        {"item": "Biscuits",   "price": 30,   "qty": 3},
        {"item": "Dal",        "price": 120,  "qty": 2},   # duplicate
        {"item": "Soaps",      "price": 40,   "qty": 4},   # duplicate
        {"item": "Rice",       "price": 60,   "qty": 5},   # duplicate
    ]
    
    seen = {}
    a_cart = []
    for product in cart :
        if product["item"]