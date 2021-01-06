import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S STATE GAME")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
correct = 0
state_guess = []


while len(state_guess) < 50:
    
    user_answer = turtle.textinput(f"GUESS THE STATE ({correct}/50)", "What is another state: ").title()
    if user_answer == "Exit":
        learn_data = [state for state in state_list if state not in state_guess]
        # for state in state_list:
        #     if state not in  state_guess:
        #         learn_data.append(state)

        data = pandas.DataFrame(learn_data)
        data.to_csv("./learn_state.csv")
    break


    if user_answer in state_list:
        correct +=1
        user_answer_state_data = data[data["state"]==user_answer]
        t = turtle.Turtle() 
        t.ht()
        t.penup()
        t.goto(int(user_answer_state_data.x),int(user_answer_state_data.y))
        t.write(user_answer)
        state_guess.append(user_answer)


        
        
    turtle.mainloop()


