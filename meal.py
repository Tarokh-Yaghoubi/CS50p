# Meal Time Program 

def main():
    time = input("Enter the time , in this format 00:00 ")
    convert(time)
    
    
def convert(time):
    hour , minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    
    if 7 <= hour <= 8 and 00 <= minute < 60:
        print(f"{hour}:{minute} is breakfast time")
if __name__ == "__main__":
    main()