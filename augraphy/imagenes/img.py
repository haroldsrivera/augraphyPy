from augraphy import *
import cv2
import numpy as np

image = cv2.imread("texto_imagen.jpg")

# create an example of mask
mask = np.zeros((image.shape[0], image.shape[1]), dtype="uint8")
mask[image[:,:,0]==0] = 255

# create an example of keypoints
points = []
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        if np.sum(image[y,x])<5:
            if not y%5:
                if not x%5:
                    points += [[x, y]]
keypoints = {"words":points}

# create an example of bounding boxes
bounding_boxes = [[79, 220, 199, 256],
                  [214, 219, 329, 264],
                  [347, 220, 445, 255],
                  [460, 219, 505, 255],
                  [522, 220, 630, 260],
                  [650, 220, 873, 256],
                  [888, 220, 1075, 265],
                  [1091, 218, 1150, 256]]

# create augmentation pipeline
ink_phase = [SectionShift()]
paper_phase = []
post_phase = [Geometric(rotate_range=(-5,5)),
              Folding()]
pipeline = AugraphyPipeline(ink_phase=ink_phase,
                            paper_phase=paper_phase,
                            post_phase=post_phase,
                            mask=mask,
                            keypoints = keypoints,
                            bounding_boxes = bounding_boxes)


augmented_image, augmented_mask, augmented_keypoints, augmented_bounding_boxes = pipeline(image)

# initialize input and output image for keypoints and bounding boxes
keypoints_image = np.zeros((image.shape[0], image.shape[1]), dtype="uint8")
bounding_boxes_image = np.zeros((image.shape[0], image.shape[1]), dtype="uint8")
augmented_keypoints_image = np.zeros((augmented_image.shape[0], augmented_image.shape[1]), dtype="uint8")
augmented_bounding_boxes_image = np.zeros((augmented_image.shape[0], augmented_image.shape[1]), dtype="uint8")

# plot keypoints
# input
for keypoint in keypoints["words"]:
    keypoints_image[keypoint[1], keypoint[0]] = 255
# output
for keypoint in augmented_keypoints["words"]:
    augmented_keypoints_image[keypoint[1], keypoint[0]] = 255

# plot bounding boxes
# input
for bounding_box in bounding_boxes:
    cv2.rectangle(bounding_boxes_image, (bounding_box[0],bounding_box[1]), (bounding_box[2],bounding_box[3]), color=(255,255,255), thickness=1)
# output
for bounding_box in augmented_bounding_boxes:
    cv2.rectangle(augmented_bounding_boxes_image, (bounding_box[0],bounding_box[1]), (bounding_box[2],bounding_box[3]), color=(255,255,255), thickness=1)

# ...
# Convertir imágenes binarias en matrices NumPy
augmented_bounding_boxes_np = np.array(augmented_bounding_boxes, dtype=np.uint8)
augmented_bounding_boxes_image_np = np.array(augmented_bounding_boxes_image, dtype=np.uint8)

# ...

# Mostrar las imágenes convertidas


# ...

cv2.imshow("input image", image)
cv2.imshow("augmented",augmented_image)

cv2.imshow("input mask", mask)
cv2.imshow("augmented mask",augmented_mask)

cv2.imshow("input keypoints", keypoints_image)
cv2.imshow("augmented keypoints",augmented_keypoints_image)

cv2.imshow("augmented bounding boxes", augmented_bounding_boxes_np)
cv2.imshow("augmented bounding boxes", augmented_bounding_boxes_image_np)

# Espera una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()