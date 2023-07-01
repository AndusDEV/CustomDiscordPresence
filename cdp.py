from pypresence import Presence
import time

def set_discord_rpc():
    client_id = '1124743681308635156'  # Replace with your Discord application's client ID
    RPC = Presence(client_id)
    RPC.connect()

    details = "This is a custom"
    state = "Discord Presence"
    large_image = "large_image"  # Replace with the key of your large image asset
    large_text = "This is a large image"
    small_image = "small_image"  # Replace with the key of your small image asset
    small_text = "This is a small image"

    RPC.update(
        details=details,
        state=state,
        large_image=large_image,
        large_text=large_text,
        small_image=small_image,
        small_text=small_text
    )

    while True:
        time.sleep(15)

if __name__ == '__main__':
    set_discord_rpc()