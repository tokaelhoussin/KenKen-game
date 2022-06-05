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
