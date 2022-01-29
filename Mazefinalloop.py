from XLMaze import check_avl, show
from MAZEfinal import MazeSolving, MazeBack, MazeRun

Explore = MazeSolving()

i = 0
pos_x = 0
pos_y = 0
Set = 1
count = 1
path = []

solved = False
back = False
run = False

while solved == False:
    Explore.turn(Set,pos_x,pos_y)
    r_avlb, f_avlb, l_avlb = check_avl(Set,pos_y,pos_x, 2)
    r_avlb,f_avlb,l_avlb = Explore.check(r_avlb, f_avlb, l_avlb)
    Next, Nextcell = Explore.nextmove(r_avlb,f_avlb,l_avlb, pos_y, pos_x)
    Explore.countindex(Nextcell, pos_x, pos_y)
    pos_x, pos_y, Set = Explore.move(Next,Set, pos_x, pos_y)
    print(f"y: {pos_y} x: {pos_x} Set: {Set}")
    solved = Explore.end(pos_y,pos_x)
    

# show(Explore.Maze)
print(Explore.Maze)
Back = MazeBack(Explore.Maze, pos_y, pos_x)

if Set == 5:
    Set = 1
elif Set == 6:
    Set = 2
elif Set == 0:
    Set = 4

while back == False:
    Back.turn(Set, pos_x, pos_y)
    r_avlb, f_avlb, l_avlb = check_avl(Set,pos_y,pos_x, 3)
    r_avlb,f_avlb,l_avlb = Back.check(r_avlb, f_avlb, l_avlb)
    Next, Nextcell = Back.nextmove(r_avlb,f_avlb,l_avlb, pos_y, pos_x)
    Back.countindex(Nextcell, pos_x, pos_y)
    pos_x, pos_y, Set = Back.move(Next,Set, pos_x, pos_y)
    print(f"y: {pos_y} x: {pos_x} Set: {Set}")
    back = Back.end(pos_y, pos_x)

Back.countindex(Nextcell, pos_x, pos_y)
print(Back.Maze)

RuN = MazeRun(Back.Maze, 25)

print(RuN.path)

Set = Set + 2
if Set == 5:
    Set = 1
elif Set == 6:
    Set = 2
elif Set == 0:
    Set = 4

while run == False:
    RuN.turn(Set, pos_x, pos_y)
    r_avlb, f_avlb, l_avlb = check_avl(Set,pos_y,pos_x, 4)
    r_avlb,f_avlb,l_avlb = RuN.check(r_avlb, f_avlb, l_avlb)
    Next, Nextcell = RuN.nextmove(r_avlb,f_avlb,l_avlb, pos_y, pos_x)
    pos_x, pos_y, Set = RuN.move(Next,Set, pos_x, pos_y)
    print(f"y: {pos_y} x: {pos_x} Set: {Set}")
    run = RuN.end(pos_y, pos_x)