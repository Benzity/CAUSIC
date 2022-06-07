import pygame
import time
    
chords = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B',
          'Cm','Dbm','Dm','Ebm','Em','Fm','Gbm','Gm','Abm','Am','Bbm','Bm',
          'CM7', 'DbM7','DM7','EbM7','EM7','FM7','GbM7','GM7','AbM7','AM7','BbM7','BM7'
          'C7','Db7','D7','Eb7','E7','F7','Gb7','G7','Ab7','A7','Bb7','B7',
          'Cm7','Dbm7','Dm7','Ebm7','Em7','Fm7','Gbm7','Gm7','Abm7','Am7','Bbm7','Bm7',
          'Csus4','Dbsus4','Dsus4','Ebsus4','Fsus4','Gbsus4','Gsus4','Absus4','Asus4','Bbsus4','Bsus4',
          'C/E','G/B','D/F#','Cdim','Caug','C6','F#m7b5']

# v1.0.0 초기 버전. 기본 코드 기준 메이저, 마이너, Dominant7, M7, sus4 추가
# 실험 ver C키의 4번 Option, C6, Cdim, Caug등의 생소 코드 추가
    
pygame.mixer.init()

'''Major Chord'''
C = pygame.mixer.Sound('C.wav')
Db = pygame.mixer.Sound('Db.wav')
D = pygame.mixer.Sound('D.wav')
Eb = pygame.mixer.Sound('Eb.wav')
E = pygame.mixer.Sound('E.wav')
F = pygame.mixer.Sound('F.wav')
Gb = pygame.mixer.Sound('Gb.wav')
G = pygame.mixer.Sound('G.wav')
Ab = pygame.mixer.Sound('Ab.wav')
A = pygame.mixer.Sound('A.wav')
Bb = pygame.mixer.Sound('Bb.wav')
B = pygame.mixer.Sound('B.wav')

'''Minor Chord'''

Cm = pygame.mixer.Sound('Cm.wav')
Dbm = pygame.mixer.Sound('Dbm.wav')
Dm = pygame.mixer.Sound('Dm.wav')
Ebm = pygame.mixer.Sound('Ebm.wav')
Em = pygame.mixer.Sound('Em.wav')
Fm = pygame.mixer.Sound('Fm.wav')
Gbm = pygame.mixer.Sound('Gbm.wav')
Gm = pygame.mixer.Sound('Gm.wav')
Abm = pygame.mixer.Sound('Abm.wav')
Am = pygame.mixer.Sound('Am.wav')
Bbm = pygame.mixer.Sound('Bbm.wav')
Bm = pygame.mixer.Sound('Bm.wav')

'''Dominant7 Chord'''

C7 = pygame.mixer.Sound('C7.wav')
Db7 = pygame.mixer.Sound('Db7.wav')
D7 = pygame.mixer.Sound('D7.wav')
Eb7 = pygame.mixer.Sound('Eb7.wav')
E7 = pygame.mixer.Sound('E7.wav')
F7 = pygame.mixer.Sound('F7.wav')
Gb7 = pygame.mixer.Sound('Gb7.wav')
G7 = pygame.mixer.Sound('G7.wav')
Ab7 = pygame.mixer.Sound('Ab7.wav')
A7 = pygame.mixer.Sound('A7.wav')
Bb7 = pygame.mixer.Sound('Bb7.wav')
B7 = pygame.mixer.Sound('B7.wav')

'''Major7 Chord'''

CM7 = pygame.mixer.Sound('CM7.wav')
DbM7 = pygame.mixer.Sound('DbM7.wav')
DM7 = pygame.mixer.Sound('DM7.wav')
EbM7 = pygame.mixer.Sound('EbM7.wav')
EM7 = pygame.mixer.Sound('EM7.wav')
FM7 = pygame.mixer.Sound('FM7.wav')
GbM7 = pygame.mixer.Sound('GbM7.wav')
GM7 = pygame.mixer.Sound('GM7.wav')
AbM7 = pygame.mixer.Sound('AbM7.wav')
AM7 = pygame.mixer.Sound('AM7.wav')
BbM7 = pygame.mixer.Sound('BbM7.wav')
BM7 = pygame.mixer.Sound('BM7.wav')

'''Minor7 Chord'''

Cm7 = pygame.mixer.Sound('Cminor7.wav')
Dbm7 = pygame.mixer.Sound('Dbminor7.wav')
Dm7 = pygame.mixer.Sound('Dminor7.wav')
Ebm7 = pygame.mixer.Sound('Ebminor7.wav')
Em7 = pygame.mixer.Sound('Eminor7.wav')
Fm7 = pygame.mixer.Sound('Fminor7.wav')
Gbm7 = pygame.mixer.Sound('Gbminor7.wav')
Gm7 = pygame.mixer.Sound('Gminor7.wav')
Abm7 = pygame.mixer.Sound('Abminor7.wav')
Am7 = pygame.mixer.Sound('Aminor7.wav')
Bbm7 = pygame.mixer.Sound('Bbminor7.wav')
Bm7 = pygame.mixer.Sound('Bminor7.wav')

'''Sus4 Chord'''

Csus4 = pygame.mixer.Sound('Csus4.wav')
Dbsus4 = pygame.mixer.Sound('Dbsus4.wav')
Dsus4 = pygame.mixer.Sound('Dsus4.wav')
Ebsus4 = pygame.mixer.Sound('Ebsus4.wav')
Esus4 = pygame.mixer.Sound('Esus4.wav')
Fsus4 = pygame.mixer.Sound('Fsus4.wav')
Gbsus4 = pygame.mixer.Sound('Gbsus4.wav')
Gsus4 = pygame.mixer.Sound('Gsus4.wav')
Absus4 = pygame.mixer.Sound('Absus4.wav')
Asus4 = pygame.mixer.Sound('Asus4.wav')
Bbsus4 = pygame.mixer.Sound('Bbsus4.wav')
Bsus4 = pygame.mixer.Sound('Bsus4.wav')

'''Special Chord'''
C_E = pygame.mixer.Sound('C_E.wav')
G_B = pygame.mixer.Sound('G_B.wav')
D_Gb = pygame.mixer.Sound('D_F#.wav')
Em_G = pygame.mixer.Sound('Em_G.wav')
Gbm7b5 = pygame.mixer.Sound('F#m7b5.wav')
Cdim = pygame.mixer.Sound('Cdim.wav')
Caug = pygame.mixer.Sound('Caug.wav')
C6 = pygame.mixer.Sound('C6.wav')
canon = pygame.mixer.Sound('canon.wav')
canon_rehar = pygame.mixer.Sound('canon_rehar.wav')


def next(): # 코드 입력 후 3.9초간의 텀을 두고 다음 코드를 안겹치게 재생하게 해주는 함수
    time.sleep(3.9)
    
def chordsplay(chord): # 변수에 저장된 wave 파일을 pygame을 이용해 재생하는 함수
    
    if chord == 'C': C.play()
    elif chord == 'Db': Db.play()
    elif chord == 'D': D.play()
    elif chord == 'Eb': Eb.play()
    elif chord == 'E': E.play()
    elif chord == 'F': F.play()
    elif chord == 'Gb': Gb.play()
    elif chord == 'G': G.play()
    elif chord == 'Ab': Ab.play()
    elif chord == 'A': A.play()
    elif chord == 'Bb': Bb.play()
    elif chord == 'B': B.play()
    
    elif chord == 'Cm': Cm.play()
    elif chord == 'Dbm': Dbm.play()
    elif chord == 'Dm': Dm.play()
    elif chord == 'Ebm': Ebm.play()
    elif chord == 'Em': Em.play()
    elif chord == 'Fm': Fm.play()
    elif chord == 'Gbm': Gbm.play()
    elif chord == 'Gm': Gm.play()
    elif chord == 'Abm': Abm.play()
    elif chord == 'Am': Am.play()
    elif chord == 'Bbm': Bbm.play()
    elif chord == 'Bm': Bm.play()

    elif chord == 'Cm7': Cm7.play()
    elif chord == 'Dbm7': Dbm7.play()
    elif chord == 'Dm7': Dm7.play()
    elif chord == 'Ebm7': Ebm7.play()
    elif chord == 'Em7': Em7.play()
    elif chord == 'Fm7': Fm7.play()
    elif chord == 'Gbm7': Gbm7.play()
    elif chord == 'Gm7': Gm7.play()
    elif chord == 'Abm7': Abm7.play()
    elif chord == 'Am7': Am7.play()
    elif chord == 'Bbm7': Bbm7.play()
    elif chord == 'Bm7': Bm7.play()

    elif chord == 'CM7': CM7.play()
    elif chord == 'DbM7': DbM7.play()
    elif chord == 'DM7': DM7.play()
    elif chord == 'EbM7': EbM7.play()
    elif chord == 'EM7': EM7.play()
    elif chord == 'FM7': FM7.play()
    elif chord == 'GbM7': GbM7.play()
    elif chord == 'GM7': GM7.play()
    elif chord == 'AbM7': AbM7.play()
    elif chord == 'AM7': AM7.play()
    elif chord == 'BbM7': BbM7.play()
    elif chord == 'BM7': BM7.play()

    elif chord == 'C7': C7.play()
    elif chord == 'Db7': Db7.play()
    elif chord == 'D7': D7.play()
    elif chord == 'Eb7': Eb7.play()
    elif chord == 'E7': E7.play()
    elif chord == 'F7': F7.play()
    elif chord == 'Gb7': Gb7.play()
    elif chord == 'G7': G7.play()
    elif chord == 'Ab7': Ab7.play()
    elif chord == 'A7': A7.play()
    elif chord == 'Bb7': Bb7.play()
    elif chord == 'B7': B7.play()
    
    elif chord == 'Csus4': Csus4.play()
    elif chord == 'Dbsus4': Dbsus4.play()
    elif chord == 'Dsus4': Dsus4.play()
    elif chord == 'Ebsus4': Ebsus4.play()
    elif chord == 'Esus4': Esus4.play()
    elif chord == 'Fsus4': Fsus4.play()
    elif chord == 'Gbsus4': Gbsus4.play()
    elif chord == 'Gsus4': Gsus4.play()
    elif chord == 'Absus4': Absus4.play()
    elif chord == 'Asus4': Asus4.play()
    elif chord == 'Bbsus4': Bbsus4.play()
    elif chord == 'Bsus4': Bsus4.play()

    elif chord == 'C/E': C_E.play()
    elif chord == 'G/B': G_B.play()
    elif chord == 'D/F#': D_Gb.play
    elif chord == 'Em/G':Em_G.play()
    elif chord == 'F#m7b5':Gbm7b5.play()
    elif chord == 'Cdim': Cdim.play()
    elif chord == 'Caug': Caug.play()
    elif chord == 'C6': C6.play()
    elif chord == 'canon': canon.play()
    elif chord == 'canon_rehar': canon_rehar.play()
    
    
    
    next()
        

'''
CAUSIC Music Compose Program v1.0.0.
Made by Younghyun Choi, CHUNG-ANG UNIV.

Recent Update - 2022.05.31(v1.0.0.)
'''

print("                                                            ")
print("    ■■■■ ■■■■ ■    ■ ■■■■ ■ ■■■■ ®      ")
print("    ■       ■    ■ ■    ■ ■       ■ ■               ")
print("    ■       ■□□■ ■    ■ ■■■■ ■ ■               ")
print("    ■       ■    ■ ■    ■       ■ ■ ■               ")
print("    ■□□□ ■    ■ ■■■■ ■■■■ ■ ■■■■   v1.0.0.")
print("                                                            ")





print("Made By 최영현(Younghyun Choi).")


while True:
    print("1. CAUSIC 소개  2. 코드 들어보기  3. 4개 코드 직접 작곡하기 4. 코드 추천받아 작곡하기 5. 종료 ")
    init_option = int(input("원하시는 기능을 선택하세요 :"))
   

    if init_option == 1:
          
          print("CAUSIC은 어려운 DAW로 작곡에 어려움을 겪는 사람들이 간단한 코드 입력으로 바로 코드 진행을 들을 수 있게 해주는 프로그램입니다. 멋진 작곡 하세요!")
          sec_option = input("바로 작곡을 진행보시겠어요? Y/N : ")
          if sec_option == 'Y':
              init_option = 3
          else:
              continue

    elif init_option == 2:
        

        while True:
            whatchord = input("어떤 코드를 들어보시겠어요?: ")
            if whatchord in chords:
                print("%s 코드가 연주중입니다." %whatchord)
                chordsplay(whatchord)
            else:
                print("아직 추가되지 않았거나 잘못된 코드입니다 !")

            option2_yesorno = input("그만하시겠습니까? Y/N :")
            if option2_yesorno == 'Y':
                break
            elif option2_yesorno == 'N':
                continue
            else:
                print("잘못된 접근입니다.")
                break

    elif init_option == 3:
        while True:
            chords = []
            for i in range (4):
                ch = input("진행시킬 %d번째 코드를 입력하세요: " %(i+1))
                chords.append(ch)
            for j in range (4):
                print("%d번째 코드가 플레이 중입니다 . . ." %(j+1))
                chordsplay(chords[j])

            while True:
                optionrepeat = input("한번 더 연주하시겠습니까? Y/N: ")
                if optionrepeat == 'Y':
                    for j in range (4):
                        print("%d번째 코드가 플레이 중입니다 . . ." %(j+1))
                        chordsplay(chords[j])
                else:
                    break

            option3_yesorno = input("다른 코드를 입력하시겠습니까? Y/N: ")
            if option3_yesorno == 'N':
                break
            elif option3_yesorno == 'Y':
                continue
    elif init_option == 4:
        while True:
            keychords = []
            key = input("원하시는 키를 입력하세요. (옵션을 나가려면 !를 입력하세요): ")
            if key == 'C':
                print("CAUSIC은 %s키의 코드 진행을 다음과 같이 추천합니다. 어떤 진행을 들려드릴까요?" %key)
                print("♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪")
                
                print("1. Popular Music ㅣ C-G-Am-F ㅣ 1-5-6-4")
                print("2. Popular Music ㅣ C-Em-Am-F ㅣ 1-3-6-4")
                print("3. Popular Music ㅣ C-G-Dm-F ㅣ 1-5-2-4")
                print("4. Popular Music ㅣ Am-F-C-G ㅣ 6-4-1-5")
                print("5. Popular Music ㅣ Am-C-G-F ㅣ 6-1-5-4")
                print("6. Popular Music ㅣ F-G-Am-C ㅣ 4-5-6-1")
                print("7. Popular Music ㅣ Dm-F-Am7-G ㅣ 2-4-6-5")
                print("8. Jazz ㅣ CM7-Am7-Dm7-G7 ㅣ 1-6-2-5")
                print("9. Jazz ㅣ Dm7-G7-CM7-Am7 ㅣ 2-5-1-6")
                print("10. Jazz ㅣ FM7-G7-Em7-Am7 ㅣ 4-5-3-6")
                print("11. Jazz ㅣ CM7-Dm7-C/E(Em7)-FM7 ㅣ 1-2-3-4")
                print("12. Canon ㅣ C-G/B-Am7-Em/G-FM7-C/E-Dm7-G7ㅣ***")
                print("13. Canon Reharmonied ㅣ CM7-Bm7(b5)-E7-Am7-Gm7-C7-FM7-Em7-Dm7-G7ㅣ***")
                
                print("♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪")


                while True:
                    keyoption = int(input("몇 번 진행을 시작할지 입력하세요, 다른 키 입력 또는 다른 기능을 이용하고 싶을 시 0을 눌러주세요.: "))
                    if keyoption == 0:
                        print("---------------------------------------------------------------------")
                        break
                    elif keyoption == 1:
                        keychords = ['C','G','Am','F']
                        print("Popular Music(%s-%s-%s-%s)의 진행이 재생 중입니다 . . ." %(keychords[0],keychords[1],keychords[2],keychords[3]))
                        for i in range (len(keychords)):
                            chordsplay(keychords[i])
                    elif keyoption == 2:
                        keychords = ['C','Em','Am','F']
                        print("Popular Music(%s-%s-%s-%s)의 진행이 재생 중입니다 . . ." %(keychords[0],keychords[1],keychords[2],keychords[3]))            
                        for i in range (len(keychords)):
                            chordsplay(keychords[i])
                    elif keyoption == 3:
                        keychords = ['C','G','Dm','F']
                        print("Popular Music(%s-%s-%s-%s)의 진행이 재생 중입니다 . . ." %(keychords[0],keychords[1],keychords[2],keychords[3])) 
                        for i in range (len(keychords)):
                            chordsplay(keychords[i])
                    elif keyoption == 4:
                        keychords = ['Am','F','C','G']
                        print("Popular Music(%s-%s-%s-%s)의 진행이 재생 중입니다 . . ." %(keychords[0],keychords[1],keychords[2],keychords[3]))
                        for i in range (len(keychords)):
                            chordsplay(keychords[i])
                    elif keyoption == 5:
                        keychords = ['Am','C','G','F']
                        print("Popular Music(%s-%s-%s-%s)의 진행이 재생 중입니다 . . ." %(keychords[0],keychords[1],keychords[2],keychords[3]))
                        for i in range (len(keychords)):
                            chordsplay(keychords[i])
                    elif keyoption == 6:
                        keychords = ['F','G','Am','C']
                        print("Popular Music(%s-%s-%s-%s)의 진행이 재생 중입니다 . . ." %(keychords[0],keychords[1],keychords[2],keychords[3]))
                        for i in range (len(keychords)):
                            chordsplay(keychords[i])
                    elif keyoption == 7:
                        keychords = ['Dm','F','Am7','G']
                        print("Popular Music(%s-%s-%s-%s)의 진행이 재생 중입니다 . . ." %(keychords[0],keychords[1],keychords[2],keychords[3]))
                        for i in range (len(keychords)):
                            chordsplay(keychords[i])
                    elif keyoption == 8:
                        keychords = ['CM7','Am7','Dm7','G7']
                        print("Jazz(%s-%s-%s-%s)의 진행이 재생 중입니다 . . ." %(keychords[0],keychords[1],keychords[2],keychords[3]))
                        for i in range (len(keychords)):
                            chordsplay(keychords[i])
                    elif keyoption == 9:
                        keychords = ['Dm7','G7','CM7','Am7']
                        print("Jazz(%s-%s-%s-%s)의 진행이 재생 중입니다 . . ." %(keychords[0],keychords[1],keychords[2],keychords[3]))
                        for i in range (len(keychords)):
                            chordsplay(keychords[i])
                    elif keyoption == 10:
                        keychords = ['FM7','G7','Em7','Am7']
                        print("Jazz(%s-%s-%s-%s)의 진행이 재생 중입니다 . . ." %(keychords[0],keychords[1],keychords[2],keychords[3]))
                        for i in range (len(keychords)):
                            chordsplay(keychords[i])
                    elif keyoption == 11:
                        keychords = ['CM7','Dm7','C/E','FM7']
                        print("Jazz(%s-%s-%s-%s)의 진행이 재생 중입니다 . . ." %(keychords[0],keychords[1],keychords[2],keychords[3]))
                        for i in range (len(keychords)):
                            chordsplay(keychords[i])
                    elif keyoption == 12:
                        keychords = ['C','G/B','Am7','Em/G','FM7','C/E','Dm7','G7']
                        print("C키의 Canon 진행이 재생 중입니다 . . .")
                        chordsplay('canon')
                        time.sleep(15)
                    elif keyoption == 13:
                        keychords = ['CM7','Bm7(b5)','E7','Am7','Gm7','C7','FM7','Em7','Dm7','G7']
                        print("C키의 Canon Reharmonied 진행이 재생 중입니다 . . .")
                        chordsplay('canon_rehar')
                        time.sleep(16)
                    else:
                        print("더 이상의 키 진행 번호가 없거나 잘못된 접근입니다.")
                        continue
            elif key == '!':
                break
            else:
                print("아직 준비중입니다. C키만 가능합니다 ")
                continue
                    
                                

                
                
    elif init_option == 5:
        break

    else:
        print("잘못된 접근입니다.")
        continue
    
            
        
        
        

        
        
    

    
