
import random

while True:
    adad = random.randint(1, 100)
    talash = 0
    shans = 5
    bord = False

    print("بازی حدس اعداد")
    print("یک عدد بین 1 تا 100 حدس بزن.")

    while talash < shans:

        print("تلاش", talash + 1, "از", shans)
        print("جان باقی مانده:", shans - talash)

        try:
            hads = int(input("عدد مورد نظر: "))

        except ValueError:
            print("لطفاً عدد وارد کن.")
            continue

        if hads < 1 or hads > 100:
            print("عدد باید بین 1 تا 100 باشد.")
            continue

        talash += 1

        if hads == adad:
            bord = True
            print("آفرین! درست حدس زدی.")

            if talash == 1:
                print("رتبه: نمونه ای")
            elif talash == 2:
                print("رتبه: بسیار خوبی")
            elif talash == 3:
                print("رتبه: خوب")
            elif talash == 4:
                print("رتبه: قبول")
            else:
                print("رتبه: با شانس بردی!")

            break

        else:
            if hads > adad:
                print("کوچک تر وارد کن!")
            else:
                print("بزرگ تر وارد کن!")

            fasele = abs(hads - adad)

            if fasele <= 5:
                print("خیلی نزدیکی!")
            elif fasele <= 15:
                print("نزدیکی، ولی هنوز فاصله داری!")
            else:
                print("خیلی دوری!")

    if bord == False:
        print("باختی!")
        print("عدد درست:", adad)

    javab = input("دوباره بازی می کنی؟ (بله/خیر): ")

    if javab == "خیر":
        print("خداحافظ!")
        break
