import turtle
import pandas as pd
import datetime

screen = turtle.Screen()
screen.title("Guess Game")
bg = "blank_states_img.gif"
screen.addshape(bg)
screen.setup(725, 491)
turtle.shape(bg)
stats_cor = pd.read_csv("50_states.csv")
writer = turtle.Turtle()
writer.shape("turtle")
writer.penup()
writer.hideturtle()
score = 0
user_dict = []

# answer box
gameover = False
while not gameover:
    your_ans = screen.textinput(f"{score}/50 Guess Game", "Guess the state name: ").capitalize()

    get_location = stats_cor[stats_cor.state == your_ans]

    if not get_location.empty:
        writer.goto(get_location["x"].iloc[0], get_location["y"].iloc[0])
        writer.write(your_ans)
        score += 1
        new_entry = {'state': your_ans, 'x': get_location["x"].iloc[0], 'y': get_location["y"].iloc[0]}
        user_dict.append(new_entry)
    if score == 50:
        gameover = True
    
    if your_ans == "Exit":
        gameover = True
        screen.bye()

if gameover:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pd.DataFrame(user_dict).to_csv(f"history/your_score_{current_time}.csv", index=False)

    



# print(stats_cor[stats_cor.state == "Alabama"])

print(user_dict)
screen.mainloop()