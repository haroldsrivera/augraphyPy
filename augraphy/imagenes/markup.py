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

#1
markup_strikethrough = Markup(num_lines_range=(5, 7),
                              markup_length_range=(0.5, 1),
                              markup_thickness_range=(1, 2),
                              markup_type="strikethrough",
                              markup_ink = "pencil",
                              markup_color=(0, 0, 255),
                              repetitions=4,
                              large_word_mode=1,
                              single_word_mode=False)

img_markup_strikethrough = markup_strikethrough(image)
cv2.imshow("markup_strikethrough", img_markup_strikethrough)

#2
markup_highlight = Markup(num_lines_range=(1, 1),
                          markup_length_range=(0.5, 1),
                          markup_thickness_range=(5, 5),
                          markup_type="highlight",
                          markup_ink="highlighter",
                          markup_color=(0, 255, 0),
                          repetitions=1,
                          large_word_mode=1,
                          single_word_mode=False)

img_markup_highlight = markup_highlight(image)
cv2.imshow("markup_highlight", img_markup_highlight)


#3

markup_underline = Markup(num_lines_range=(1, 1),
                          markup_length_range=(0.5, 1),
                          markup_thickness_range=(2, 2),
                          markup_type="underline",
                          markup_ink="marker",
                          markup_color=(255, 0, 0),
                          repetitions=1,
                          large_word_mode=1,
                          single_word_mode=False)

img_markup_underline = markup_underline(image)
cv2.imshow("markup_underline", img_markup_underline)


cv2.waitKey(0)
cv2.destroyAllWindows()