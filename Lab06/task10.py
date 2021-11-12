# 10. Napisz system ekspertowy, który określi
# czy dana osoba choruje na grypę czy przeziębienie
# w zależności od symptomów. Jeśli mamy wszystkie
# trzy symptomy: gorączka, ból mieśni i osłabienie
# to mamy grypę. Jeśli mamy gorączkę i osłabienie
# to przeziębienie, jeśli tylko osłabienie to wszystko
# OK a jeśli ból mieśni to jesteśmy przetrenowani.

def diagnoza(s):
    my_dict = dict(s)
    if (my_dict.get("gorączka")
            and my_dict.get("ból mięśni")
            and my_dict.get("osłabienie")):
        return "grypa"
    elif (my_dict.get("gorączka")
          and my_dict.get("osłabienie")):
        return "przeziębienie"
    elif my_dict.get("ból mięśni"):
        return "przetrenowanie"
    return "wszystko ok"


symptomy = {"gorączka": False,
            "ból mięśni": True,
            "osłabienie": False
            }

print(diagnoza(symptomy))
