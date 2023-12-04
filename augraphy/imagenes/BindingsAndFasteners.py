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
binder_punch_holes = BindingsAndFasteners(overlay_types="darken",
                                          foreground=None,
                                          effect_type="punch_holes",
                                          width_range = (70,80),
                                          height_range = (70,80),
                                          ntimes=(3, 3),
                                          nscales=(1.5, 1.5),
                                          edge="left",
                                          edge_offset=(30,50),
                                          use_figshare_library=0,
                                          )

img_punch_holes =binder_punch_holes(image)
cv2.imshow("punch_holes", img_punch_holes)

#tipo2

binder_binding_holes = BindingsAndFasteners(overlay_types="darken",
                                            foreground=None,
                                            effect_type="binding_holes",
                                            width_range = "random",
                                            height_range = "random",
                                            ntimes=(9, 10),
                                            nscales=(1, 2),
                                            edge="top",
                                            edge_offset=(40,50),
                                            use_figshare_library=0,
                                            )

img_binding_holes =binder_binding_holes(image)
cv2.imshow("binding_holes", img_binding_holes)

#tipo 3
binder_binding_clips = BindingsAndFasteners(overlay_types="darken",
                                            foreground=None,
                                            effect_type="clips",
                                            width_range = "random",
                                            height_range = "random",
                                            ntimes= (2, 3),
                                            nscales=(1, 2),
                                            edge="random",
                                            edge_offset=(10,20),
                                            use_figshare_library=0,
                                            )

img_binding_clips = binder_binding_clips(image)
cv2.imshow("clips",img_binding_clips)

#tipo 4
binder_rectangle = np.full((50,20),fill_value=250,dtype="uint8")
binder_rectangle[10:40,5:15] = 0


user_binder_clips = BindingsAndFasteners(overlay_types="darken",
                                         foreground=binder_rectangle,
                                         ntimes= (2, 3),
                                         nscales=(1, 2),
                                         edge="right",
                                         edge_offset=(10,20),
                                         use_figshare_library=0,
                                         )

img_user_binder = user_binder_clips(image)
cv2.imshow("user binders",img_user_binder)

cv2.waitKey(0)
cv2.destroyAllWindows()