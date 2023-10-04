#This actually executes the code in amuni.py mainline (not within sample functions)
print("***Running imports within main")

from sample import amuni

def main():
    print("***Running main within sample")
    amuni.add_one(1)
    print("***And back in main within sample")

if __name__ == "__main__":
    # This block of code will only run if main.py is executed directly
    main()


    