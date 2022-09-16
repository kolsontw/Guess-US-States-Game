import turtle
import pandas
from writer import Writer

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
w = Writer()

states = pandas.read_csv("50_states.csv")
guessed = 0
guessed_answer = []


while guessed < 50:
    answer_state = screen.textinput(title=f"{guessed}/50 States Correct", prompt="What's another state's name")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break

    if answer_state not in states["state"].tolist():
        continue
    elif answer_state in states["state"].tolist() and answer_state not in guessed_answer:
        guessed_answer.append(answer_state)
        guessed += 1
        x_cor = int(states[states.state == answer_state]["x"])
        y_cor = int(states[states.state == answer_state]["y"])
        w.wr(answer_state, x_cor, y_cor)


# Get coordinate of states

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()