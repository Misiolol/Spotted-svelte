import os
import time
import typer
from instagrapi import Client
import getpass
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer()

def upload_photos(username: str, password: str, folder_path: str):
    try:
        cl = Client()

        cl.login(username, password)

        files = os.listdir(folder_path)

        files.sort()

        upload_interval = 60

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            
            if file_name.endswith(('.jpg', '.jpeg', '.png')):
                media = cl.photo_upload(
                    path=file_path,
                    caption='Your photo caption here'
                )
                typer.echo(f"Uploaded: {file_name}")
            
            time.sleep(upload_interval)

    except Exception as e:
        typer.echo(f"Error: {e}")

@app.command()
def main():
    username = os.getenv('INSTAGRAM_LOGIN')
    password = os.getenv('INSTAGRAM_PASSWORD')
    folder_path = './posts'
    
    upload_photos(username, password, folder_path)

if __name__ == "__main__":
    app()