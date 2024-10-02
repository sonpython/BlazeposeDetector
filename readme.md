
# BlazePose Camera Stream Add-on

This add-on uses BlazePose to stream from a camera and integrate it into Home Assistant as a camera entity. The video is streamed via a Flask server and can be used as a real-time video feed inside Home Assistant.

## Features
- Real-time pose detection using BlazePose.
- Easily integrated into Home Assistant as an MJPEG camera feed.
- Configurable camera index to choose which camera to use.

## Installation

### Step 1: Add Repository to Home Assistant

1. Open Home Assistant.
2. Navigate to **Settings > Add-ons > Add-on Store**.
3. In the bottom right, click on the **"Repositories"** button.
4. In the **"Add repository by URL"** field, enter the URL of this repository:

   ```
   https://github.com/sonpython/home-assistant-blazepose-addon
   ```

   Replace `username` with your GitHub username if you have forked or modified this repository.

5. Click **Add**, and the repository will now appear in the add-on store.

### Step 2: Install and Configure the Add-on

1. After adding the repository, find **BlazePose Camera Stream** in the list of available add-ons and click on it.
2. Click **Install** to install the add-on.
3. After installation, navigate to the **Configuration** tab to set your preferred options:
   - **Camera Index**: Select the index of the camera you want to use (`0` for the default camera, `1` for an external one, etc.).
4. Click **Save** to save your configuration.

### Step 3: Start the Add-on

1. Go back to the **Info** tab and click **Start** to start the add-on.
2. Once the add-on is started, the video feed will be available at:

   ```
   http://<YOUR_HA_IP>:5001/video_feed
   ```

   Replace `<YOUR_HA_IP>` with the IP address of your Home Assistant server.

### Step 4: Add Camera to Home Assistant

To use the video stream as a camera in Home Assistant, add the following configuration to your `configuration.yaml` file:

```yaml
camera:
  - platform: mjpeg
    name: BlazePose Camera
    mjpeg_url: http://<YOUR_HA_IP>:5001/video_feed
```

Replace `<YOUR_HA_IP>` with the IP address of your Home Assistant server.

After adding this configuration, restart Home Assistant for the changes to take effect. You should now see the **BlazePose Camera** as an available camera entity in Home Assistant.

## Configuration Options

- **camera_index**: Integer. Set the camera index (`0` for default camera, `1` for external camera, etc.). This allows the user to select which camera to use if there are multiple connected to the host.

## Notes

- Ensure that Docker has access to the camera device on the host.
- The add-on uses the `--device` flag to map the camera (`/dev/video0`). If you have multiple cameras, update the configuration appropriately.

## Troubleshooting

1. **No Video Feed**: 
   - Ensure that the correct camera index is selected.
   - Check if the camera is properly connected and accessible.
   - Ensure Docker is given the correct permissions to access the camera.

2. **Add-on Crashes**:
   - Check the logs in the **Log** tab of the add-on for any error messages.
   - If there is a specific error related to the camera, try restarting the add-on or selecting a different camera index.

## About

This add-on is part of the BlazePose Add-ons repository, providing easy integration of AI-powered pose detection into Home Assistant for real-time monitoring and automation.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

### Summary of Changes
- Provided detailed instructions for adding the repository to Home Assistant.
- Described how to install, configure, and start the add-on.
- Added details on how to add the video stream as a camera entity in Home Assistant.
- Included configuration options for selecting the camera index.
- Added troubleshooting steps to help users resolve common issues.
