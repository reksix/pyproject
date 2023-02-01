def rating_calculator():
    global rating
    global rating_yuzde

    rating = like_num / (like_num + dislike_num)
    rating_yuzde = rating * 100

def rating_shower():
    print("Bu videonun beğenilme oranı : %", rating_yuzde)

    if (rating_yuzde > 50):
        print("Bu video beğenildi!")
    else:
        print("Yarrak gibi video yapmışsın.")

def user_input():
    global like_num
    global dislike_num


    print("Video beğeni değerini giriniz:")
    try:
        like_num = int(input())

    except ValueError:
        print("Bir sayı gircen amk kreş bebesi misin?")
        user_input()


    print("Video beğenilmeme değerini giriniz:")
    try:
        dislike_num = int(input())

    except ValueError:
        print("Bir daha yanlış yaparsan allahını sikerim")
        user_input()

user_input()
