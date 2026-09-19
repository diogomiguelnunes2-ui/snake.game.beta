# pyright: reportMissingImports=false
import random
import tkinter as tk

SIZE = 400
CELL = 20
root = tk.Tk()
root.title("Snake")
canvas = tk.Canvas(root, width=SIZE, height=SIZE, bg="black")
canvas.pack()

snake = [(200, 200)]
direction = (20, 0)
food = (random.randrange(0, 400, 20), random.randrange(0, 400, 20))

def set_direction(new_direction):
    global direction
    if new_direction != (-direction[0], -direction[1]):
        direction = new_direction


def update():
    global food
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if (head[0] < 0 or head[0] >= 400 or head[1] < 0 or head[1] >= 400
            or head in snake):
        root.destroy()
        return

    snake.insert(0, head)
    if head == food:
        free = [(x, y) for x in range(0, 400, 20)
                for y in range(0, 400, 20) if (x, y) not in snake]
        if not free:
            root.destroy()
            return
        food = random.choice(free)
    else:
        snake.pop()

    canvas.delete("all")
    canvas.create_rectangle(food[0], food[1], food[0] + CELL,
                            food[1] + CELL, fill="red")
    for segment in snake:
        canvas.create_rectangle(segment[0], segment[1], segment[0] + CELL,
                                segment[1] + CELL, fill="green")
    root.after(100, update)

root.bind("<Up>", lambda event: set_direction((0, -CELL)))
root.bind("<Down>", lambda event: set_direction((0, CELL)))
root.bind("<Left>", lambda event: set_direction((-CELL, 0)))
root.bind("<Right>", lambda event: set_direction((CELL, 0)))
root.focus_force()
update()
root.mainloop()