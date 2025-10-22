file = open ('youtube.txt','w')

try:
    file.write('Chai aur Code')
finally:
    file.close()

with open ('youtube.txt','w') as file:
    file.write('Chai aur python')
    