import cv2
import numpy as np
import urllib.request

def loop_video_from_url(url):
    try:
        video_stream = urllib.request.urlopen(url)
        bytes = b''
        cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
        
        while True:
            bytes += video_stream.read(1024)
            a = bytes.find(b'\xff\xd8')
            b = bytes.find(b'\xff\xd9')
            
            if a != -1 and b != -1:
                frame = cv2.imdecode(np.fromstring(bytes[a:b+2], dtype=np.uint8), cv2.IMREAD_COLOR)
                cv2.imshow('Video', frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
                bytes = bytes[b+2:]
                
        video_stream.close()
        
    except Exception as e:
        print(f"Error: {e}")

    cv2.destroyAllWindows()

# Example usage:
video_url = "https://example.com/video.mp4"
loop_video_from_url(video_url)
