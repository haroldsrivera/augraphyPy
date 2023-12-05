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



def apply_dotmatrix (image):

        dotmatrix = DotMatrix(dot_matrix_shape="circle",
                              dot_matrix_dot_width_range=(5, 5),
                              dot_matrix_dot_height_range=(5, 5),
                              dot_matrix_min_width_range=(1, 1),
                              dot_matrix_max_width_range=(50, 50),
                              dot_matrix_min_height_range=(1, 1),
                              dot_matrix_max_height_range=(50, 50),
                              dot_matrix_min_area_range=(10, 10),
                              dot_matrix_max_area_range=(800, 800),
                              dot_matrix_median_kernel_value_range = (29,29),
                              dot_matrix_gaussian_kernel_value_range=(1, 1),
                              dot_matrix_rotate_value_range=(0, 0)
                              )

        return dotmatrix(image)

cv2.waitKey(0)
cv2.destroyAllWindows()