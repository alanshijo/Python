import csv
key = ['No' , 'Company' , 'CarModel']
car = [{'No':'1' , 'Company':'Ferrari' , 'CarModel':'Roma'},
       {'No':'2' , 'Company':'Toyota' , 'CarModel':'Innova'},
       {'No':'3' , 'Company':'Maruti' , 'CarModel':'800'},
       {'No':'4' , 'Company':'Renault' , 'CarModel':'Dexter'},
       {'No':'5' , 'Company':'Volkswagen' , 'CarModel':'Polo'}]
with open('new.csv', 'w') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=key)
    write.writeheader()
    write.writerows(car)

with open('new.csv', newline='') as csvfile:
    d = csv.reader(csvfile, delimiter='|')
    for i in d:
        print(','.join(i))