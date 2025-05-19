with open("mail.txt") as mail:
    mail = mail.read()
    
with open("names.txt") as names:
    names = names.read().split('\n')
    
for name in names:
    sendable = mail.replace("[name]", name.capitalize())
    with open(f"./output/mail_to_{name.lower()}.txt", mode="w") as m:
        m.write(sendable)