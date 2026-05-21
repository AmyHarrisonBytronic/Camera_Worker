from MQTT_Objects.Classes.mqtt_CameraClass import CameraClass
import time

TRIGGER_TOPIC = "camera/capture"
PUBLISH_TOPIC = "camera/image"

def listen_for_capture():
    # This function waits for a capture request to be sent from the broker and then triggers the camera to capture an image.
    # it returns a boolean value indicating whether the capture was received or not.
    camera = CameraClass()
    msg = camera.ListenForMessage()
    print(f"Received message: {msg}")
    if msg is not None:
        print("Capture request received.")
        return True
    return False

def main():
    camera = CameraClass()
    camera.ConnectToCamera()
    camera.ConnectToServer("localhost", 1883)
    camera.SubscribeToTopic(TRIGGER_TOPIC)

    while True:
        time.sleep(1)  # Sleep for a short time to prevent busy waiting
        if listen_for_capture():
            image = camera.GetImageFromCamera()

            if image is not None:
                camera.PublishMessage(PUBLISH_TOPIC, image)
            else:
                print("Failed to capture image.")

if __name__ == "__main__":
    main()