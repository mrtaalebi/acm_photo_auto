from PIL import Image
from PIL import PngImagePlugin


def create_image(team_number, card, team_pics_path, out_path, padding_left, padding_top, width):
    try:
        team_path = "{}/{}".format(team_pics_path, team_number)
        print(team_path)
        team_pic = Image.open(team_path)
        team_pic = team_pic.convert("RGBA")
    except:
        print("\033[0;31m TEAM PIC ERROR FOR TEAM NUMEBR: {} RETURNING \033[0m".format(team_number))
        return
    w1, h1 = team_pic.size
    team_pic.thumbnail((width, int(width * h1 / w1)), Image.ANTIALIAS)
    print(card.size)
    print(team_pic.size)
    team_pic.paste(card, (int(team_pic.size[0] * padding_left), int(team_pic.size[1] * padding_top), card.convert("RGBA"))
    team_pic.save("{}/{}".format(out_path, team_number), "PNG")


def init_card(width, height, brand):
    card = Image.new('RGBA', (width, height))
    brand.thumbnail((width, int(brand.size[1] * width / brand.size[0])), Image.ANTIALIAS)
    card.paste(brand, (0, 0), brand.convert("RGBA"))
    return card, brand.size[1]


def png_safe():
    Image.MAX_IMAGE_PIKELS = None
    PngImagePlugin.MAX_TEXT_CHUNK = 1000000000000


def uni_logo_to_card(team_number, csv, card, team_info_top, uni_logos_path, uni_logo_percentage, padding=0.1):
    try:
        uni_logo = Image.open("{}/{}".format(uni_logos_path, csv[team_number][csv[0].index("uni")]))
    except:
        print("\033[0;31m UNI LOGO ERROR FOR TEAM NUMEBR: {} RETURNING \033[0m".format(team_number))
        return
    uni_logo.thumbnail((int(card.size[0] * uni_logo_percentage * (1 - padding)),
        int(card.size[0] * uni_logo_percentage * (1 - padding) * uni_logo.size[1] / uni_logo.size[0])), Image.ANTIALIAS)
    card.paste(uni_logo, (int((card.size[0] - uni_logo.size[0]) / 2), int((card.size[1] + team_info_top - uni_logo.size[1]) / 2)), uni_logo.convert("RGBA"))
    card.save("temp", "PNG")
    return card


def csv_loader(path_to_csv):
    csv = {}
    read = open(path_to_csv, "r")
    arr = [line.rstrip() for line in read]
    for i in range(len(arr)):
        csv[i] = [x.strip('"') for x in arr[i].split(',')]
    return csv




png_safe()
csv = csv_loader("teams.csv")
brand = Image.open("brand")
width = 1366
height = int(3 / 5 * width)

for i in range(1, 100):
    card, top = init_card(int(width * 0.25), int(height * 0.9), brand)
    card = uni_logo_to_card(i, csv, card, top, "new_logos", 0.25)
    create_image(i, card, "teams", "out", 0.03, 0.01, width)


