from PIL import Image
from PIL import PngImagePlugin

def create_image(team_number, csv, brand, uni_logos_path, team_pics_path, out_path):
    try:
        Image.MAX_IMAGE_PIXELS = None
        PngImagePlugin.MAX_TEXT_CHUNK = 1000000000000
        uni_path = "{}/{}".format(uni_logos_path, csv[team_number][csv[0].index("uni")])
        print(uni_path)
        uni_logo = Image.open(uni_path)
    except:
       print("\033[0;31m UNI LOGO ERROR FOR TEAM NUMEBR: {} RETURNING \033[0m".format(team_number))
    try:
        team_path = "{}/{}".format(team_pics_path, team_number)
        print(team_path)
        team_pic = Image.open(team_path)
        team_pic = team_pic.convert("RGBA")
    except:
        print("\033[0;31m TEAM PIC ERROR FOR TEAM NUMEBR: {} RETURNING \033[0m".format(team_number))
        return
    team_pic.paste(uni_logo, (0, 0, 10, 10), uni_logo.convert("RGBA"))
    team_pic.save("{}/{}".format(out_path, team_number), "PNG")


def csv_loader(path_to_csv):
    csv = {}
    read = open(path_to_csv, "r")
    arr = [line.rstrip() for line in read]
    for i in range(len(arr)):
        csv[i] = [x.strip('"') for x in arr[i].split(',')]
    return csv


csv = csv_loader("teams.csv")
brand = Image.open("brand.jpg")
for i in range(1, 100):
    create_image(i, csv, brand, "new_logos", "teams", "out")


