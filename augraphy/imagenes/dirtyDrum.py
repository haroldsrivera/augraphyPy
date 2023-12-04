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
dirtydrum1 = DirtyDrum(line_width_range=(1, 4),
                      line_concentration=0.1,
                      direction=0,
                      noise_intensity=0.5,
                      noise_value=(0, 30),
                      ksize=(3, 3),
                      sigmaX=0,
                      )

img_dirtydrum1 = dirtydrum1(image)
cv2.imshow("dirtydrum1", img_dirtydrum1)


#tipo 2

dirtydrum2 = DirtyDrum(line_width_range=(5, 10),
                      line_concentration=0.3,
                      direction=1,
                      noise_intensity=0.2,
                      noise_value=(0, 10),
                      ksize=(3, 3),
                      sigmaX=0,
                      )

img_dirtydrum2 = dirtydrum2(image)
cv2.imshow("dirtydrum2", img_dirtydrum2)

#tipo 3


dirtydrum3 = DirtyDrum(line_width_range=(2, 5),
                      line_concentration=0.3,
                      direction=2,
                      noise_intensity=0.4,
                      noise_value=(0, 5),
                      ksize=(3, 3),
                      sigmaX=0,
                      )

img_dirtydrum3 = dirtydrum3(image)
cv2.imshow("dirtydrum3", img_dirtydrum3)

cv2.waitKey(0)
cv2.destroyAllWindows()