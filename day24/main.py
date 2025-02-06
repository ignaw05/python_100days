with open("Names/invited_names.txt", "r") as file:
    lista = file.readlines()

for line in lista:
    name = line.strip()
    print(name)
    with open(f"Ready/ready_{name}.docx","a") as ready:
        with open("Letters/starting_letter.txt","r") as file2:
            text = file2.read()
            text = text.replace("[Name]",name)
            ready.write(text)