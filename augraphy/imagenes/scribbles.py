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


def apply_scribbles (image):

        scribbles = Scribbles(scribbles_type="random",
                              scribbles_ink="random",
                              scribbles_location="random",
                              scribbles_size_range=(400, 600),
                              scribbles_count_range=(1, 6),
                              scribbles_thickness_range=(1, 3),
                              scribbles_brightness_change=[8, 16],
                              scribbles_skeletonize=0,
                              scribbles_skeletonize_iterations=(2, 3),
                              scribbles_color="random",
                              scribbles_text="random",
                              scribbles_text_font="random",
                              scribbles_text_rotate_range=(0, 360),
                              scribbles_lines_stroke_count_range=(1, 6),
                              )
        return scribbles(image)



cv2.waitKey(0)
cv2.destroyAllWindows()