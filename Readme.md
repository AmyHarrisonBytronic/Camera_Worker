# Example camera microsservice

This repo contains a simple camera worker that listens for a trigger command, captures images from the camera when ordered and sends them to an mqtt topic listed in the yaml file.

## Yaml

The yaml file contains the topic for the camera to send the data to, a topic to listen for a trigger phrase and the ip and port for the mqtt broker
currently the messgae field is not doing anything but it should be used to set the trigger phrase.

# Process

worker will subscribe to a trigger topic and capture and send an image when it is requested by using the mqtt library 
the image will be sent over a set topic to the mqtt broker
