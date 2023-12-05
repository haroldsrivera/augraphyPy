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



def apply_lines_degradation(image):

    lines_degradation = LinesDegradation(line_roi = (0.0, 0.0, 1.0, 1.0),
                                         line_gradient_range=(32, 255),
                                         line_gradient_direction= (1,1),
                                         line_split_probability=(0.2, 0.3),
                                         line_replacement_value=(250, 250),
                                         line_min_length=(15, 15),
                                         line_long_to_short_ratio = (3,3),
                                         line_replacement_probability = (0.5, 0.5),
                                         line_replacement_thickness = (1, 2)
                                         )
    return lines_degradation(image)

#2
def apply_lines_degradation_2(image):
    lines_degradation = LinesDegradation(line_roi = (0.0, 0.0, 0.5, 1.0),
                                         line_gradient_range=(32, 255),
                                         line_gradient_direction= (2,2),
                                         line_split_probability=(0.2, 0.3),
                                         line_replacement_value=(0, 25),
                                         line_min_length=(15, 15),
                                         line_long_to_short_ratio = (3,3),
                                         line_replacement_probability = (1.0, 1.0),
                                         line_replacement_thickness = (2, 2)
                                         )
    return lines_degradation(image)


cv2.waitKey(0)
cv2.destroyAllWindows()