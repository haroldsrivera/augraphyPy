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


def apply_noisy_lines (image):
    noisylines = NoisyLines(noisy_lines_direction = 0,
                            noisy_lines_location = "random",
                            noisy_lines_number_range = (3,5),
                            noisy_lines_color = (0,0,0),
                            noisy_lines_thickness_range = (2,2),
                            noisy_lines_random_noise_intensity_range = (0.01, 0.1),
                            noisy_lines_length_interval_range = (0,100),
                            noisy_lines_gaussian_kernel_value_range = (3,3),
                            noisy_lines_overlay_method = "ink_to_paper",
                            )


    return noisylines(image)

cv2.waitKey(0)
cv2.destroyAllWindows()