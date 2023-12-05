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



def apply_brightness_dimmer(image):
    brightness_dimmer= Brightness(brightness_range=(0.2, 0.8),
                                    min_brightness=1,
                                    min_brightness_value=(120, 150),
                            )
    return brightness_dimmer(image)

cv2.waitKey(0)
cv2.destroyAllWindows()