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


def apply_brightness_texturize(image):

    brightness_texturize = BrightnessTexturize(texturize_range=(0.9, 0.99),
                                               deviation=0.1 )

    return brightness_texturize (image)
cv2.waitKey(0)
cv2.destroyAllWindows()