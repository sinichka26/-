time = int(input("Enter a number of seconds: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Time formate чч:мм:сс   {hours} : {minutes} : {seconds}")