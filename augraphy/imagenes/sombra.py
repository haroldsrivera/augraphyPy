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

bleedthrough = BleedThrough(intensity_range=(0.1, 0.2),
                            color_range=(0, 224),
                            ksize=(17, 17),
                            sigmaX=0,
                            alpha=0.3,
                            offsets=(50, 30),
                        )

img_bleedthrough = bleedthrough(image)
cv2.imshow("bleedthrough", img_bleedthrough)

cv2.waitKey(0)
cv2.destroyAllWindows()