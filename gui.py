from inspect import trace
import pygame
import pygame_menu
import generate_board
from random import randint
import CSP
from pygame.locals import *
from sys import exit
import itertools
from timeit import default_timer



WIDTH = 800
WINDOW_SIZE=(800,800)
original_grid_element_color = (52, 31, 151)
background_color = (255,255,255)

size =['5']
algorithm=['1']
def run():
    running=True
    pause=False
    #assignment = CSP.backtracking_search(ken, inference=CSP.forward_checking)
    cliques = generate_board.generate(int(size[0]))
    
    ken = generate_board.Kenken(int(size[0]), cliques)
    ####calculate performance#####
    start1 = default_timer()
    assignment1 = CSP.backtracking_search(ken)
    duration1 = default_timer() - start1
    print("Time to compute Backtracking = ",duration1)


    start = default_timer()
    assignment2 = CSP.backtracking_search(ken, inference=CSP.forward_checking)
    duration = default_timer() - start
    print("Time to compute Forward checking = ",duration)
    

    start2 = default_timer()
    assignment3 = CSP.backtracking_search(ken, inference=CSP.AC3)
    duration2 = default_timer() - start2
    print("Time to compute Arc_Consistency = ",duration2)

    performance_100_cell(int(size[0]))
    ########################################### 

      
    gen = generate(cliques, int(size[0]))
    def solveit():
        Second_menu.disable()
        if int(algorithm[0]) == 1:
            assignment = CSP.backtracking_search(ken)
            print('1')
        elif int(algorithm[0]) == 2:
            assignment = CSP.backtracking_search(ken, inference=CSP.forward_checking)
            print('2')
        elif int(algorithm[0]) == 3:
            assignment = CSP.backtracking_search(ken, inference=CSP.AC3)
            print('3')
        ans=solve(cliques, int(size[0]),assignment)
    
        
    #menu.add.button('Solve', window = solve(cliques, int(size[0]),assignment))
    
    #ken.display(assignment) 
    #while tp keep it always running instead of timer
    #pygame offers different types of events
    while running:
        if pygame.key.get_pressed()[pygame.K_c]:
            menu.disable()
            pygame.init()
            game = pygame.display.set_mode((WIDTH, WIDTH))
            pygame.display.set_caption("kenken")
            game.fill(background_color)
            Second_menu = pygame_menu.Menu('Algorithm', 600, 300,
                       theme=pygame_menu.themes.THEME_BLUE)
            Second_menu.add.selector('Select Algorithm:', [('Choose',0),('Backtracking',1), ('forward_checking',2),('Arc_Consistency',3) ], onchange=set_algorithm)
            #print(cliques)
            Second_menu.add.button('Solve', solveit)
            Second_menu.mainloop(game)

            menu.enable()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #keydown means the keyboard is pressed
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running=False

def set_difficulty(value, difficulty:str) -> None:
    #global size
    size[0]=difficulty
    
    
def set_algorithm(value, algo:str) -> None:
    #global size
    algorithm[0]=algo    




def generate(cliques, size):
    pygame.init()
    game = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("kenken") 
    game.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 32)
    x =0 
    w=((WIDTH-100)//size)
    f_esc = myfont.render('Press c to choose the algoritm', True, (0, 0, 0))
    game.blit(f_esc, (int(WINDOW_SIZE[0] - f_esc.get_width()) / 2,10))
    colors= []
    for r  in range(20 ,255 , 80):
        for b  in range(0 ,255 , 80):
            for g  in range(10,255 , 80):
                colors.append((r,g,b))
    for clique in cliques:
        index ,op, target = clique
        color = colors[randint(0, len(colors)-1)]
        colors.remove(color) 
        for i in index:
            shape_surf = pygame.Surface(pygame.Rect(((50+w*(i[0]-1)) , (50+w*(i[1]-1)) ,w, w )).size,pygame.SRCALPHA )
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
            shape_surf.set_alpha(100)
            game.blit(shape_surf,((50+w*(i[0]-1)) , (50+w*(i[1]-1)) ,w, w) )
            


        value = myfont.render(str(target), True, (0,0,0))
        game.blit(value, (( (index[0][0]-1) *w )+55 ,((index[0][1]-1)*w )+55 ))
        if op != '.':
            value = myfont.render(op, True, (0,0,0))
            game.blit(value, (( (index[0][0]-1) *w )+ 70+15*len(str(target)) ,((index[0][1]-1)*w )+55 ))

        
    for i in range(size+1):
        pygame.draw.line(game, (0,0,0), (50 +w*i, 50), (50 + w*i ,750 ), 2 )
        pygame.draw.line(game, (0,0,0), (50, 50 + w*i), (750, 50 + w*i), 2 )
    pygame.display.update()

    
    return game

def solve(cliques, size,assignment):
    pygame.init()
    game = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("kenken") 
    game.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 32)
    x =0 
    w=((WIDTH-100)//size)
    f_esc = myfont.render('Press esc to play again', True, (0, 0, 0))
    game.blit(f_esc, (int(WINDOW_SIZE[0] - f_esc.get_width()) / 2,10))
    assign=list(assignment.values())
    out = list(itertools.chain(*assign))
    flag=0
    colors= []
    for r  in range(20 ,255 , 80):
        for b  in range(0 ,255 , 80):
            for g  in range(10,255 , 80):
                colors.append((r,g,b))  
    for clique in cliques:
        index ,op, target = clique
        color = colors[randint(0, len(colors)-1)]
        colors.remove(color) 
        for i in index:
            shape_surf = pygame.Surface(pygame.Rect(((50+w*(i[0]-1)) , (50+w*(i[1]-1)) ,w, w )).size,pygame.SRCALPHA )
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
            shape_surf.set_alpha(100)
            game.blit(shape_surf,((50+w*(i[0]-1)) , (50+w*(i[1]-1)) ,w, w) )
            value1 = myfont.render(str(out[flag]), True, (0,0,0))
            game.blit(value1, (( (i[0]-1) *w )+100 ,((i[1]-1)*w )+100 ))
            #game.blit(value1, (( (index[0][0]-1) *w )+55 ,((index[0][1]-1)*w )+55 ))
            flag=flag+1


        value = myfont.render(str(target), True, (0,0,0))
        game.blit(value, (( (index[0][0]-1) *w )+55 ,((index[0][1]-1)*w )+55 ))
        if op != '.':
            value = myfont.render(op, True, (0,0,0))
            game.blit(value, (( (index[0][0]-1) *w )+ 70+15*len(str(target)) ,((index[0][1]-1)*w )+55 ))

        
    for i in range(size+1):
        pygame.draw.line(game, (0,0,0), (50 +w*i, 50), (50 + w*i ,750 ), 2 )
        pygame.draw.line(game, (0,0,0), (50, 50 + w*i), (750, 50 + w*i), 2 )
    pygame.display.update()

    
    return game



def performance_100_cell(size):
    cliques = []
    total_time=0
    for i in range(100):
        cliques.append(generate_board.generate(size))

    for clique in cliques:
        ken = generate_board.Kenken(size, clique)
        start1 = default_timer()
        assignment1 = CSP.backtracking_search(ken)
        duration1 = default_timer() - start1
        total_time+=duration1

    avg_time = total_time / 100
    print("Average time to compute 100 cell using Backtracking = ",avg_time)
    
    total_time=0
    for clique in cliques:
        ken = generate_board.Kenken(size, clique)
        start1 = default_timer()
        assignment1 = CSP.backtracking_search(ken,inference=CSP.forward_checking)
        duration1 = default_timer() - start1
        total_time+=duration1

    avg_time = total_time / 100
    print("Average time to compute 100 cell using forward_checking = ",avg_time)

    total_time=0
    for clique in cliques:
        ken = generate_board.Kenken(size, clique)
        start1 = default_timer()
        assignment1 = CSP.backtracking_search(ken,inference=CSP.AC3)
        duration1 = default_timer() - start1
        total_time+=duration1

    avg_time = total_time / 100
    print("Average time to compute 100 cell using Arc_Consistency = ",avg_time)



if __name__ == "__main__":
    
    pygame.init()
    game = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("kenken")
    game.fill(background_color)
    menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)
    menu.add.selector('Size :', [('Choose',0),('3x3',3), ('4x4',4),('5x5',5),('6x6',6),('7x7',7),('8x8',8),('9x9',9) ], onchange=set_difficulty)
    #print(cliques)
    
    
    menu.add.button('Select', run)
    #menu.add.button('Play', run())

    menu.mainloop(game)
    
    
    #menu.add.button('Play', run())

    #Second_menu.disable()

    #print (assignment)

    #ken.display(assignment) 
    #window = draw(cliques, size)
    run()
