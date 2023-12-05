import cv2
import numpy as np
from augraphy import *
from markup import apply_markup_strikethrough, apply_markup_highlight, apply_markup_underline, show_image
from bad_photo import apply_bad_photo, apply_bad_photo_2, apply_bad_photo_3, apply_bad_photo_4, apply_bad_photo_5
from bookBinding import apply_book_binder_up
from brightness import apply_brightness_dimmer
from brightnessTexturize import  apply_brightness_texturize
from colorPaper import apply_colorpaper
from colorShift import apply_color_shift
from delaunayTessellation import apply_delaunay_pattern
from dirtyDrum import apply_dirty_drum_1, apply_dirty_drum_2, apply_dirty_drum_3
from dithering import apply_dirther_floyd, apply_dirther_ordered
from dirtyRollers import apply_dirty_rollers
from dotMatrix import apply_dotmatrix
from faxify import apply_faxify
from folding import apply_folding
from inkColorSwap import apply_inkcolor_swap
from letterPress import apply_letterpress
from linesDegradation import apply_lines_degradation, apply_lines_degradation_2
from sombra import apply_bleedtrough
from shadowCast import apply_shadowcast
from scribbles import apply_scribbles
from pageBorder import apply_page_border
from noisyLines import apply_noisy_lines

image = np.full((500, 1300, 3), 250, dtype="uint8")
cv2.putText(
    image,
    "Texto de prueba para generar imagenes sinteticas",
    (80, 250),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.5,
    0,
    3,
)


def show_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    while True:
        print("Seleccione un filtro:")
        print("1. Strikethrough")
        print("2. Highlight")
        print("3. Underline")
        print("4. Bad photo left")
        print("5. Bad photo right")
        print("6. Bad photo 3")
        print("7. Bad photo 4")
        print("8. Bad photo all")
        print("9. Book binder")
        print("10. Brightness dimmer")
        print("11. Brightness texturize")
        print("12. Color paper")
        print("13. Color shift")
        print("14. Delaunay pattern")
        print("15. Dirty drum 1")
        print("16. Dirty drum 2")
        print("17. Dirty drum 3")
        print("18. Dirther ordered")
        print("19. Dirther floyd")
        print("20. Dirty rollers")
        print("21. Dotmatrix")
        print("22. Faxify")
        print("23. Folding")
        print("24. Inkcolor swap")
        print("25. Letterpress")
        print("26. Lines degradation")
        print("27. Lines degradation 2")
        print("28. Bleed through")
        print("29. Shadow cast")
        print("30. Scribbles")
        print("31. Page border")
        print("32. Noisy lines")
        print("0. Salir")

        choice = input("Ingrese su elección: ")

        if choice == '1':
            filtered_image = apply_markup_strikethrough(image)
            show_image("strikethrough", filtered_image)
        elif choice == '2':
            filtered_image = apply_markup_highlight(image)
            show_image("highlight", filtered_image)
        elif choice == '3':
            filtered_image = apply_markup_underline(image)
            show_image("underline", filtered_image)
        elif choice =='4':
            filtered_image = apply_bad_photo(image)
            show_image("bad photo left", filtered_image)
        elif choice == '5':
            filtered_image = apply_bad_photo_2(image)
            show_image("bad photo right", filtered_image)
        elif choice == '6':
            filtered_image = apply_bad_photo_3(image)
            show_image('bad photo 3', filtered_image)
        elif choice == '7':
            filtered_image = apply_bad_photo_4(image)
            show_image('bad photo 4', filtered_image)
        elif choice == '8':
            filtered_image = apply_bad_photo_5(image)
            show_image('bad photo all', filtered_image)
        elif choice == '9':
            filtered_image = apply_book_binder_up(image)
            show_image('book binder', filtered_image)
        elif choice == '10':
            filtered_image = apply_book_binder_up(image)
            show_image('book binder', filtered_image)
        elif choice == '11':
            filtered_image = apply_brightness_dimmer(image)
            show_image('brightness dimmer', filtered_image)
        elif choice == '12':
            filtered_image = apply_brightness_texturize(image)
            show_image('brightness texturize', filtered_image)
        elif choice == '13':
            filtered_image = apply_colorpaper(image)
            show_image('color paper', filtered_image)
        elif choice == '14':
            filtered_image = apply_color_shift(image)
            show_image('color shift', filtered_image)
        elif choice == '15':
            filtered_image = apply_delaunay_pattern(image)
            show_image('delaunay pattern', filtered_image)
        elif choice == '16':
            filtered_image = apply_dirty_drum_1(image)
            show_image('dirty drum 1', filtered_image)
        elif choice == '17':
            filtered_image = apply_dirty_drum_2(image)
            show_image('dirty drum 2', filtered_image)
        elif choice == '18':
            filtered_image = apply_dirty_drum_3(image)
            show_image('dirty drum 3', filtered_image)
        elif choice == '19':
            filtered_image = apply_dirther_ordered(image)
            show_image('dirther ordered', filtered_image)
        elif choice == '20':
            filtered_image = apply_dirther_floyd(image)
            show_image('dirther floyd', filtered_image)
        elif choice == '21':
            filtered_image = apply_dirty_rollers(image)
            show_image('dirty rollers', filtered_image)
        elif choice == '22':
            filtered_image = apply_dotmatrix(image)
            show_image('dotmatrix', filtered_image)
        elif choice == '23':
            filtered_image = apply_faxify(image)
            show_image('faxify', filtered_image)
        elif choice == '24':
            filtered_image = apply_folding(image)
            show_image('folding', filtered_image)
        elif choice == '25':
            filtered_image = apply_inkcolor_swap(image)
            show_image('inkcolor', filtered_image)
        elif choice == '26':
            filtered_image = apply_letterpress(image)
            show_image('letterpress', filtered_image)
        elif choice == '27':
            filtered_image = apply_lines_degradation(image)
            show_image('lines degradation', filtered_image)
        elif choice == '28':
            filtered_image = apply_lines_degradation_2(image)
            show_image('lines degradation 2', filtered_image)
        elif choice == '29':
            filtered_image = apply_bleedtrough(image)
            show_image('bleed trough', filtered_image)
        elif choice == '30':
            filtered_image = apply_shadowcast(image)
            show_image('show cast', filtered_image)
        elif choice == '31':
            filtered_image = apply_scribbles(image)
            show_image('scribbles', filtered_image)
        elif choice == '32':
            filtered_image = apply_page_border(image)
            show_image('page border', filtered_image)
        elif choice == '31':
            filtered_image = apply_noisy_lines(image)
            show_image('noisy lines', filtered_image)
        elif choice == '0':
            break
        else:
            print("Selección no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
    main()
