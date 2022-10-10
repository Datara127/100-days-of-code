import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
count_right_answer = 0
states = data.state.to_list()
screen.tracer(0)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{count_right_answer}/50 States correct",
                                    prompt="What's another state's name?")
    if answer_state.lower() == "exit":
        missing_state = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        count_right_answer += 1
        states.remove(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.ht()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()
