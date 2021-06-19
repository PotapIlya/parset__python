import time
import cv2
import mss
import mss.tools
import numpy as np
import pyautogui
import difflib
# import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\Пользователь\AppData\Local\Programs\Tesseract-OCR\\tesseract.exe'

# def screen():
#     with mss.mss() as sct:
#         # config
#         mon = {"top": 250, "left": 480, "width": 940, "height": 740}
#         output = "sct-{top}x{left}_{width}x{height}.png".format(**mon)

#         img = sct.grab(mon)
#         mss.tools.to_png(img.rgb, img.size, output='./images/11'+output)
#         # print(img)
#         # imgBin = np.asarray(img)

#         # print(imgBin)
#         image = './images/11sct-250x480_940x740.png'
#         image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
#         gray = cv2.threshold(image, 0, 225, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#         cv2.imwrite('./images/11.jpg', gray)
#         # print(gray)
#         imgBin = np.asarray(gray)

#         rgb = cv2.cvtColor(imgBin, cv2.THRESH_BINARY)
#         print(rgb)
#         pcm6 = pytesseract.image_to_string(rgb, lang='eng')
#         print(pcm6)

# screen()

# monero = '1110011110000001100000010110011001111110110000111000000111000011'
# riple = '0000000000111100011100100101001110000011011100100011100000011000'

# #Функция вычисления хэша
# def CalcImageHash(FileName):
#     image = cv2.imread(FileName) #Прочитаем картинку
#     resized = cv2.resize(image, (8,8), interpolation = cv2.INTER_AREA) #Уменьшим картинку
#     gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) #Переведем в черно-белый формат
#     avg=gray_image.mean() #Среднее значение пикселя
#     ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0) #Бинаризация по порогу

#     #Рассчитаем хэш
#     _hash=""
#     for x in range(8):
#         for y in range(8):
#             val=threshold_image[x,y]
#             if val==255:
#                 _hash=_hash+"1"
#             else:
#                 _hash=_hash+"0"

#     return _hash

# def CompareHash(hash1,hash2):
#     l=len(hash1)
#     i=0
#     count=0
#     while i<l:
#         if hash1[i]!=hash2[i]:
#             count=count+1
#         i=i+1
#     return count
#     #if 0 одинаковые

imgs = [
    {'i':'./images/coins/bit.png', 'n':'btc'},{'i':'./images/coins/bnb.png','n':'bnb'},{'i':'./images/coins/ether.png','n':'eth'},
    {'i':'./images/coins/lite.png','n':'ltc'},
    {'i':'./images/coins/monero.png','n':'mnr'},{'i':'./images/coins/riple.png','n':'rpl'},{'i':'./images/coins/rocket.png','n':'rkt'},
    {'i':'./images/coins/roll.png','n':'rll'},
    {'i':'./images/coins/teter.png','n':'ttr'},{'i':'./images/coins/usdt.png','n':'usdt'},
]

sett = [
    {
        'id':11,
        'name':'',
        'x': 650,'y':300
    },{
        'id':12,
        'name':'',
        'x': 800,'y':300
    },{
        'id':13,
        'name':'',
        'x': 950,'y':300
    },{
        'id':14,
        'name':'',
        'x': 1100,'y':300
    },{
        'id':15,
        'name':'',
        'x': 1250,'y':300
    },{
        'id':21,
        'name':'',
        'x': 650,'y':450
    },{
        'id':22,
        'name':'',
        'x': 800,'y':450
    },{
        'id':23,
        'name':'',
        'x': 950,'y':450
    },{
        'id':24,
        'name':'',
        'x': 1100,'y':450
    },{
        'id':25,
        'name':'',
        'x': 1250,'y':450
    },{
        'id':31,
        'name':'',
        'x': 650,'y':600
    },{
        'id':32,
        'name':'',
        'x': 800,'y':600
    },{
        'id':33,
        'name':'',
        'x': 950,'y':600
    },{
        'id':34,
        'name':'',
        'x': 1100,'y':600
    },{
        'id':35,
        'name':'',
        'x': 1250,'y':600
    },{
        'id':41,
        'name':'',
        'x': 650,'y':750
    },{
        'id':42,
        'name':'',
        'x': 800,'y':750
    },{
        'id':43,
        'name':'',
        'x': 950,'y':750
    },{
        'id':44,
        'name':'',
        'x': 1100,'y':750
    },{
        'id':45,
        'name':'',
        'x': 1250,'y':750
    },

]
toClick = []
# hash1=CalcImageHash("./images/coins/bit.png")
# hash2=CalcImageHash("./images/coins/bnb.png")
# print(hash1)
# print(hash2)
# print(CompareHash(hash1, hash2))

def start():
    end = True
    # games = pyautogui.locateCenterOnScreen('./images/games.png')
    # print(games)
    # pyautogui.moveTo(games)

    # pyautogui.click()

    # coin = pyautogui.locateCenterOnScreen('./images/coin.png')
    # pyautogui.moveTo(coin[0], coin[1]+65)
    # pyautogui.click()
    # time.sleep(3)

    # start = pyautogui.locateCenterOnScreen('./images/start.png')#If the file is not a png file it will not work
    # print(start)
    # pyautogui.moveTo(start)#Moves the mouse to the coordinates of the image

    # pyautogui.click()
    # time.sleep(4)

    i = 0
    prepend = ''
    sleep = False
    dbl = True

    while (end):

        print(sett[i]['id'])
        pyautogui.moveTo(sett[i]['x'], sett[i]['y'])
        pyautogui.click()

        pyautogui.moveTo(sett[i]['x'], sett[i]['y']+200)
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'tab')

        checkInArr = True
        k = 0
        j = 0

        while checkInArr:
            coin = pyautogui.locateCenterOnScreen(imgs[j]['i'], confidence=0.6)
            if coin:
                print(imgs[j]['n'])
                if len(toClick):
                    for click in toClick:
                        if click['name'] == imgs[j]['n']:
                            if sleep:
                                pyautogui.hotkey('alt', 'tab')
                                time.sleep(1)
                                pyautogui.moveTo(sett[i]['x'], sett[i]['y'])
                                pyautogui.click()
                                pyautogui.moveTo(click['x'], click['y'])
                                pyautogui.click()
                                time.sleep(1)
                                toClick.pop(k)
                                dbl = False
                                checkInArr = False
                            else:
                                print(click['name'])
                                pyautogui.moveTo(click['x'], click['y'])
                                pyautogui.click()
                                time.sleep(1)
                                # toClick.pop(k)
                                checkInArr = False

                sett[i]['name'] = imgs[j]['n']

                toClick.append(sett[i])
                k+=1

                if (not sleep):
                    prepend = imgs[j]
                    imgs.pop(j)

                checkInArr = False
            j+=1
            if(j>=len(imgs)):
                checkInArr = False

        if (sleep & dbl):
            pyautogui.hotkey('alt','tab')
            time.sleep(1)
            imgs.append(prepend)
        else:
            dbl = True

        sleep = not sleep
        i+=1

    end = False



start()


# def test():
    #1 str
    # pyautogui.moveTo(650, 300)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(800, 300)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(950, 300)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(1100, 300)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(1250, 300)
    # pyautogui.click()


    #2 str
    # pyautogui.moveTo(650, 450)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(800, 450)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(950, 450)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(1100, 450)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(1250, 450)
    # pyautogui.click()

    #3 str
    # pyautogui.moveTo(650, 600)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(800, 600)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(950, 600)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(1100, 600)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(1250, 600)
    # pyautogui.click()

    #4 str
    # pyautogui.moveTo(650, 750)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(800, 750)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(950, 750)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(1100, 750)
    # pyautogui.click()
    # time.sleep(1)
    # pyautogui.moveTo(1250, 750)
    # pyautogui.click()


# test()











# def coinclick():












# import pyautogui as pag  # mouse
# # from mss import mss  # скриншот
# import mss
# import mss.tools

# from PIL import Image
# import pytesseract
# import cv2
# import os




# image = './images/sct-250x480_940x740.png'
# # preprocess = "thresh"
# image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
# image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# cv2.imwrite('1.jpg', image)


# # img = np.asarray(image)
# # rgb = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# # rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR
# # filename = "7.png".format(os.getpid())
# image = cv2.imread('1.jpg')

# print(Image.open(image))
# # print(
# #     pytesseract.image_to_string(Image.open(image))
# # )C
# exit()

# # затем удаление временного файла
# text = pytesseract.image_to_string(Image.open(filename))
# os.remove(filename)
# print(text)

# # показать выходные изображения
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)
# input('pause...')





# def screen():
#     with mss.mss() as sct:
#         # config
#         monitor = {"top": 250, "left": 480, "width": 940, "height": 740}
#         output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

#         sct_img = sct.grab(monitor)

#         mss.tools.to_png(sct_img.rgb, sct_img.size, output='./images/'+output)
#         print(output)

# # screen()




# # width = pag.size()[0]
# # height = pag.size()[1]

# # width = 1803
# # height = 61
# #
# # pag.moveTo(width, height)
# # pag.click()
