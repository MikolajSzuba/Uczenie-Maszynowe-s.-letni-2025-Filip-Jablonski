from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.modalview import ModalView
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import re
import api


class ApiSettingsPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "API Settings"
        self.size_hint = (None, None)
        self.size = (400, 200)
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        self.text_input = TextInput(hint_text="API key")
        confirm_button = Button(text="Save API Key", size_hint=(1, 0.3))
        confirm_button.bind(on_press=self.dismiss)
        confirm_button.bind(on_press=self.save_api_key)

        layout.add_widget(self.text_input)
        layout.add_widget(confirm_button)

        self.content = layout

    def save_api_key(self, instance):
        api_key = self.text_input.text.strip()
        if api_key:
            api.save_api_key_to_file(api_key)
        self.dismiss()

def save_script_to_file(script, filename="youtube_script.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(script)
        return True
    except Exception:
        return False

def format_script(text):
    formatted_text = ""
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        line = line.replace('*', '')  # Usuwa pojedyncze gwiazdki
        if re.match(r'^##+\s*(.*)', line):
            header_text = re.sub(r'^##+\s*', '', line)  # Nagłówki ##
            formatted_text += f"\n[b]{header_text}[/b]\n"
        elif line.startswith("(") and line.endswith(")"):  # Kursywa dla wskazówek wizualnych
            formatted_text += f"\n[i]{line}[/i]\n"
        else:
            formatted_text += f"{line}\n"
    return formatted_text

def remove_formatting(text):
    text = re.sub(r'\[i\](.*?)\[/i\]', r'\1', text)
    text = re.sub(r'\[b\](.*?)\[/b\]', r'\1', text)
    return text

class YouTubeScriptGeneratorApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=15, spacing=15)
        title_label = Label(text="[b][size=30]ScriptGenerator[/size][/b]", markup=True)
        self.root.add_widget(title_label)

        layout_input = GridLayout(cols=2, size_hint_y=None, height=500, spacing=10)
        label_size = {'size_hint_x': None, 'width': 200, 'text_size': (200, 70)}

        # Settings
        menu_layout = BoxLayout(size_hint_y=None, height=50, padding=10)
        self.menu = Spinner(
            text="Settings",
            values=["Set API Key"],
            size_hint=(None, None),
            size=(150, 40)
        )
        self.menu.bind(text=self.menu_selected)
        menu_layout.add_widget(self.menu)
        layout_input.add_widget(menu_layout)

        layout_input.add_widget(Label(text="Video Topic:", font_size=18, **label_size))
        self.topic_input = TextInput(hint_text="Enter topic", size_hint_y=None, height=40)
        layout_input.add_widget(self.topic_input)

        layout_input.add_widget(Label(text="Genre:", font_size=18, **label_size))
        self.genre_spinner = Spinner(text="Educational", values=("Educational", "Humorous", "Dramatic", "Motivational", "Vlog", "Tutorial"), size_hint_y=None, height=40)
        layout_input.add_widget(self.genre_spinner)

        layout_input.add_widget(Label(text="Video Length (min):", font_size=18, **label_size))
        length_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.length_slider = Slider(min=1, max=30, value=10, step=1)
        self.length_label = Label(text="10 min", size_hint_x=None, width=60, font_size=18)
        length_layout.add_widget(self.length_slider)
        length_layout.add_widget(self.length_label)
        layout_input.add_widget(length_layout)
        self.length_slider.bind(value=self.update_length_label)

        layout_input.add_widget(Label(text="Tone:", font_size=18, **label_size))
        self.tone_spinner = Spinner(text="Formal", values=("Formal", "Informal", "Serious", "Funny", "Casual"), size_hint_y=None, height=40)
        layout_input.add_widget(self.tone_spinner)

        layout_input.add_widget(Label(text="Target Audience:\n", font_size=18, **label_size))
        self.target_spinner = Spinner(text="General", values=("General", "Teens", "Adults", "Kids", "Seniors"), size_hint_y=None, height=40)
        layout_input.add_widget(self.target_spinner)

        self.editing_tips_checkbox = CheckBox()
        layout_input.add_widget(Label(text="Include Editing Tips\n", font_size=18, **label_size))
        layout_input.add_widget(self.editing_tips_checkbox)

        self.generate_button = Button(text="Generate Script", size_hint_y=None, height=50)
        self.generate_button.bind(on_press=self.generate_script)
        self.root.add_widget(layout_input)
        self.root.add_widget(self.generate_button)

        return self.root

    def menu_selected(self, spinner, text):
        if text == "Set API Key":
            popup = ApiSettingsPopup()
            popup.open()
            spinner.text = "Settings"

    def update_length_label(self, instance, value):
        self.length_label.text = f"{int(value)} min"

    def generate_script(self, instance):
        api_key = api.read_credentials("credentials.txt")

        # Validate the API key length.
        if len(api_key) != 39:
            self.show_popup("Error", "API key must be exactly 39 characters long.")
            return

        topic = self.topic_input.text.strip()
        if not topic:
            self.show_popup("Error", "Please enter a topic.")
            return

        self.generate_button.text = "Generating..."
        self.generate_button.disabled = True
        Clock.schedule_once(lambda dt: self.process_script_generation(api_key, topic), 1)

    def process_script_generation(self, api_key, topic):
        prompt = f"Generate a {self.genre_spinner.text.lower()} YouTube video script about {topic}. "
        prompt += f"The video should be {int(self.length_slider.value)} minutes long, with a {self.tone_spinner.text.lower()} tone. "
        prompt += f"The target audience is {self.target_spinner.text.lower()}. "
        if self.editing_tips_checkbox.active:
            prompt += "Include video editing tips."

        try:
            script = api.send_prompt(api_key, prompt)
            formatted_script = format_script(script.text)
            self.show_popup("Generated Script", formatted_script, save_button=True)
        except Exception as e:
            self.show_popup("Error", f"Error generating script: {str(e)}")
        finally:
            self.generate_button.text = "Generate Script"
            self.generate_button.disabled = False

    def show_popup(self, title, message, save_button=False):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_scroll = ScrollView(size_hint=(1, 1))
        popup_label = Label(text=message, markup=True, size_hint_y=None, text_size=(400, None))
        popup_label.bind(texture_size=popup_label.setter('size'))
        popup_scroll.add_widget(popup_label)

        close_button = Button(text="Close", size_hint_y=None, height=50)
        popup_layout.add_widget(popup_scroll)
        if save_button:
            save_button_widget = Button(text="Save to File", size_hint_y=None, height=50)
            save_button_widget.bind(on_press=lambda x: self.handle_save(message))
            popup_layout.add_widget(save_button_widget)
        popup_layout.add_widget(close_button)

        popup = ModalView(size_hint=(None, None), size=(450, 500))
        popup.add_widget(popup_layout)
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def handle_save(self, message):
        # Remove formatting before saving.
        plain_text = remove_formatting(message)
        if save_script_to_file(plain_text):
            self.show_popup("Success", "[color=00FF00]Script saved successfully!")
        else:
            self.show_popup("Error", "Failed to save the script.")

if __name__ == '__main__':
    YouTubeScriptGeneratorApp().run()