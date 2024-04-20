from PIL import Image,ImageDraw

def draw_boxes(path_to_png:str,boxes,msg:str):
    page = Image.open(path_to_png)
    draw = ImageDraw.Draw(page)
    for box in boxes:
        draw.rectangle(box,outline="red")
        top_left = (box[0], box[3])
        draw.text(top_left, msg, fill="red", align="left")
    page.save(f"{path_to_png.split('.')[0]}_with_errors.png")