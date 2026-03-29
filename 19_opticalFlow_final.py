import numpy as np
import cv2


cap = cv2.VideoCapture('images/people_walking.avi')
width = int(cap.get(3)) 
height = int(cap.get(4))


#                          filename                          encoding (MP4V, DIVX)        fps     frameSize
out = cv2.VideoWriter('optical_flow_walking.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (width, height))


color = np.random.randint(0,255,(100,3))

ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)


mask = np.zeros_like(prev_frame)


feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

prev_corners = cv2.goodFeaturesToTrack(prev_gray, mask = None, **feature_params)


lucas_kanade_params = dict( winSize = (15,15),
                            maxLevel = 2,
                            criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


while(1):
    ret, frame = cap.read()

    if ret == True:
      frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

      # calculate optical flow
      new_corners, status, errors = cv2.calcOpticalFlowPyrLK(prev_gray, 
                                                            frame_gray, 
                                                            prev_corners, 
                                                            None, 
                                                            **lucas_kanade_params)

      # Select and store good points
      if new_corners is not None:
          good_new = new_corners[status==1]
          good_old = prev_corners[status==1]
      else:
          break

      # Draw the tracks
      for i,(new,old) in enumerate(zip(good_new, good_old)):
          a, b = new.ravel()
          c, d = old.ravel()

          a, b, c, d = int(a), int(b), int(c), int(d)
          mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
          frame = cv2.circle(frame, (a,b), 5, color[i].tolist(),-1)
          
      img = cv2.add(frame,mask)

      # Save Video
      out.write(img)

      prev_gray = frame_gray.copy()
      prev_corners = good_new.reshape(-1,1,2)

    else:
      break
    
cap.release()
out.release()



cv2.waitKey(0)
cv2.destroyAllWindows()