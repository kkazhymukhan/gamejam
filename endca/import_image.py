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


    boss = [
    pygame.transform.scale(pygame.image.load("image/boss/boss.png"), (300, 200)),
    pygame.transform.scale(pygame.image.load("image/boss/boss1.png"), (300, 200)),
    pygame.transform.scale(pygame.image.load("image/boss/boss2.png"), (300, 200)),
    pygame.transform.scale(pygame.image.load("image/boss/boss3.png"), (300, 200))
    ]


    boss_bg=[
    pygame.transform.scale(pygame.image.load("image/boss_bg/boss1.png"), (600, 600)),
    pygame.transform.scale(pygame.image.load("image/boss_bg/boss11.png"), (600, 600)),
    pygame.transform.scale(pygame.image.load("image/boss_bg/boss2.png"), (600, 600)),
    pygame.transform.scale(pygame.image.load("image/boss_bg/boss3.png"), (600, 600)),
    pygame.transform.scale(pygame.image.load("image/boss_bg/boss4.png"), (600, 600)),
    pygame.transform.scale(pygame.image.load("image/boss_bg/boss5.png"), (600, 600)),
    pygame.transform.scale(pygame.image.load("image/boss_bg/boss6.png"), (600, 600)),
    pygame.transform.scale(pygame.image.load("image/boss_bg/boss7.png"), (600, 600)),
    pygame.transform.scale(pygame.image.load("image/boss_bg/boss8.png"), (600, 600)),
    pygame.transform.scale(pygame.image.load("image/boss_bg/boss9.png"), (600, 600)),
    pygame.transform.scale(pygame.image.load("image/boss_bg/boss10.png"), (600, 600))

    ]
    win=[
    pygame.transform.scale(pygame.image.load("image/win/win0.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/win/win1.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/win/win2.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/win/win3.png"), (800, 800)),
    ]

    cutscene=[
    pygame.transform.scale(pygame.image.load("image/cutscene/news0.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/news1.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/no0.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/no1.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/pixil-frame-7.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/pixil-frame-8.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/pixil-frame-9.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/pixil-frame-10.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/pixil-frame-11.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/pixil-frame-12.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/pixil-frame-13.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/pixil-frame-14.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/pixil-frame-15.png"), (800, 800)),
    pygame.transform.scale(pygame.image.load("image/cutscene/pixil-frame-16.png"), (800, 800))

    ]
