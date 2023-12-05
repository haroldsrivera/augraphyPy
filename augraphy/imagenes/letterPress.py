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


def apply_letterpress (image):

        letterpress = Letterpress(n_samples=(200, 500),
                                  n_clusters=(300, 800),
                                  std_range=(1500, 5000),
                                  value_range=(200, 255),
                                  value_threshold_range=(128, 128),
                                  blur=1
                                  )
        return letterpress(image)
cv2.waitKey(0)
cv2.destroyAllWindows()