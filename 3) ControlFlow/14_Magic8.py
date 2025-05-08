import random as r

Question = input("Ask a question: ")

random_ans = ["Yes - definitely.", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.",
"Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

print(f"Magic 8 Ball: {r.choice(random_ans)}")