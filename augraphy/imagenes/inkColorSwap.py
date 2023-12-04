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

#1

inkcolorswap= InkColorSwap(ink_swap_color = "random",
                           ink_swap_sequence_number_range = (1,10),
                           ink_swap_min_width_range=(3,3),
                           ink_swap_max_width_range=(100,100),
                           ink_swap_min_height_range=(3,3),
                           ink_swap_max_height_range=(100,100),
                           ink_swap_min_area_range=(10,10),
                           ink_swap_max_area_range=(400,400)
                           )

img_inkcolorswap = inkcolorswap(image)

cv2.imshow("inkcolorswap", img_inkcolorswap)

cv2.waitKey(0)
cv2.destroyAllWindows()