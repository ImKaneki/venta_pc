import reflex as rx

def index() -> rx.Component:
    return rx.container(
        # Botón para cambiar el tema
        rx.color_mode.button(position="absolute", top="1rem", right="1rem"),
        
        # Contenedor principal de la página
        rx.vstack(
            # Contenedor para el título, texto y botones en la parte superior
            rx.hstack(
                # Columna de imágenes a la izquierda
                rx.vstack(
                    rx.image(
                        src="https://cdn.shopify.com/s/files/1/0098/7247/4167/files/pc_gaming_con_setup_de_luces_led.jpg?v=1630513725",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    rx.image(
                        src="https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2023/04/21/pc-gamer-thumb-ts56rack6f6u.jpg",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    spacing="5",  # Espaciado entre las imágenes
                    align="center",  # Alineación centrada
                    margin_right="6rem",  # Espaciado entre las imágenes y el contenido de la derecha
                ),
                
                # Espaciador para centrar el título y texto
                rx.spacer(flex="1"),  # Esto asegura que el contenido se quede centrado
                
                # Contenedor para el título, texto y botones en la parte derecha
                rx.vstack(
                    # Contenedor con título y texto
                    rx.vstack(
                        # Título centrado
                        rx.heading("¡Bienvenido a app venta pc!", size="2xl", color="green", text_align="center"),
                        
                        # Descripción centrada
                        rx.text(
                            "Nuestra aplicación te permite configurar y comprar la PC perfecta para tus necesidades, desde un simple ordenador de oficina hasta una máquina de gaming de última generación. . "
                            "¿Te has sentido frustrado al buscar una PC que realmente se adapte a tus necesidades? ¿Te han vendido una PC pre-armada que no te convence? ¡No te preocupes, amigo!.",
                            size="md",
                            color="white",
                            max_width="40rem",
                            text_align="center",  # Centrado del texto
                            margin_top="1rem",  # Margen superior para el texto
                        ),
                        spacing="6",  # Espaciado entre el título y el texto
                        align="center",  # Alineación centrada
                    ),
                    
                    # Botones en la parte superior derecha
                    rx.hstack(
                        # Botón "Regístrate aquí"
                        rx.link(
                            rx.button("¡Regístrate aquí!", color_scheme="green"),
                            href="https://docs.google.com/forms/d/1Qm54XmIdT-uwr5M0kftktM8SAkplAmXjhLxB5s0WbRg/edit",
                            is_external=True,
                        ),  
                        # Botón "Facebook" 
                        rx.link(
                            rx.button(rx.icon(tag="facebook"), color_scheme="blue"),
                            href="https://facebook.com",
                            is_external=True,
                        ),
                        # Botón "Instagram"
                        rx.link(
                            rx.button(rx.icon(tag="instagram"), color_scheme="pink"),
                            href="https://instagram.com",
                            is_external=True,
                        ),
                        spacing="4",  # Espaciado entre los botones
                        align="end",  # Alineación de los botones a la derecha
                    ),
                    
                    # Espaciado para que los botones no se peguen al contenido
                    margin_top="2rem",
                ),
                
                # Columna de imágenes a la derecha
                rx.vstack(
                    rx.image(
                        src="https://i.blogs.es/8c3c21/pcbuild2/1366_2000.jpg",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="14rem",  # Tamaño ajustado para la imagen
                    ),
                    rx.image(
                        src="https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/media/image/2023/05/torre-gaming-3036108.jpg?tf=3840x",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="14rem",  # Tamaño ajustado para la imagen
                    ),
                    spacing="7",  # Espaciado entre las imágenes
                    align="center",  # Alineación centrada
                    margin_left="6rem",  # Espaciado entre las imágenes y el contenido de la izquierda
                ),
                
                spacing="7",  # Espaciado general entre las columnas
                justify="space-between",  # Distribución equitativa de espacio entre las columnas
                align="center",  # Alineación centrada entre las columnas
            ),
            
            # Fondo y padding de la página
            bg="#36f750.",  #color verde 
            padding="2rem",
            min_height="100vh",  # Asegura que la página ocupe toda la altura de la pantalla
        ),
    )


# Crear la aplicación
app = rx.App()
app.add_page(index)