import mtcnn
import cv2
def facebox(filename, result_list):
    data=plt.imread(filename)
    plt.imshow(data)
    ax=plt.gca()
    for result in result_list:
        x,y,width,height=result['box']
        rect=plt.Rectangle((x,y),width,height,fill=False,color='green')
        ax.add_patch(rect)
    plt.show()
file="C:/Users/GREEN/Desktop/images/download.jfif"
pixels=plt.imread(file)
detector=mtcnn.MTCNN()
faces=detector.detect_faces(pixels)
facebox(file,faces)

