import discord
from discord.ext import commands
from JumpPediaWrapper import JumpPediaAPI
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import io
from tabulate import tabulate

# Create an instance of the JumpPediaAPI
api = JumpPediaAPI(base_url='http://localhost:5000')

# Define the intents
intents = discord.Intents.default()

# Specify the intents your bot requires
intents.typing = False
intents.presences = False

# Create an instance of the bot with the specified intents
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def jumps(ctx):
    # Retrieve all jump levels
    jump_levels = api.retrieve_all_jump_levels()

    if len(jump_levels) > 0:
        # Create a DataFrame from the jump levels data
        df = pd.DataFrame(jump_levels)
        table = tabulate(df, headers='keys', tablefmt='html')

        # Convert the HTML table to an image
        table_image = await create_table_image(table)

        # Send the image in a Discord message
        file = discord.File(table_image, filename='table.png')
        embed = discord.Embed(title='Trickjumps', description='Jump Levels', color=discord.Color.blue())
        embed.set_image(url='attachment://table.png')
        await ctx.send(file=file, embed=embed)
    else:
        await ctx.send('No jump levels found.')


def create_table_image(table):
    # Create a DataFrame from the table data
    df = pd.read_html(table)[0]

    # Convert DataFrame to an HTML table
    html_table = df.to_html(index=False)

    # Create an in-memory buffer to store the image
    buffer = io.BytesIO()

    # Create an Image object using a white background
    image = Image.new('RGB', (1, 1), color='white')

    # Set the font and font size
    font = ImageFont.truetype('arial.ttf', 12)  # Replace 'arial.ttf' with the path to your desired font file

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw the HTML table onto the image
    draw.text((0, 0), html_table, font=font, fill='black')

    # Save the image to the buffer
    image.save(buffer, format='PNG')
    buffer.seek(0)

    return buffer

bot.run('BOTKEY')
