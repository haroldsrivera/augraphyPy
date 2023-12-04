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

colorpaper= ColorPaper(hue_range=(0, 10), saturation_range=(10,30))

img_colorpaper = colorpaper(image)
cv2.imshow("colorpaper", img_colorpaper)

cv2.waitKey(0)
cv2.destroyAllWindows()