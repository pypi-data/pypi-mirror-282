import cv2
from pathlib import Path

def video_frames_generator(video_path, start_frame, end_frame):
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Define the contrast and brightness values
    alpha = 1.2  # Contrast control (1.0-3.0)
    beta = 0  # Brightness control (0-100)


    for i in range(start_frame, end_frame):
        ret, frame = cap.read()
        adjusted_frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
        adjusted_frame[adjusted_frame < 100] = 50
        if not ret:
            break
        yield adjusted_frame

    cap.release()

# Example usage:
VIDEO_PATH = Path(
        '/Volumes/data2/GO/7cam/221223_aJO-GAL4xUAS-CsChr/Fly001/002_Beh/behData/videos/camera_3.mp4')
start_frame = 100
end_frame = 200
frames_generator = video_frames_generator(str(VIDEO_PATH), start_frame, end_frame)
# from IPython import embed; embed()
# Do something with the frames, e.g. display them:
for frame in list(frames_generator):
    cv2.imshow('Frame', frame)
    cv2.waitKey(500)

cv2.destroyAllWindows()
