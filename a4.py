h =  int(input("Enter your time"))

if 5 <= h < 12:
    msg = "Morning"
    
elif 12 <= h < 16:
    msg = "Afternoon"
    
elif 16 <= h < 19:
    msg = "Evening"

elif 19 <= h < 23:
    msg = "Night" 
    
print("Good",msg)
