date = input("Enter a date in the following format 'mm/dd/yyyy': ")
div = date.split("/")
num = int(div[0])
month = {1:"January", 2:"February", 3:"March", 4:"April",
        5:"May", 6:"June", 7:"July", 8:"August",
        9:"September", 10:"October", 11:"November", 12:"December"}
print (f"{month[num]} {div[1]} {div[2]}")