async def take_photo(self, widget, **kwargs):
        try:
            if not self.camera.has_permission:
                await self.camera.request_permission()

            image = await self.camera.take_photo()
            if image:
                self.photo.image = image
        except NotImplementedError:
            await self.main_window.info_dialog(
                "Oh no!",
                "The Camera API is not implemented on this platform",
            )
        except PermissionError:
            await self.main_window.info_dialog(
                "Oh no!",
                "You have not granted permission to take photos",
            )