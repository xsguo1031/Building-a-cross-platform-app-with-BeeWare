"""
first GUI app using Beeware 
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import httpx
import asyncio
import numpy as np 


# class ChelseaGuo(toga.App):
#     def startup(self):
#         """Construct and show the Toga application.

#         Usually, you would add your application to a main content box.
#         We then create a main window (with a name matching the app), and
#         show the main window.
#         """
#         main_box = toga.Box()

#         self.main_window = toga.MainWindow(title=self.formal_name)
#         self.main_window.content = main_box
#         self.main_window.show()

def greeting(name): 
        if name: 
            return f"Hello, {name}" 
        else:
            return "Hello, stranger"

class ChelseaGuo(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "Your name: ",
            style=Pack(margin=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, margin=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            style=Pack(margin=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget, **kwargs):
        print(f"Hello, {self.name_input.value}")


    # async def say_hello(self, widget, **kwargs):
    #     await self.dialog(toga.InfoDialog(
    #         greeting(self.name_input.value),
    #         "Hi there!", 
    #         ))

    value = np.random.randint(0, 100, size=10)
    async def say_hello(self, widget, **kwargs):
        await self.dialog(toga.InfoDialog(
            greeting(str(self.value)),
            "Hi there!", 
            ))

    # third-party package
    # async def say_hello(self, widget):
    #     with httpx.Client() as client:
    #         response = client.get(
    #             "https://jsonplaceholder.typicode.com/posts/42")
    #     payload = response.json()
    #     time.sleep(5) # wait for 5 seconds (simulate a long-runnning task --> solution: multi-threading (use one thread to do the long-running tasks, and let other tasks runn in the meantime))
    #     await self.dialog(toga.InfoDialog(
    #     greeting(self.name_input.value),
    #     payload["body"],
    #     ))

    # async def say_hello(self, widget):
    #     async with httpx.AsyncClient() as client:
    #         response = await client.get("https://jsonplaceholder.typicode.com/posts/42")
    #         payload = response.json()
    #         await asyncio.sleep(5) # wait for 5 seconds but GUI is still doing other things--> resolve the issue of blocking the GUI
    #         await self.dialog(toga.InfoDialog(
    #             greeting(self.name_input.value),
    #             payload["body"],
    #             ))
        
def main():
    return ChelseaGuo()
