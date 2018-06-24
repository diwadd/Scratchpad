import cv2
import glob
import sys

if __name__ == "__main__":

    path_to_images = sys.argv[1]
    print("Provided path: " + str(path_to_images))
    list_of_image_file_names = glob.glob(path_to_images + "/*.JPG")


    print(list_of_image_file_names)

    scaling_factor = 0.5
    n_images = len(list_of_image_file_names)
    for i in range(n_images):

        image_file_names = list_of_image_file_names[i]
        print("Processing image: " + str(image_file_names))

        img = cv2.imread(image_file_names)
        img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

        cv2.imwrite(image_file_names.replace("DSC","small_" + str(scaling_factor) + "_DSC"), img)
