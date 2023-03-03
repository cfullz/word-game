import arcade
import arcade.gui as gui
import random

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Word Game"





class MainMenu(arcade.View):
    def __init__(self):
        super().__init__()

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))


        # Again, method 1. Use a child class to handle events.
        quit_button = arcade.gui.UIFlatButton(text="Tutorial", width=200)
        self.v_box.add(quit_button.with_space_around(top=20))

        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start

        # --- Method 3 for handling click events,
        # use a decorator to handle on_click events
            

        @quit_button.event("on_click")
        def on_click_settings(event):
            print("Tutorial:", event)
            tutorial_view = TutorialView()
            self.window.show_view(tutorial_view)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self, event):
        print("Start:", event)
        game_view = GameView()
        self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()

class TutorialView(arcade.View):
    
    def __init__(self):
        super().__init__()
        self.v_box = arcade.gui.UIBoxLayout()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.ui_manager = arcade.gui.UIManager(self.window)
        start_button = arcade.gui.UIFlatButton(text="Main Menu", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                child=self.v_box)
        )
        start_button.on_click = self.on_click_start

        @start_button.event("on_click")
        def on_click_settings(event):
            print("Tutorial:", event)
            main_menu = MainMenu()
            self.window.show_view(main_menu)

    def on_draw(self):
        self.clear()

        # This draws our UI elements
        self.ui_manager.draw()
        arcade.draw_text("Tutorial",
                         start_x=0, start_y=self.window.height - 55,
                         width=self.window.width,
                         font_size=40,
                         align="center",
                         color=arcade.color.BLACK)
        arcade.draw_text("Start by choosing one of three difficulties. For easy, you must type words over 4 letters, for medium it's 7 letters, and for hard the words must have at least 10 letters each.",  start_x=0, start_y=self.window.height - 100,
                         width=self.window.width,
                         font_size=20,
                         align="center",
                         color=arcade.color.BLACK)
        arcade.draw_text("After choosing a difficulty, start typing words! You may have to click the word bar once before it starts registering your typing. Be careful! You only have 60 seconds to enter as many words as you can think of!",  start_x=0, start_y=self.window.height - 250,
                         width=self.window.width,
                         font_size=20,
                         align="center",
                         color=arcade.color.BLACK)
        arcade.draw_text("You will only gain points if the word actually exists. You can't fool us! Your score is displayed above the entry bar and is saved at the end of the round. You can see the leaderboard by navigating to the leaderboard tab from the main menu.",  start_x=0, start_y=self.window.height - 400,
                         width=self.window.width,
                         font_size=20,
                         align="center",
                         color=arcade.color.BLACK)
        arcade.draw_text("Just a simple game to help grow your vocabulary! Enjoy!",  start_x=0, start_y=self.window.height - 550,
                         width=self.window.width,
                         font_size=20,
                         align="center",
                         color=arcade.color.BLACK)
        self.manager.draw()

    def on_click_start(self, event):
        print("Start:", event)

class GameOver(arcade.View):
    
    def __init__(self):
        super().__init__()
        self.v_box = arcade.gui.UIBoxLayout()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.ui_manager = arcade.gui.UIManager(self.window)
        start_button = arcade.gui.UIFlatButton(text="Main Menu", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                child=self.v_box)
        )
        start_button.on_click = self.on_click_start

        @start_button.event("on_click")
        def on_click_settings(event):
            print("Tutorial:", event)
            main_menu = MainMenu()
            self.window.show_view(main_menu)

    def on_draw(self):
        self.clear()

        # This draws our UI elements
        self.ui_manager.draw()
        arcade.draw_text("Game Over.",
                         start_x=0, start_y=self.window.height - 55,
                         width=self.window.width,
                         font_size=70,
                         align="center",
                         color=arcade.color.BLACK)
        arcade.draw_text("Your score has been saved.",
                         start_x=0, start_y=self.window.height - 300,
                         width=self.window.width,
                         font_size=55,
                         align="center",
                         color=arcade.color.BLACK)
        self.manager.draw()

    def on_click_start(self, event):
        print("Start:", event)
        
        


class GameView(arcade.View):
    def __init__(self):
        
        super().__init__()
        self.manager = gui.UIManager()
        self.manager.enable()

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        # Keep track of the score
        self.score = 0

        arcade.set_background_color(arcade.color.BEIGE)
        
        # Create a text label
        self.label = arcade.gui.UILabel(
            text="",
            text_color=arcade.color.DARK_RED,
            width=350,
            height=40,
            font_size=19,
            font_name="Kenney Future",
            align="center")

        # Create an text input field
        self.input_field = gui.UIInputText(
          color=arcade.color.DARK_BLUE_GRAY,
          font_size=19,
          width=200,
          )

        # Create the score text

        self.scoreText = arcade.gui.UILabel(
            text="",
            text_color=arcade.color.DARK_RED,
            width=350,
            height=40,
            font_size=19,
            font_name="Kenney Future",
            align="center"
        )

        # Create a button
        submit_button = gui.UIFlatButton(
          color=arcade.color.DARK_BLUE_GRAY,
          text='Submit')
        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        submit_button.on_click = self.on_click 
        
        self.v_box = gui.UIBoxLayout()
        self.v_box.add(self.scoreText)
        self.v_box.add(self.label.with_space_around(bottom=0))
        self.v_box.add(self.input_field)
        self.v_box.add(submit_button)
       
        
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

        self.total_time = 10
        self.timer_text = arcade.Text(
            text="01:00:00",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT // 2 + 100,
            color=arcade.color.BLACK,
            font_size=30,
            anchor_x="center",
        )
    def setup(self):
        self.total_time = 0.0


    def update_text(self):
        
        if len(self.input_field.text) > 3:
                with open(r'WordList.txt', 'r') as file:
                # read all content from a file using read()
                    content = file.read()
                    # check if string present or not
                    if self.input_field.text in content:
                            print(f"updating the label with input text '{self.input_field.text}'")
                            self.label.text = ('Word Works!')
                            self.score += 1
                            self.scoreText.text = ("Score: " + str(self.score))
                            print(self.score)
                            self.input_field.text = ('')
                    else:
                        print(f"word not found")
                        self.label.text = ("Try again!")
                        self.input_field.text = ('')
            
        else:
            print(f"word not found end")
            self.label.text = ('no')
            self.input_field.text = ('')

    def on_update(self, delta_time):
        
        self.total_time -= delta_time

        # Calculate minutes
        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60

        # Calculate 100s of a second
        seconds_100s = int((self.total_time - seconds) * 100)

        # Use string formatting to create a new text string for our timer
        self.timer_text.text = f"{minutes:02d}:{seconds:02d}:{seconds_100s:02d}"
        

    
            
        

        

    def on_click(self, event):
        
        print(f"click-event caught: {event}")
        self.update_text()

    def on_draw(self):
        self.clear()
        
        arcade.start_render()
        self.manager.draw()
        # Activate the GUI camera before drawing GUI elements
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18)
        self.timer_text.draw()

        if self.total_time <= 0.0:
            f = open("ScoreCounter.txt", "a")
            f.write(str(self.score) + "\n")
            f.close()
            game_over = GameOver()
            self.window.show_view(game_over)
    
def main():
    """Main function"""
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MainMenu()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()