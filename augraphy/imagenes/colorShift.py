# import libraries
import cv2
import numpy as np
from augraphy import *

ink_phase   = [InkShifter()]
paper_phase = [VoronoiTessellation(p=1)]
post_phase  = [GlitchEffect()]
image = np.full((500, 1500,3), 250, dtype="uint8")
cv2.putText(
    image,
    "Texto de prueba para generar imagenes sinteticas",
    (80, 250),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.5,
    0,
    3,
)


cv2.imshow("Input image", image)

colorshift = ColorShift(color_shift_offset_x_range = (3,5),
                        color_shift_offset_y_range = (3,5),
                        color_shift_iterations = (2,3),
                        color_shift_brightness_range = (0.9,1.1),
                        color_shift_gaussian_kernel_range = (3,3),
                        )

img_colorshift = colorshift(image)
cv2.imshow("colorshift", img_colorshift)

cv2.waitKey(0)
cv2.destroyAllWindows()