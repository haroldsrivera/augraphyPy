import cv2
import numpy as np
from augraphy import *

# Define los filtros como métodos
def apply_markup_strikethrough(image):
    markup_strikethrough = Markup(num_lines_range=(5, 7),
                                  markup_length_range=(0.5, 1),
                                  markup_thickness_range=(1, 2),
                                  markup_type="strikethrough",
                                  markup_ink="pencil",
                                  markup_color=(0, 0, 255),
                                  repetitions=4,
                                  large_word_mode=1,
                                  single_word_mode=False)
    return markup_strikethrough(image)

def apply_markup_highlight(image):
    markup_highlight = Markup(num_lines_range=(1, 1),
                              markup_length_range=(0.5, 1),
                              markup_thickness_range=(5, 5),
                              markup_type="highlight",
                              markup_ink="highlighter",
                              markup_color=(0, 255, 0),
                              repetitions=1,
                              large_word_mode=1,
                              single_word_mode=False)
    return markup_highlight(image)

def apply_markup_underline(image):
    markup_underline = Markup(num_lines_range=(1, 1),
                              markup_length_range=(0.5, 1),
                              markup_thickness_range=(2, 2),
                              markup_type="underline",
                              markup_ink="marker",
                              markup_color=(255, 0, 0),
                              repetitions=1,
                              large_word_mode=1,
                              single_word_mode=False)
    return markup_underline(image)

# Crear la imagen base
image = np.full((500, 1500, 3), 250, dtype="uint8")
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
        print("4. Salir")

        choice = input("Ingrese su elección: ")

        if choice == '1':
            filtered_image = apply_markup_strikethrough(image)
            show_image("Strikethrough", filtered_image)
        elif choice == '2':
            filtered_image = apply_markup_highlight(image)
            show_image("Highlight", filtered_image)
        elif choice == '3':
            filtered_image = apply_markup_underline(image)
            show_image("Underline", filtered_image)
        elif choice == '4':
            break
        else:
            print("Selección no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
    main()
