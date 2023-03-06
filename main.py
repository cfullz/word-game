import arcade
import arcade.gui as gui
import random
import os

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Word Game"


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class MainMenu(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = None
        self.background = arcade.load_texture("FBLA_SLC_Computer_Game_Presentation.png")
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
        tutorial_button = arcade.gui.UIFlatButton(text="Tutorial", width=200)
        self.v_box.add(tutorial_button.with_space_around(bottom=20))

        leaderboard_button = arcade.gui.UIFlatButton(text="Leaderboard", width=200)
        self.v_box.add(leaderboard_button.with_space_around(bottom=20))

        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=20))


        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start

        # --- Method 3 for handling click events,
        # use a decorator to handle on_click events
            

        @tutorial_button.event("on_click")
        def on_click_settings(event):
            print("Tutorial:", event)
            tutorial_view = TutorialView()
            self.window.show_view(tutorial_view)

        @leaderboard_button.event("on_click")
        def on_click_settings(event):
            print("Leaderboard:", event)
            leaderboard_view = Leaderboard()
            self.window.show_view(leaderboard_view)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                child=self.v_box)
        )

    def on_key_press(self, symbol, modifier):
        if symbol == arcade.key.ESCAPE:
            arcade.exit()

    def on_click_start(self, event):
        print("Start:", event)
        choice = DifficultyChoice2()
        self.window.show_view(choice)
    # Draw background image and buttons on start screen
    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.manager.draw()

class DifficultyChoice2(arcade.View):
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
            text="Enter your name:",
            text_color=arcade.color.FALU_RED,
            width=350,
            height=40,
            font_size=19,
            font_name="Kenney Rocket Square",
            align="center")

        # Create an text input field
        self.input_field = gui.UIInputText(
          text = '',  
          color=arcade.color.DARK_BLUE_GRAY,
          font_size=19,
          width=200,
          align="center"
          )

        # Create the score text

        self.scoreText = arcade.gui.UILabel(
            text="",
            text_color=arcade.color.FALU_RED,
            width=350,
            height=40,
            font_size=19,
            font_name="Kenney Rocket Square",
            align="center"
        )

        # Create a button
        
        
        self.v_box = gui.UIBoxLayout()
        self.v_box.add(self.label.with_space_around(bottom=10))
        self.v_box.add(self.input_field.with_space_around(bottom=20))

       
        
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

        start_button = arcade.gui.UIFlatButton(text="Easy Mode (4 Letters)", width=300)
        self.v_box.add(start_button.with_space_around(bottom=20))

        medium_button = arcade.gui.UIFlatButton(text="Medium Mode (7 Letters)", width=300)
        self.v_box.add(medium_button.with_space_around(bottom=20))

        hard_button = arcade.gui.UIFlatButton(text="Hard Mode (10 Letters)", width=300)
        self.v_box.add(hard_button.with_space_around(bottom=20))


        # Again, method 1. Use a child class to handle events.
       

        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start

        # --- Method 3 for handling click events,
        # use a decorator to handle on_click events
            

        @medium_button.event("on_click")
        def on_click_settings(event):
            print("Medium:", event)
            medium_mode = MediumMode()
            self.window.show_view(medium_mode)

        @hard_button.event("on_click")
        def on_click_settings(event):
            print("Hard:", event)
            hard_mode = HardMode()
            self.window.show_view(hard_mode)

    def on_click_start(self, event):
        print("Start:", event)
        game_view = EasyMode()
        self.window.show_view(game_view)

    def on_key_press(self, symbol, modifier):
        if symbol == arcade.key.ESCAPE:
            arcade.exit()

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)
        arcade.start_render()
        self.manager.draw()
        # Activate the GUI camera before drawing GUI elements
        
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)
        
         

            



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
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)
        # This draws our UI elements
        self.ui_manager.draw()
        # Draws the instructions
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
        arcade.draw_text("After choosing a difficulty, start typing words! You may have to click the word bar once before it starts registering your typing. Be careful! You only have 60 seconds to enter as many words as you can think of!",  start_x=0, start_y=self.window.height - 225,
                         width=self.window.width,
                         font_size=20,
                         align="center",
                         color=arcade.color.BLACK)
        arcade.draw_text("You will only gain points if the word actually exists. You can't fool us! Your score is displayed above the entry bar and is saved at the end of the round. You can see the leaderboard by navigating to the leaderboard tab from the main menu.",  start_x=0, start_y=self.window.height - 375,
                         width=self.window.width,
                         font_size=20,
                         align="center",
                         color=arcade.color.BLACK)
        arcade.draw_text("Just a simple game to help grow your vocabulary! Enjoy! \n PS: Always click by the start of the input field! You risk restarting your game if you click in the wrong area!",  start_x=0, start_y=self.window.height - 500,
                         width=self.window.width,
                         font_size=20,
                         align="center",
                         color=arcade.color.BLACK)
        self.manager.draw()

    def on_key_press(self, symbol, modifier):
        if symbol == arcade.key.ESCAPE:
            arcade.exit()

    def on_click_start(self, event):
        print("Start:", event)

class Leaderboard(arcade.View):
    
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
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)
        infile = open('ScoresEasy.txt')
        contents = infile.read()
        infile.close()
    
        lines = contents.splitlines()
    
        maxEasy = lines[0]
        for line in lines:
            if line > maxEasy:
                maxEasy = line

        infile = open('ScoresMed.txt')
        contents = infile.read()
        infile.close()
    
        lines = contents.splitlines()
    
        maxMed = lines[0]
        for line in lines:
            if line > maxMed:
                maxMed = line

        infile = open('ScoresHard.txt')
        contents = infile.read()
        infile.close()
    
        lines = contents.splitlines()
    
        maxHard = lines[0]
        for line in lines:
            if line > maxHard:
                maxHard = line
              
        # This draws our UI elements
        self.ui_manager.draw()
        arcade.draw_text("Leaderboard",
                         start_x=0, start_y=self.window.height - 55,
                         width=self.window.width,
                         font_size=50,
                         align="center",
                         color=arcade.color.BLACK)
        arcade.draw_text("This page displays the top score for every difficulty. Remember, each word is 1 point.",
                         start_x=0, start_y=self.window.height - 100,
                         width=self.window.width,
                         font_size=30,
                         align="center",
                         color=arcade.color.BLACK)
        arcade.draw_text("Easy", start_x = 100, start_y=self.window.height - 300, width=self.window.width, font_size = 30, align="left", color=arcade.color.BLACK)
        arcade.draw_text(str(maxEasy), start_x = 120, start_y=self.window.height - 400, width=self.window.width, font_size = 30, align="left", color=arcade.color.BLACK)
        arcade.draw_text("Medium", start_x = 0, start_y=self.window.height - 300, width=self.window.width, font_size = 30, align="center", color=arcade.color.BLACK)
        arcade.draw_text(str(maxMed), start_x = 0, start_y=self.window.height - 400, width=self.window.width, font_size = 30, align="center", color=arcade.color.BLACK)
        arcade.draw_text("Hard", start_x = -100, start_y=self.window.height - 300, width=self.window.width, font_size = 30, align="right", color=arcade.color.BLACK)
        arcade.draw_text(str(maxHard), start_x = -120, start_y=self.window.height - 400, width=self.window.width, font_size = 30, align="right", color=arcade.color.BLACK)
        self.manager.draw()

    def on_click_start(self, event):
        print("Start:", event)

    def on_key_press(self, symbol, modifier):
        if symbol == arcade.key.ESCAPE:
            arcade.exit()

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
        # Define destination for main menu button
        @start_button.event("on_click")
        def on_click_settings(event):
            print("Tutorial:", event)
            main_menu = MainMenu()
            self.window.show_view(main_menu)

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)
        # This draws our UI elements
        self.ui_manager.draw()
        arcade.draw_text("Game Over.",
                         start_x=0, start_y=self.window.height - 100,
                         width=self.window.width,
                         font_size=60,
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
    # Quit program when ESC key is clicked
    def on_key_press(self, symbol, modifier):
        if symbol == arcade.key.ESCAPE:
            arcade.exit()

# Create scene for Easy Mode
class EasyMode(arcade.View):
    def __init__(self):
        
        super().__init__()
        
        self.manager = gui.UIManager()
        self.manager.enable()
        self.usedwords = []
        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        # Keep track of the score
        self.score = 0

        arcade.set_background_color(arcade.color.BEIGE)
        
        # Create a text label
        self.label = arcade.gui.UILabel(
            text="",
            text_color=arcade.color.FALU_RED,
            width=350,
            height=40,
            font_size=19,
            font_name="Kenney Rocket Square",
            align="center")

        # Create an text input field
        self.input_field = gui.UIInputText(
          text = '',  
          color=arcade.color.DARK_BLUE_GRAY,
          font_size=19,
          width=200,
          )

        # Create the score text

        self.scoreText = arcade.gui.UILabel(
            text="",
            text_color=arcade.color.FALU_RED,
            width=350,
            height=40,
            font_size=19,
            font_name="Kenney Rocket Square",
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

        self.total_time = 30
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
                        if self.input_field.text in self.usedwords:
                            print(f"word already used")
                            self.label.text = ("Try again!")
                            self.input_field.text = ('')
                        else:
                            print(f"updating the label with input text '{self.input_field.text}'")
                            self.label.text = ('Word Works!')
                            self.score += 1
                            self.usedwords.append(self.input_field.text)
                            self.scoreText.text = ("Score: " + str(self.score))
                            print(self.score)
                            self.input_field.text = ('')
                    else:
                        print(f"word not found")
                        self.label.text = ("Try again!")
                        self.input_field.text = ('')
            
        else:
            print(f"word not found end")
            self.label.text = ('Try again!')
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
        
        self.clear(arcade.color.COLUMBIA_BLUE)
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)
        arcade.start_render()
        self.manager.draw()
        # Activate the GUI camera before drawing GUI elements
        
        self.timer_text.draw()

        if self.total_time <= 0.0:
            f = open("ScoresEasy.txt", "a")
            f.write(str(self.score) + "\n")
            f.close()
            game_over = GameOver()
            self.window.show_view(game_over)
# Create scene for Medium mode
class MediumMode(arcade.View):
    def __init__(self):
        
        super().__init__()
        self.manager = gui.UIManager()
        self.manager.enable()
        self.usedwords = []
        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        # Keep track of the score
        self.score = 0

        arcade.set_background_color(arcade.color.BEIGE)
        
        # Create a text label
        self.label = arcade.gui.UILabel(
            text="",
            text_color=arcade.color.FALU_RED,
            width=350,
            height=40,
            font_size=19,
            font_name="Kenney Rocket Square",
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
            text_color=arcade.color.FALU_RED,
            width=350,
            height=40,
            font_size=19,
            font_name="Kenney Rocket Square",
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

        self.total_time = 30
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
                        if self.input_field.text in self.usedwords:
                            print(f"word already used")
                            self.label.text = ("Try again!")
                            self.input_field.text = ('')
                        else:
                            print(f"updating the label with input text '{self.input_field.text}'")
                            self.label.text = ('Word Works!')
                            self.score += 1
                            self.usedwords.append(self.input_field.text)
                            self.scoreText.text = ("Score: " + str(self.score))
                            print(self.score)
                            self.input_field.text = ('')
                    else:
                        print(f"word not found")
                        self.label.text = ("Try again!")
                        self.input_field.text = ('')
            
        else:
            print(f"word not found end")
            self.label.text = ('Try again!')
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
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)
        arcade.start_render()
        self.manager.draw()
        # Activate the GUI camera before drawing GUI elements
        
        self.timer_text.draw()

        if self.total_time <= 0.0:
            f = open("ScoresMed.txt", "a")
            f.write(str(self.score) + "\n")
            f.close()
            game_over = GameOver()
            self.window.show_view(game_over)
# Create scene for Hard mode
class HardMode(arcade.View):
    def __init__(self):
        
        super().__init__()
        self.manager = gui.UIManager()
        self.manager.enable()
        self.usedwords = []
        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        # Keep track of the score
        self.score = 0

        arcade.set_background_color(arcade.color.BEIGE)
        
        # Create a text label
        self.label = arcade.gui.UILabel(
            text="",
            text_color=arcade.color.FALU_RED,
            width=350,
            height=40,
            font_size=19,
            font_name="Kenney Rocket Square",
            align="center")

        # Create an text input field
        self.input_field = gui.UIInputText(
          color=arcade.color.BLACK,
          font_size=19,
          width=200,
          )

        # Create the score text

        self.scoreText = arcade.gui.UILabel(
            text="",
            text_color=arcade.color.FALU_RED,
            width=350,
            height=40,
            font_size=19,
            font_name="Kenney Rocket Square",
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

        self.total_time = 30
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
                        # check if word has been used or not
                        if self.input_field.text in self.usedwords:
                            print(f"word already used")
                            self.label.text = ("Try again!")
                            self.input_field.text = ('')
                        else:
                            print(f"updating the label with input text '{self.input_field.text}'")
                            self.label.text = ('Word Works!')
                            self.score += 1
                            self.usedwords.append(self.input_field.text)
                            self.scoreText.text = ("Score: " + str(self.score))
                            print(self.score)
                            self.input_field.text = ('')
                    else:
                        print(f"word not found")
                        self.label.text = ("Try again!")
                        self.input_field.text = ('')
            
        else:
            print(f"word not found end")
            self.label.text = ('Try again!')
            self.input_field.text = ('')

    def on_update(self, delta_time):
        # remove time from starting time
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
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)
        arcade.start_render()
        self.manager.draw()
        # Activate the GUI camera before drawing GUI elements
        
        self.timer_text.draw()

        if self.total_time <= 0.0:
            f = open("ScoresHard.txt", "a")
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