
def main():
    due = 50

    while True:

        print(f"Amount Due : {due}")
        insert = int(input("Insert Coin: "))
        if insert == 25 or insert == 10 or insert == 5:
            due = due - insert
    
        if check(due):
            print(f"Change Owed: {abs(due)}")
            break
    
def check(due_val):
    return True if due_val <= 0 else False



main()