self.photo = toga.ImageView(style=Pack(height=300, margin=5))
camera_button = toga.Button(
            "Take photo", 
            on_press=self.take_photo, 
            style=Pack(margin=5)
        )

main_box.add(self.photo)
main_box.add(camera_button)