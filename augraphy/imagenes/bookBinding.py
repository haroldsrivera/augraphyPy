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



def apply_book_binder_up(image):
    book_binder_up = BookBinding(shadow_radius_range=(100, 100),
                                 curve_range_right=(300, 300),
                                 curve_range_left=(300, 300),
                                 curve_ratio_right = (0.3, 0.3),
                                 curve_ratio_left = (0.3, 0.3),
                                 mirror_range=(1.0, 1.0),
                                 binding_align = 0,
                                 binding_pages = (10,10),
                                 curling_direction=0,
                                 backdrop_color=(255, 255, 255),
                                 enable_shadow=1,
                                 use_cache_images = 0,
                                 )

    return book_binder_up(image)

cv2.waitKey(0)
cv2.destroyAllWindows()