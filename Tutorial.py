import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Load data
df = pd.read_csv("students.csv")

# Convert DataFrame to dictionary using 'records' orientation
records = df.to_dict(orient='records')

# Define font
font = ImageFont.truetype("NotoSerifGujarati-VariableFont_wght.ttf", size=25)

def generate_card(data):
    # Load template image
    template = Image.open("template.png")
    
    # Load and resize the student's photo
    pic = Image.open(f"photos/{data['id']}.jpg").resize((288, 350), Image.LANCZOS)
    template.paste(pic, (682, 214, 970, 564))
    
    # Create a drawing context
    draw = ImageDraw.Draw(template)
    
    # Draw text fields, converting all to strings
    draw.text((197, 219), str(data['name']), font=font, fill='black')
    draw.text((197, 285), str(data['std']), font=font, fill='black')
    draw.text((197, 350), str(data['mobile']), font=font, fill='black')
    draw.text((197, 420), str(data['udias']), font=font, fill='black')
    draw.text((197, 485), str(data['dob']), font=font, fill='black')
    draw.text((197, 550), str(data['address']), font=font, fill='black')
    draw.text((821, 575), str(data['G.R.No']), font=font, fill='black')
    
    return template

# Generate cards for each record
for record in records:
    card = generate_card(record)
    card.save(f"cards/{record['id']}.jpg")

