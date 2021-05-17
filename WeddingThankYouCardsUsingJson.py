import json
import random

### IMPORTANT!!!!!!!!!!! ###
#make sure guestDictionary.txt and weddingThankYou.txt are downloaded before running.
###IMPORTANT!!!!!!!!!!!!!###

#Use this to convert file of nested dictionary of guests into a nested dictionary (use JSON format)
with open('guestDictionary.txt') as file:
    x = file.read()
    variable = json.loads(x)
    print(variable)
    print(variable['Guests'])
    guestList = []
    for i in range(0, len(variable['Guests'])):
        guestList.append(f"Guest{i+1}")

#This function converts the name of the guests
def nameChange(y):
    for guest in guestList:
        name = (y['Guests'][f"{guest}"]['name'])
        nameSplit = name.split(" ")
        firstName = nameSplit[0]
        with open('weddingThankYou.txt') as letter:
            contents = letter.read()
            new = contents.replace('(name)', firstName)
            with open(f"{name}'s_letter.txt", mode="w") as newLetter:
                newLetter.write(new)

#This function tests if the guest gave a gift, and writes a message accordingly.
def giftChange(y):
    for guest in guestList:
        name = (y['Guests'][f"{guest}"]['name'])
        gift = (y['Guests'][f"{guest}"]['gift'])
        print(gift)
        print(type(gift))
        if gift.lower() != 'none':
            with open(f"{name}'s_letter.txt") as letter:
                contents = letter.read()
                new = contents.replace('(gift)', gift)
                print(new)
                with open(f"{name}'s_letter.txt", mode="w") as newLetter:
                    newLetter.write(new)
        if gift.lower() == 'none':
            with open(f"{name}'s_letter.txt") as letter:
                contents = letter.read()
                new = contents.replace('(gift) you gave us', 'memories you helped us make')
                with open(f"{name}'s_letter.txt", mode="w") as newLetter:
                    newLetter.write(new)

#This function randomly selects a food from the food at the wedding, and writes it into the letter.

def foodChange(y):
    foodList = ["Spaghetti and MeatBalls", "Steak and Broccoli", "Chicken and Rice"]
    for guest in guestList:
        name = (y['Guests'][f"{guest}"]['name'])
        food = foodList[random.randint(0, (len(foodList) - 1))]
        with open(f"{name}'s_letter.txt") as letter:
            contents = letter.read()
            new = contents.replace('(food)', food)
            print(new)
            with open(f"{name}'s_letter.txt", mode="w") as newLetter:
                newLetter.write(new)


def htmlConvert(y):
    for guest in guestList:
        name = (y['Guests'][f"{guest}"]['name'])
        preBody = '''
        <!DOCTYPE html>
            <html lang="en">
                <head>
    <meta charset="UTF-8">
    <title>(name)</title>
</head>
<body>
'''
        header = f'<h1>{name}</h1>'
        with open(f"{name}'s_letter.txt") as letter:
            content = letter.read()
        paragraph = f'<p><pre>{content}</pre></p>'
        postBody = '''
        </body>
</html>
'''
        contents = (preBody + header + paragraph + postBody)

        with open(f"{name}'s_letter.html", mode="w") as newLetter:
            newLetter.write(contents)

nameChange(variable)
giftChange(variable)
foodChange(variable)
htmlConvert(variable)
