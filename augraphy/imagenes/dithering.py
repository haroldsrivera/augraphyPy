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


#tipo 1

dirther_ordered = Dithering(dither="ordered", order=(8, 8))


img_dither_ordered = dirther_ordered(image)
cv2.imshow("dither_ordered", img_dither_ordered)

#tipo 2

dirther_floyd = Dithering(dither="floyd" )

img_dither_floyd = dirther_floyd(image)
cv2.imshow("dither_floyd", img_dither_floyd)
cv2.waitKey(0)
cv2.destroyAllWindows()