import pygame
class image:
    hearts = [
    pygame.transform.scale(pygame.image.load("image/hearts/xp0.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp1.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp2.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp3.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp4.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp5.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp6.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp7.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp8.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp9.png"), (320, 60)),
    ]

    playerRun = [
    pygame.transform.scale(pygame.image.load("image/run/run1.png"), (100, 80)),
    pygame.transform.scale(pygame.image.load("image/run/run2.png"), (100, 80))
    ]

    enemyRun = [
    pygame.transform.scale(pygame.image.load("image/enemy/enemy1.png"), (90, 85)),
    pygame.transform.scale(pygame.image.load("image/enemy/enemy2.png"), (90, 85))
]

    playerHit = [
    pygame.transform.scale(pygame.image.load("image/hit/hit1.png"), (100, 80)),
    pygame.transform.scale(pygame.image.load("image/hit/hit2.png"), (100, 80))
    ]

    reverse_playerRun = [
    pygame.transform.flip(playerRun[0], True, False),
    pygame.transform.flip(playerRun[1], True, False)
    ]

    reverse_playerHit = [
    pygame.transform.flip(playerHit[0], True, False),
    pygame.transform.flip(playerHit[1], True, False)
    ]

    reverse_enemyRun = [
    pygame.transform.flip(enemyRun[0], True, False),
    pygame.transform.flip(enemyRun[1], True, False)
    ]
