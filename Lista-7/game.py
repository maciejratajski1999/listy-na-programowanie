import sys, pygame
from note import Note
from song import Song
from timer import Timer

pygame.init()
pygame.mixer.init()

size = width, height = 960, 540
speed = [0, 5]
background = 120, 22, 10
blue = 10, 50, 130
grey = 100, 100, 100
black = 0, 10, 10
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Metal Thrashing")

drumstick = pygame.mixer.Sound("resources\\drumstick.wav")
# metal_E = pygame.mixer.Sound("resources\\metal_E.wav")

def game_text(content, font):
    ingame_text = font.render(content, True, black)
    return ingame_text, ingame_text.get_rect()

def game_start():
    intro = 1
    while intro == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                collision(mouse_pos)
        screen.fill(background)
        metal_text = pygame.font.Font('freesansbold.ttf', 71)
        metal_sprite, metal_rect = game_text("Metal", metal_text)
        metal_rect.center = 300, 270
        metal_button = pygame.draw.circle(screen, grey, metal_rect.center, 100)

        blues_text = pygame.font.Font('freesansbold.ttf', 71)
        blues_sprite, blues_rect = game_text("Blues", blues_text)
        blues_rect.center = 660, 270
        blues_button = pygame.draw.circle(screen, blue, blues_rect.center, 100)

        def collision(pos):
            if metal_button.collidepoint(pos):
                game_song("metal")
            if blues_button.collidepoint(pos):
                game_song("blues")


        screen.blit(metal_sprite, metal_rect)
        screen.blit(blues_sprite, blues_rect)
        pygame.display.flip()


def game_song(key):

    def get_song(key):
        song = Song(key)
        return Timer(song.bpm), song.tab, song.length, song.background_sounds, song.user_sounds
    song_timer, overtab, length, bg_sounds, user_sounds = get_song(key)

    def new_tab(index):
        try:
            tab = overtab[index]
            notes = [Note(letter, bg_sounds) for letter in tab]
            sprites = [(pygame.image.load(note.image), note.pos) for note in notes]
            ingame_positions = [pos for image, pos in sprites]
            ingame_notes = [image.get_rect() for image, pos in sprites]
            ingame_sounds = [[pygame.mixer.Sound(note.sound)] for note in notes]
            for i in range(0, len(ingame_notes)):
                ingame_notes[i].x = ingame_positions[i]
                ingame_notes[i].y = -100
            return sprites, ingame_notes, ingame_sounds
        except IndexError:
            return [], [], []


    all_sprites, all_notes, all_sounds = [], [], []
    while 1:
        frame_sounds = []
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT : sys.exit()
            elif keys[pygame.K_q]:frame_sounds.append(pygame.mixer.Sound(user_sounds["Q"]))
            elif keys[pygame.K_w]:frame_sounds.append(pygame.mixer.Sound(user_sounds["W"]))
            elif keys[pygame.K_e]:frame_sounds.append(pygame.mixer.Sound(user_sounds["E"]))
            elif keys[pygame.K_r]:frame_sounds.append(pygame.mixer.Sound(user_sounds["R"]))
        if song_timer.tab_index > length and len(all_notes) == 0:
            # TODO
            raise IOError("koniec piosenki niezaimplementowany")

        if song_timer.check():
            song_timer.tab_index_up()
            sprites, ingame_notes, ingame_sounds = new_tab(song_timer.tab_index)
            for new_sprite in sprites:
                all_sprites.append(new_sprite)
            for new_note in ingame_notes:
                all_notes.append(new_note)
            for new_sound in ingame_sounds:
                all_sounds.append(new_sound)

            if (song_timer.tab_index % 2) == 0:
                all_sounds[-1].append(drumstick)

        __remove = []
        for i in range(len(all_notes)):
            all_notes[i] = all_notes[i].move(speed)
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

        screen.fill(background)
        for j in range(0, len(all_notes)):
            screen.blit(all_sprites[0 - j][0], all_notes[0 - j])
        pygame.display.flip()
        song_timer()
        pygame.time.Clock().tick_busy_loop(30)
        for sound in frame_sounds:
            sound.play()

game_start()