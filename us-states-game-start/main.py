import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()  # keep screen open after click, alternative screen.exitonclick()

score = 0
guessed_states = []
data = pandas.read_csv("50_states.csv")
while len(guessed_states) < 50:
    answer_state= screen.textinput(title=f"Guess the State {score}/50", prompt="What's another state's name").title()
    state_exists = answer_state in data.state.values
    if answer_state == "Exit":
        missing_states = [state for state in data.state if  state not in guessed_states]
        # for state in data.state:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if state_exists and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        score +=1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.write(answer_state, font=("Verdana",7, "normal"))

turtle.mainloop()
#screen.exitonclick()

