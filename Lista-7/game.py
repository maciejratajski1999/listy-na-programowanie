import sys, pygame
from note import Note
from song import Song
from timer import Timer
from score import Score
pygame.init()
pygame.mixer.init()

size = width, height = 960, 540
speed = [0, 6]
background = 120, 22, 10
blue = 10, 50, 130
grey = 110, 130, 130
black = 0, 10, 10
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hit Em Notes")

drumstick = pygame.mixer.Sound("resources\\drumstick.wav")
highstick = pygame.mixer.Sound("resources\\highstick.wav")
kickdrum = pygame.mixer.Sound("resources\\kickdrum.wav")

def game_text(content, font, color):
    ingame_text = font.render(content, True, color)
    return ingame_text, ingame_text.get_rect()

def game_start():
    score = Score()
    intro = 1
    while intro == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                collision(mouse_pos)
        screen.fill(background)
        metal_text = pygame.font.Font('freesansbold.ttf', 71)
        metal_sprite, metal_rect = game_text("Metal", metal_text, black)
        metal_rect.center = 300, 270
        metal_button = pygame.draw.circle(screen, grey, metal_rect.center, 100)
        metal_score = pygame.font.Font('freesansbold.ttf', 55)
        metal_score_sprite, metal_score_rect = game_text(str(score.metal), metal_score, black)
        metal_score_rect.center = 300, 400

        blues_text = pygame.font.Font('freesansbold.ttf', 71)
        blues_sprite, blues_rect = game_text("Blues", blues_text, black)
        blues_rect.center = 660, 270
        blues_button = pygame.draw.circle(screen, blue, blues_rect.center, 100)
        blues_score = pygame.font.Font('freesansbold.ttf', 55)
        blues_score_sprite, blues_score_rect = game_text(str(score.blues), blues_score, black)
        blues_score_rect.center = 660, 400

        def collision(pos):
            if metal_button.collidepoint(pos):
                game_song("metal")
            if blues_button.collidepoint(pos):
                game_song("blues")


        screen.blit(metal_sprite, metal_rect)
        screen.blit(blues_sprite, blues_rect)
        screen.blit(metal_score_sprite, metal_score_rect)
        screen.blit(blues_score_sprite, blues_score_rect)
        pygame.display.flip()

def aftergame(score):
    score_font = pygame.font.Font('freesansbold.ttf', 55)
    sprite, rect = game_text("your score: " + str(score), score_font, grey)
    rect.center = 480, 270
    for i in range(0,180):
        screen.blit(sprite, rect)
        pygame.time.Clock().tick_busy_loop(60)
        pygame.display.flip()



def game_song(key):

    downboard = pygame.image.load("resources\\downboard.png")
    downboard_rect = downboard.get_rect()
    downboard_rect.center = (width/2, height-100)
    score_font = pygame.font.Font('freesansbold.ttf', 33)

    def get_song(key):
        song = Song(key)
        return Timer(song.bpm), song.tab, song.length, song.background_sounds, song.user_sounds, song.bg_image

    song_timer, overtab, length, bg_sounds, user_sounds, bg_image_path = get_song(key)

    bg_image = pygame.image.load(bg_image_path)
    bg_image = pygame.transform.scale(bg_image, (300,640))
    bg_image_rect = bg_image.get_rect()
    bg_image_rect.center = (width/2, height/2)

    def new_tab(index):
        try:
            tab = overtab[index]
            notes = [Note(letter, bg_sounds) for letter in tab]
            if len(notes) == 0:
                notes = [Note(None, bg_sounds)]
            sprites = [(pygame.image.load(note.image), note.pos) for note in notes]
            ingame_positions = [pos for image, pos in sprites]
            ingame_notes = [image.get_rect() for image, pos in sprites]
            try:
                ingame_sounds = [[pygame.mixer.Sound(note.sound)] for note in notes]
            except TypeError:
                ingame_sounds = [[]]
            ingame_keys = [note.key for note in notes]
            for i in range(0, len(ingame_notes)):
                ingame_notes[i].x = ingame_positions[i]
                ingame_notes[i].y = -100
            return sprites, ingame_notes, ingame_sounds, ingame_keys
        except IndexError:
            return [], [], [], []


    all_sprites, all_notes, all_sounds, all_keys = [], [], [], []
    score = 0
    loop = 1
    while loop:
        frame_sounds = []
        note_check = []
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT : sys.exit()
            elif keys[pygame.K_q]:
                frame_sounds.append(pygame.mixer.Sound(user_sounds["Q"]))
                note_check.append("Q")
            elif keys[pygame.K_w]:
                frame_sounds.append(pygame.mixer.Sound(user_sounds["W"]))
                note_check.append("W")
            elif keys[pygame.K_e]:
                frame_sounds.append(pygame.mixer.Sound(user_sounds["E"]))
                note_check.append("E")
            elif keys[pygame.K_r]:
                frame_sounds.append(pygame.mixer.Sound(user_sounds["R"]))
                note_check.append("R")
        if song_timer.tab_index > length and len(all_notes) == 0:
            aftergame(score)
            Score().save(score, key)
            game_start()

        if song_timer.check():
            song_timer.tab_index_up()
            sprites, ingame_notes, ingame_sounds, ingame_keys = new_tab(song_timer.tab_index)
            for new_sprite in sprites:
                all_sprites.append(new_sprite)
            for new_note in ingame_notes:
                all_notes.append(new_note)
            for new_sound in ingame_sounds:
                all_sounds.append(new_sound)
            for new_key in ingame_keys:
                all_keys.append(new_key)

            if (song_timer.tab_index % 2) == 0:
                all_sounds[-1].append(drumstick)
            if ((song_timer.tab_index + 1) % 8) == 0:
                all_sounds[-1].append(highstick)
            if ((song_timer.tab_index - 1) % 2) == 0:
                all_sounds[-1].append(kickdrum)

        __remove = []
        for i in range(len(all_notes)):
            all_notes[i] = all_notes[i].move(speed)
            if all_keys[i] in note_check:
                if all_notes[i].top > (height-180):
                    for sound in all_sounds[i]:
                        frame_sounds.append(sound)
                    __remove.append(i)
                    score += 1
            if all_notes[i].top > (height - 100):
                __remove.append(i)
                for sound in all_sounds[i]:
                    frame_sounds.append(sound)
        if len(__remove) > 0:
            __remove.reverse()
            for index in __remove:
                all_sprites.pop(index)
                all_notes.pop(index)
                all_sounds.pop(index)
                all_keys.pop(index)

        score_sprite, score_rect = game_text("score: " + str(score), score_font, grey)
        score_rect.center = 864, 486
        screen.fill(background)
        screen.blit(score_sprite, score_rect)
        screen.blit(bg_image, bg_image_rect)
        for j in range(0, len(all_notes)):
            screen.blit(all_sprites[-1 - j][0], all_notes[-1 - j])
        screen.blit(downboard, downboard_rect)
        pygame.display.flip()
        song_timer()
        pygame.time.Clock().tick_busy_loop(60)
        for sound in frame_sounds:
            sound.play()

game_start()