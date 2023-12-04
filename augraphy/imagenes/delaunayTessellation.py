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
delaunay_pattern = DelaunayTessellation(
                                        n_points_range = (500, 800),
                                        n_horizontal_points_range=(50, 100),
                                        n_vertical_points_range=(50, 100),
                                        noise_type = "random")

img_final = delaunay_pattern(image)
cv2.imshow("Delaunay Image", img_final)

cv2.waitKey(0)
cv2.destroyAllWindows()