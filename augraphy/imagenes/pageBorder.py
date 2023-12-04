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

page_border = PageBorder(page_border_width_height = (30, -40),
                         page_border_color=(0, 0, 0),
                         page_border_background_color=(255, 255, 255),
                         page_border_use_cache_images = 0,
                         page_border_trim_sides = (0, 0, 0, 0),
                         page_numbers = 10,
                         page_rotate_angle_in_order = 0,
                         page_rotation_angle_range = (1, 5),
                         curve_frequency=(0, 1),
                         curve_height=(1, 2),
                         curve_length_one_side=(30, 60),
                         same_page_border=0,
                         )
img_page_border = page_border(image)
cv2.imshow("page_border", img_page_border)

cv2.waitKey(0)
cv2.destroyAllWindows()