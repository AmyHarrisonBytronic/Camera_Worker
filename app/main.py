from MQTT_Objects.Classes.mqtt_CameraClass import CameraClass
import time
import asyncio
import threading

IP = "localhost"
PORT = 1883
TRIGGER_TOPIC = "trigger/capture"
PUBLISH_TOPIC = "camera/image"

def start_async_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def listen_for_capture():
    # This function waits for a capture request to be sent from the broker and then triggers the camera to capture an image.
    # it returns a boolean value indicating whether the capture was received or not.
    camera = CameraClass()
    msg = await camera.ListenForMessage()
    if msg is not None and msg.topic == TRIGGER_TOPIC:
        print("Capture request received.")
        return True
    return False

def main():
    camera = CameraClass()
    camera.ConnectToCamera()
    camera.ConnectToServer(IP, PORT)
    camera.SubscribeToTopic(TRIGGER_TOPIC)

    loop = asyncio.new_event_loop()
    t = threading.Thread(target=listen_for_capture, args=(loop,), daemon=True)
    t.start()

    asyncio.run_coroutine_threadsafe(camera.ListenForMessage(), loop)

    time.sleep(0.1)

    while True:
        time.sleep(1)  # Sleep for a short time to prevent busy waiting
        if listen_for_capture():
            print("Capturing image...")
            image = camera.GetImageFromCamera()

            if image is not None:
                camera.PublishMessage(PUBLISH_TOPIC, image)
            else:
                print("Failed to capture image.")

if __name__ == "__main__":
    main()