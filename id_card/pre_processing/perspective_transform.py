import cv2
from glob import glob
import numpy as np

file_path = '/home/ubuntu/kshatra/OCR/id_card/id_card_imgs/belgium3.jpg'
paper = cv2.imread(file_path)
paper = cv2.resize(paper, (1260,820))
pts1 = np.float32([[32,27],[1247,23],[35,798],[1245,795]])
pts2 = np.float32([[0,0],[1260,0],[0,820],[1260,820]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(paper, M, (1260,820))

cv2.imshow("paper", paper)
cv2.imshow("dst", dst)
cv2.imwrite(file_path, dst)
cv2.waitKey(0) 
cv2.destroyAllWindows()