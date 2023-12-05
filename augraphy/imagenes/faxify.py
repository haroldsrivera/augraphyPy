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



def apply_faxify (image):
    faxify = Faxify(scale_range = (1,2),
                    monochrome = 1,
                    monochrome_method = "cv2.threshold",
                    monochrome_arguments = {"thresh":128, "maxval":128, "type":cv2.THRESH_BINARY},
                    halftone = 1,
                    invert = 1,
                    half_kernel_size = (2,2),
                    angle = (0, 360),
                    sigma = (1,3))
    return faxify(image)

cv2.waitKey(0)
cv2.destroyAllWindows()