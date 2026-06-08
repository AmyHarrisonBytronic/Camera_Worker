# Example Camera Worker

Example Camera Worker is a Python MQTT camera capture worker.
It listens for capture requests on a configured MQTT trigger topic and publishes captured images to a configured MQTT image topic.

## Features

- MQTT trigger subscription
- Camera capture using OpenCV or an external Pylon camera implementation
- Image publish over MQTT
- YAML-based configuration in `app/Dependencies/config.yaml`

## Repository structure

- `app/` - application source code and entrypoint
- `app/Dependencies/` - configuration loader and YAML config file
- `docs/` - project documentation and notes
- `test/` - automated tests and test helpers
- `tools/` - development utilities and scripts
- `requirements.txt` - Python dependency list

## Prerequisites

- Python 3.8+
- `opencv-python` for `cv2`
- `PyYAML` for YAML configuration
- MQTT client library or external MQTT integration for the Pylon camera implementation

> Note: The repository currently imports a `PylonClass` from `MQTT_Objects.Classes.mqtt_Camera_PylonClass`. That class is expected to be available on `PYTHONPATH` or installed separately when `camera_type` is set to `pylon`.

## Configuration

The app reads values from `app/Dependencies/config.yaml`.

Important configuration keys:

- `ip` - MQTT broker hostname or IP address
- `port` - MQTT broker port
- `trigger_topic` - topic to subscribe to for capture requests
- `image_topic` - topic to publish captured image data
- `message` - optional message payload value
- `camera_type` - `opencv` or `pylon`

## Running the worker

From the repository root:

```powershell
python app/main.py
```

## Testing

Run the available tests with pytest:

```powershell
pytest test
```

## Notes

- `camera_type: opencv` uses the local default webcam via OpenCV.
- `camera_type: pylon` uses the external Pylon camera class and requires that the external module is installed and available.
- The current `requirements.txt` should be updated with the actual dependencies used by the project.
