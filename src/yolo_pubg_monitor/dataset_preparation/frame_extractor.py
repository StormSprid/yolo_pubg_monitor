import cv2
import os

def extract_dataset_from_video(VIDEO_PATHS,OUTPUT_FOLDER,FRAME_STEP,VIDEO_BASE_PATH):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    
    saved_count = 0
    print("Start dataset Extracting...")
    for video_path in VIDEO_PATHS:
        cap = cv2.VideoCapture(os.path.join(VIDEO_BASE_PATH,video_path))
        

        
        count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            if count % FRAME_STEP == 0:
                frame_name = os.path.join(OUTPUT_FOLDER, f"frame_{saved_count:04d}.jpg")
                cv2.imwrite(frame_name, frame)
                saved_count += 1
            count += 1

        cap.release()

    print(f"Done! Saves Frames: {saved_count}")
    print(f"All frames in: {OUTPUT_FOLDER}")

def main():
    VIDEO_PATHS = [
                r'1_test.mp4',
                r'2_test.mp4'
              ]  
    OUTPUT_FOLDER = os.path.join('dataset','dataset_frames') 
    FRAME_STEP = 30 
    VIDEO_BASE_PATH = os.path.join('dataset', 'videos')
    extract_dataset_from_video(VIDEO_PATHS,OUTPUT_FOLDER,FRAME_STEP,VIDEO_BASE_PATH)


if __name__ == '__main__':
   main()