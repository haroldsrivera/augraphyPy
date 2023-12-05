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



#tipo 1
def apply_bad_photo(image):
    BadPhotoCopy_type_1 = BadPhotoCopy(noise_type=1,
                                       noise_side="left",
                                       noise_iteration=(2,3),
                                       noise_size=(2,3),
                                       noise_sparsity=(0.15,0.15),
                                       noise_concentration=(0.3,0.3),
                                       blur_noise=-1,
                                       blur_noise_kernel=(5, 5),
                                       wave_pattern=0,
                                       edge_effect=0)
    return BadPhotoCopy_type_1(image)

#tipo 2
def apply_bad_photo_2(image):
    BadPhotoCopy_type_2 = BadPhotoCopy(noise_type=2,
                                       noise_side="right",
                                       noise_iteration=(1,1),
                                       noise_size=(1,1),
                                       noise_sparsity=(0.4,0.5),
                                       noise_concentration=(0.2,0.2),
                                       blur_noise=1,
                                       blur_noise_kernel=(5, 5),
                                       wave_pattern=0,
                                       edge_effect=1)
    return BadPhotoCopy_type_2(image)


#tipo 3
def apply_bad_photo_3(image):
    BadPhotoCopy_type_3 = BadPhotoCopy(noise_type=3,
                                       noise_side="none",
                                       noise_iteration=(1,1),
                                       noise_size=(1,3),
                                       noise_value=(128, 255),
                                       noise_sparsity=(0.2,0.3),
                                       noise_concentration=(0.5,0.5),
                                       blur_noise=1,
                                       blur_noise_kernel=(5, 5),
                                       wave_pattern=0,
                                       edge_effect=1)
    return BadPhotoCopy_type_3(image)
#tipo 4

def apply_bad_photo_4(image):
    BadPhotoCopy_type_4 = BadPhotoCopy(noise_type=4,
                                       noise_side="none",
                                       noise_iteration=(1,1),
                                       noise_size=(1,3),
                                       noise_value=(32, 255),
                                       noise_sparsity=(0.5,0.5),
                                       noise_concentration=(0.99,0.99),
                                       blur_noise=0,
                                       wave_pattern=0,
                                       edge_effect=0)
    return BadPhotoCopy_type_4(image)

def apply_bad_photo_5(image):
    #tipo 5
    BadPhotoCopy_type_5 = BadPhotoCopy(noise_type=5,
                                       noise_side="all",
                                       noise_iteration=(1,1),
                                       noise_size=(1,3),
                                       noise_value=(32, 128),
                                       noise_sparsity=(0.3,0.3),
                                       noise_concentration=(0.5,0.5),
                                       blur_noise=0,
                                       wave_pattern=0,
                                       edge_effect=0)
    return BadPhotoCopy_type_5(image)

cv2.waitKey(0)
cv2.destroyAllWindows()