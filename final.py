import random
import pygame
##################반드시 해야하는것###########################################
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("결혼했냐 묻는사람(똥) 피하기") # 게임 이름

#FPS
clock = pygame.time.Clock()
#############################################################################

##################사용자 게임 초기화 (배경화면, 게임이미지 , 좌표, 폰트)##############

#배경이미지 불러오기
background = pygame.image.load("C:/Users/Wookmawang/Desktop/공부/makegame/pygame_basic/background.png")

#게임 종료 화면
gameend = pygame.image.load("C:/Users/Wookmawang/Desktop/공부/makegame/pygame_basic/gameend.png")

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

# 이동 속도
character_speed = 0.6

# 떨어지는 창유성 만들기

enemy = pygame.image.load("C:/Users/Wookmawang/Desktop/공부/makegame/pygame_basic/enemy.jpg")
enemy_size = enemy.get_rect().size # 이미지 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터 가로크기
enemy_height = enemy_size[1] #캐릭터 세로크기
enemy_x_pos =  random.randint(0, screen_width - enemy_width) #화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos =  0 #화면 세로의 가장아래 해당하는 곳에 위치
enemy_speed = 4

enemy2 = pygame.image.load("C:/Users/Wookmawang/Desktop/공부/makegame/pygame_basic/enemy.jpg")
enemy_size2 = enemy2.get_rect().size # 이미지 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터 가로크기
enemy_height = enemy_size[1] #캐릭터 세로크기
enemy_x_pos2 =  random.randint(0, screen_width - enemy_width) #화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos2 =  0 #화면 세로의 가장아래 해당하는 곳에 위치
enemy_speed2 = 6

enemy3 = pygame.image.load("C:/Users/Wookmawang/Desktop/공부/makegame/pygame_basic/enemy.jpg")
enemy_size3 = enemy3.get_rect().size # 이미지 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터 가로크기
enemy_height = enemy_size[1] #캐릭터 세로크기
enemy_x_pos3 =  random.randint(0, screen_width - enemy_width) #화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos3 =  0 #화면 세로의 가장아래 해당하는 곳에 위치
enemy_speed3 = 8

enemy4 = pygame.image.load("C:/Users/Wookmawang/Desktop/공부/makegame/pygame_basic/enemy.jpg")
enemy_size4 = enemy4.get_rect().size # 이미지 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터 가로크기
enemy_height = enemy_size[1] #캐릭터 세로크기
enemy_x_pos4 =  random.randint(0, screen_width - enemy_width) #화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos4 =  0 #화면 세로의 가장아래 해당하는 곳에 위치
enemy_speed4 = 9

enemy5 = pygame.image.load("C:/Users/Wookmawang/Desktop/공부/makegame/pygame_basic/enemy.jpg")
enemy_size5 = enemy5.get_rect().size # 이미지 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터 가로크기
enemy_height = enemy_size[1] #캐릭터 세로크기
enemy_x_pos5 =  random.randint(0, screen_width - enemy_width) #화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos5 =  0 #화면 세로의 가장아래 해당하는 곳에 위치
enemy_speed5 = 9

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총시간
total_time = 0
# 시작 시간정보
start_ticks = pygame.time.get_ticks() #현재 시간 tick 을 받아옴


# 이벤트 루프 
running = True # 게임이 진행중인가?
while running: # 게임 진행중인 동안에
 
    dt = clock.tick(60) # 게임 화면 초당 프레임수 설정
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 100
    timer = game_font.render(str(int(total_time + elapsed_time)), True,(255, 255, 255))

#캐릭터가 100만큼 이동해야함
#10 fps : 1초 동안에 10번 동작 -> 1번에 몇만큼 이동? 10만큼! 10 * 10 = 100
 
    print("fps :" + str(clock.get_fps()))
 
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가
            running = False # 게임이 진행주잉 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed #to_x = to_x -5 라는 말임
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += character_speed
         

        if event.type == pygame.KEYUP: #방향키 떼면 0으로 움직이지 않게 함 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0  

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    enemy_y_pos += enemy_speed

    
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
    
    if elapsed_time > 30:
        enemy_y_pos2 += enemy_speed2

        if enemy_y_pos2 > screen_height:
            enemy_y_pos2 = 0
            enemy_x_pos2 = random.randint(0, screen_width - enemy_width)

    if elapsed_time > 70:
        enemy_y_pos3 += enemy_speed3

        if enemy_y_pos3 > screen_height:
            enemy_y_pos3 = 0
            enemy_x_pos3 = random.randint(0, screen_width - enemy_width)

    if elapsed_time > 150:
        enemy_y_pos4 += enemy_speed4

        if enemy_y_pos4 > screen_height:
            enemy_y_pos4 = 0
            enemy_x_pos4 = random.randint(0, screen_width - enemy_width)

    if elapsed_time > 200:
        enemy_y_pos5 += enemy_speed5

        if enemy_y_pos5 > screen_height:
            enemy_y_pos5 = 0
            enemy_x_pos5 = random.randint(0, screen_width - enemy_width)

    #캐릭터 화면 밖으로 못나가게 하는것임
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # 계산 잘해
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height: # 계산 잘해
        character_y_pos = screen_height - character_height


    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy_rect2 = enemy2.get_rect()
    enemy_rect2.left = enemy_x_pos2
    enemy_rect2.top = enemy_y_pos2
    
    enemy_rect3 = enemy3.get_rect()
    enemy_rect3.left = enemy_x_pos3
    enemy_rect3.top = enemy_y_pos3

    enemy_rect4 = enemy4.get_rect()
    enemy_rect4.left = enemy_x_pos4
    enemy_rect4.top = enemy_y_pos4

    enemy_rect5 = enemy4.get_rect()
    enemy_rect5.left = enemy_x_pos5
    enemy_rect5.top = enemy_y_pos5

    screen.blit(background, (0, 0))
    # 충돌 체크
    
    if character_rect.colliderect(enemy_rect) or character_rect.colliderect(enemy_rect2) or character_rect.colliderect(enemy_rect3) or character_rect.colliderect(enemy_rect4):
        
        screen.blit(gameend, (0, 0)) # 충돌시배경화면 기존 배경화면 아래에 써야 이게 반응하네
        print("충돌 했어요")
        running = False #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    
    # 타이머 집어 넣기
    # 경과시간 계산
    
    #경과시간을 1000으로 나눠서 초단위로 표시 밀리세컨드를 초로 바꿈
    # 처음에 렌더 뒤에 들어가는가는 출력할 시간정보 , True, 글자 색상
    
    


    screen.blit(timer, (10, 10))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    if elapsed_time > 20:
        screen.blit(enemy2, (enemy_x_pos2, enemy_y_pos2))
    if elapsed_time > 60:
        screen.blit(enemy3, (enemy_x_pos3, enemy_y_pos3))
    if elapsed_time > 140:
        screen.blit(enemy4, (enemy_x_pos4, enemy_y_pos4))
    if elapsed_time > 190:
        screen.blit(enemy5, (enemy_x_pos5, enemy_y_pos5))
        
            

    # 만약 시간이 0이하이면 게임종료
    #if total_time - elapsed_time <= 0:
    #    print("타임아웃")
    #    running = False
    


    pygame.display.update() # 게임화면 꼐속 그리게 하는것 이거 무조건 있어야함

# 잠시 대기 
pygame.time.delay(5000) #5초정도 대기 (ms)

# pygame 종료
pygame.quit()