from PIL import Image, ImageDraw, ImageFont
import textwrap

def add_text_to_image(image_path, text, output_path="output.png"):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    try:
        font_path = "arial.ttf"
        font = ImageFont.truetype(font_path, 80)
    except IOError:
        font = ImageFont.load_default()

    max_width = img.width * 0.8
    max_height = img.height * 0.6

    text_lines = textwrap.wrap(text, width=20)

    font_size = 80
    while True:
        font = ImageFont.truetype(font_path, font_size)
        
        total_text_width = 0
        total_text_height = 0
        for line in text_lines:
            line_bbox = draw.textbbox((0, 0), line, font=font)
            line_width = line_bbox[2] - line_bbox[0]
            line_height = line_bbox[3] - line_bbox[1]
            total_text_width = max(total_text_width, line_width)
            total_text_height += line_height + 10

        if total_text_width <= max_width and total_text_height <= max_height:
            break
        font_size -= 5

        if font_size < 10:
            break

    total_text_width = 0
    total_text_height = 0
    for line in text_lines:
        line_bbox = draw.textbbox((0, 0), line, font=font)
        line_width = line_bbox[2] - line_bbox[0]
        line_height = line_bbox[3] - line_bbox[1]
        total_text_width = max(total_text_width, line_width)
        total_text_height += line_height + 10

    padding = 20
    box_x1 = (img.width - total_text_width) // 2 - padding
    box_y1 = (img.height - total_text_height) // 2 - padding
    box_x2 = (img.width + total_text_width) // 2 + padding
    box_y2 = (img.height + total_text_height) // 2 + padding

    if box_y2 > img.height:
        new_img = Image.new("RGB", (img.width, box_y2), "white")
        new_img.paste(img, (0, 0))
        img = new_img
        draw = ImageDraw.Draw(img)

    draw.rectangle([box_x1, box_y1, box_x2, box_y2], fill="white")

    y = box_y1 + padding
    for line in text_lines:
        line_bbox = draw.textbbox((0, 0), line, font=font)
        line_width = line_bbox[2] - line_bbox[0]
        x = (img.width - line_width) // 2
        draw.text((x, y), line, fill="black", font=font)
        y += line_bbox[3] - line_bbox[1] + 10

    img.save(output_path)
    img.show()

image_path = "image.png"
user_text = "This is a long text that should be split into kjhkhkjjjjjjjjjjjjjjjjjjmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm  mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm kmmmmmmmmmmmmmmmmm mmmmmmmmm mmmmmmm mmmmmmmmmmm mmmmmmmmmmm  mmmmm mmm m m m m mmultiple lines for better readability!"
add_text_to_image(image_path, user_text)