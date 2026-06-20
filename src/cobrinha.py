import pygame

def sprite_cobrinha(size):
    verde_escuro = (40, 160, 70)
    verde_claro = (90, 220, 120)
    amarelo = (210, 170, 60)
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    
    cabeça = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.ellipse(cabeça, verde_escuro, (2, 4, size - 4, size - 8))
    pygame.draw.circle(cabeça, branco, (size - 12, size // 2 - 7), 5)
    pygame.draw.circle(cabeça, branco, (size - 12, size // 2 + 7), 5)
    pygame.draw.circle(cabeça, preto, (size - 12, size // 2 - 7), 2)
    pygame.draw.circle(cabeça, preto, (size - 12, size // 2 + 7), 2)
    
    corpo = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.rect(corpo, verde_escuro, (3,3, size -6, size -6), border_radius = 12)
    pygame.draw.circle(corpo, verde_claro, (size // 2, size // 2), size // 5)
    
    rabo = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.polygon( rabo, verde_escuro, [(4,8), (size - 14, size // 2), (4, size - 8)])
    pygame.draw.circle(rabo, amarelo, (size - 10, size // 2), 7)
    pygame.draw.circle(rabo, amarelo, (size - 4, size // 2), 5)

    return {"cabeça": cabeça, "corpo": corpo, "rabo": rabo}

def girar_cobrinha(img, dir):
    dx, dy = dir
    
    if dx > 0:
        ang = 0
    elif dx < 0 :
        ang = 180
    elif dy < 0:
        ang = 90
    else:
        ang =-90
    return pygame.transform.rotate(img, ang)

def movimento_cobrinha(cobrinha, dir, crescer):    
    cabeça_x, cabeça_y = cobrinha[0]
    cabeça_nova = (
        cabeça_x + dir[0], cabeça_y + dir[1]
    )

    if crescer:
        cobrinha.insert(0, cabeça_nova)
    else:
        cobrinha.insert(0, cabeça_nova)
        cobrinha.pop()
    
    return cobrinha

def desenho_cobrinha(tela, cobrinha, dir, sprites, size):
    for i, pos in enumerate(cobrinha):
        rect = pygame.Rect(pos[0], pos[1], size, size )
        if i == 0:
            img = girar_cobrinha(sprites["cabeça"], dir)
        elif i == len(cobrinha) - 1:
            parte_anterior = cobrinha[-2]
            rabo = cobrinha[-1]
            
            dir_rabo = (rabo[0] - parte_anterior[0], rabo[1] - parte_anterior[1])
            img = girar_cobrinha(sprites["rabo"], dir_rabo)
        
        else:
            img = sprites["corpo"]
            
        tela.blit(img, rect)

def diminuir_cobrinha(cobrinha): 
    cobrinha.pop()
    return cobrinha