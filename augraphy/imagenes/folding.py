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

folding = Folding(fold_count=10,
                  fold_noise=0.0,
                  fold_angle_range = (-360,360),
                  gradient_width=(0.1, 0.2),
                  gradient_height=(0.01, 0.1),
                  backdrop_color = (0,0,0),
                  )

img_folded= folding(image)
cv2.imshow("folding", img_folded)

cv2.waitKey(0)
cv2.destroyAllWindows()