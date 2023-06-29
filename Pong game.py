import tkinter as tk

# Set up the window
window = tk.Tk()
window.title("Pong")

# Set up the canvas
canvas = tk.Canvas(window, width=800, height=600, bg="black")
canvas.pack()

# Create the paddles
paddle_a = canvas.create_rectangle(50, 250, 70, 350, fill="white")
paddle_b = canvas.create_rectangle(730, 250, 750, 350, fill="white")

# Create the ball
ball = canvas.create_oval(390, 290, 410, 310, fill="white")

# Set initial ball movement
ball_dx = 2
ball_dy = -2

# Set initial scores
score_a = 0
score_b = 0

# Create the score labels
score_label_a = canvas.create_text(100, 50, text="Player A: 0", fill="white", font=("Arial", 14))
score_label_b = canvas.create_text(700, 50, text="Player B: 0", fill="white", font=("Arial", 14))

# Function to move Paddle A up
def paddle_a_up(event):
    canvas.move(paddle_a, 0, -20)

# Function to move Paddle A down
def paddle_a_down(event):
    canvas.move(paddle_a, 0, 20)

# Function to move Paddle B up
def paddle_b_up(event):
    canvas.move(paddle_b, 0, -20)

# Function to move Paddle B down
def paddle_b_down(event):
    canvas.move(paddle_b, 0, 20)

# Bind keyboard events to paddle movement functions
canvas.bind_all("w", paddle_a_up)
canvas.bind_all("s", paddle_a_down)
canvas.bind_all("<Up>", paddle_b_up)
canvas.bind_all("<Down>", paddle_b_down)

# Update the score labels
def update_scores():
    canvas.itemconfig(score_label_a, text="Player A: " + str(score_a))
    canvas.itemconfig(score_label_b, text="Player B: " + str(score_b))

# Check collision with paddles and update ball movement
def check_collision():
    global ball_dx, ball_dy, score_a, score_b
    ball_pos = canvas.coords(ball)
    paddle_a_pos = canvas.coords(paddle_a)
    paddle_b_pos = canvas.coords(paddle_b)

    if ball_pos[0] <= paddle_a_pos[2] and paddle_a_pos[1] <= ball_pos[1] <= paddle_a_pos[3]:
        ball_dx *= -1
    elif ball_pos[2] >= paddle_b_pos[0] and paddle_b_pos[1] <= ball_pos[1] <= paddle_b_pos[3]:
        ball_dx *= -1
    elif ball_pos[1] <= 0 or ball_pos[3] >= 600:
        ball_dy *= -1
    elif ball_pos[0] <= 0:
        score_b += 1
        update_scores()
        canvas.coords(ball, 390, 290, 410, 310)
        ball_dx *= -1
    elif ball_pos[2] >= 800:
        score_a += 1
        update_scores()
        canvas.coords(ball, 390, 290, 410, 310)
        ball_dx *= -1

    canvas.move(ball, ball_dx, ball_dy)

    # Check for game over
    if score_a >= 5 or score_b >= 5:
        canvas.unbind_all("w")
        canvas.unbind_all("s")
        canvas.unbind_all("<Up>")
        canvas.unbind_all("<Down>")
        canvas.create_text(400, 300, text="Game Over!", fill="white", font=("Arial", 30))

# Main game loop
def game_loop():
    check_collision()
    window.after(10, game_loop)

update_scores()
game_loop()
window.mainloop()
