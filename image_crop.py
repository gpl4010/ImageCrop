import cv2
import copy
import os

data_dir="./"
count=0
img= 0
clone =0
dir2 =0

# 마우스 이벤트 콜백 함수
def cap_roi(event, x, y, flags, param):
    global count
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x-50,y-50), (x+50,y+50), (0, 0, 255), 2)
        roi = clone[y-50:y+50, x-50:x+50]
        cv2.imshow("image", img)
        count+=1
        cv2.imwrite(os.path.join(dir2,filename[:-4]+"_resize"+str(count)+".jpg"), roi)
        cv2.waitKey(0)

# 이미지 불러오기
for filename in os.listdir(data_dir):
    if filename.endswith('.jpg'):
        img = cv2.imread(os.path.join(data_dir,filename))
        #img.resize(1600,1000)
        clone = copy.deepcopy(img)
    
        count=0
        dir2= filename[:-4]+"_resize"
        os.mkdir(dir2)

        # 윈도우를 생성하고 마우스 이벤트에 콜백 함수 연결
        cv2.namedWindow("image",flags=cv2.WINDOW_NORMAL)
        cv2.resizeWindow(winname="image",width=1920,height=1080)
        cv2.setMouseCallback("image", cap_roi)

        # 이미지를 표시하고 키 입력 대기
        while True:
            cv2.imshow("image", img)
            key = cv2.waitKey(1) & 0xFF

            # 종료
            if key == 27:
                break

        # 모든 창 닫기
        cv2.destroyAllWindows()