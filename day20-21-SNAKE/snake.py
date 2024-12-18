from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_LENGTH = 20

class Snake:
    def __init__(self):
        self.blocks = []
        self.create_blocks()
        self.head = self.blocks[0]

    def create_blocks(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)

    def add_block(self,position):
        new_block = Turtle(shape="square")
        new_block.penup()
        new_block.color("white")
        new_block.goto(position)
        self.blocks.append(new_block)

    def add_tail(self):
        self.add_block(self.blocks[-1].pos())
        self.add_block(self.blocks[-1].pos())
        self.add_block(self.blocks[-1].pos())

    def move(self):
        for block_num in range(len(self.blocks)-1,0,-1):
            pos_x = self.blocks[block_num - 1].xcor()
            pos_y = self.blocks[block_num - 1].ycor()
            self.blocks[block_num].goto((pos_x,pos_y))
        self.head.forward(MOVE_LENGTH)

    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)
