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

dirty_rollers = DirtyRollers(line_width_range=(12, 25),
                            scanline_type=0,
                            )

img_dirty_rollers = dirty_rollers(image)
cv2.imshow("dirty_rollers", img_dirty_rollers)

cv2.waitKey(0)
cv2.destroyAllWindows()