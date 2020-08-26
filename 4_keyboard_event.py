import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("결혼했냐 묻는사람 죽이는 게임") # 게임 이름

#배경이미지 불러오기
background = pygame.image.load("C:/Users/Wookmawang/Desktop/공부/makegame/pygame_basic/background.png")

# 캐릭터 불러오기 
character = pygame.image.load("C:/Users/Wookmawang/Desktop/공부/makegame/pygame_basic/character.jpg")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] #캐릭터 가로크기
character_height = character_size[1] #캐릭터 세로크기
character_x_pos = screen_width / 2 - character_width / 2 #화면 가로의 ㄱ절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로의 가장아래 해당하는 곳에 위치


# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프 
running = True # 게임이 진행중인가?
while running: # 게임 진행중인 동안에
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가
            running = False # 게임이 진행주잉 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= 5 #to_x = to_x -5 라는 말임
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += 5
            elif event.key == pygame.K_UP: #캐릭터를 위쪽으로
                to_y -= 5
            elif event.key == pygame.K_DOWN: #캐릭터를 아래쪽으로
                to_y += 5

        if event.type == pygame.KEYUP: #방향키 떼면 0으로 움직이지 않게 함 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0  

    character_x_pos += to_x
    character_y_pos += to_y

    #캐릭터 화면 밖으로 못나가게 하는것임
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # 계산 잘해
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height: # 계산 잘해
        character_y_pos = screen_height - character_height


    screen.blit(background, (0, 0)) #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) #배경 그리기

    pygame.display.update() # 게임화면 꼐속 그리게 하는것 이거 무조건 있어야함

# pygame 종료
pygame.quit()