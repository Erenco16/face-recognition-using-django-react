from deepface import DeepFace               
import cv2
import matplotlib.pyplot as plt

def verify(img_path_1, img_path_2):
    img1 = cv2.imread(img_path_1)
    img2 = cv2.imread(img_path_2)

    plt.imshow(img1[:,:,::-1])
    plt.show()
    plt.imshow(img2[:,:,::-1])
    plt.show()
    output = DeepFace.verify(img_path_1, img_path_2)
    print(output)
    verification = output['Verified']
    if verification:
        print("Faces are the same")
    else:
        print("Faces are not the same")

def main():
    img1_path = "/Users/godfather/Desktop/Software/connect_django_to_react/backend/photos/eren-b/adsslfkjsdlkfgjsrfy@gmail.com-3s4iN.jpg"
    img2_path = "/Users/godfather/Desktop/Software/connect_django_to_react/backend/photos/eren-b/adsslfkjsdlkfgjsrfy@gmail.com-8fCkY.jpg"
    verify(img1_path, img2_path)

if __name__ == "__main__":
    main()