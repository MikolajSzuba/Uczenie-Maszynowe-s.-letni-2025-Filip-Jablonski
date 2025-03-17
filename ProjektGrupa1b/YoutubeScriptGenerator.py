from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class YouTubeScriptGeneratorApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        layout_input = GridLayout(cols=2, size_hint_y=None, height=250)

        layout_input.add_widget(Label(text="Enter the topic of your YouTube video:"))
        self.topic_input = TextInput(hint_text="Topic", size_hint_y=None, height=30)
        layout_input.add_widget(self.topic_input)

        layout_input.add_widget(Label(text="Select the genre of the video:"))
        self.genre_spinner = Spinner(
            text="Educational", values=("Educational", "Humorous", "Dramatic", "Motivational", "Vlog", "Tutorial"),
            size_hint_y=None, height=30
        )
        layout_input.add_widget(self.genre_spinner)

        layout_input.add_widget(Label(text="Select the length of the video (minutes):"))
        self.length_spinner = Spinner(
            text="10", values=("5", "10", "15", "20"),
            size_hint_y=None, height=30
        )
        layout_input.add_widget(self.length_spinner)

        layout_input.add_widget(Label(text="Select the tone of the script:"))
        self.tone_spinner = Spinner(
            text="Formal", values=("Formal", "Informal", "Serious", "Funny", "Casual"),
            size_hint_y=None, height=30
        )
        layout_input.add_widget(self.tone_spinner)

        self.generate_button = Button(text="Generate Script", size_hint_y=None, height=50)
        self.generate_button.bind(on_press=self.generate_script)

        self.output_label = Label(text="Generated Script will appear here.", size_hint_y=None, height=30)
        self.scrollable_output = ScrollView(size_hint=(1, None), height=200)
        self.scrollable_output.add_widget(self.output_label)

        self.root.add_widget(layout_input)
        self.root.add_widget(self.generate_button)
        self.root.add_widget(self.scrollable_output)

        return self.root

    def generate_script(self, instance):
        topic = self.topic_input.text
        genre = self.genre_spinner.text
        length = self.length_spinner.text
        tone = self.tone_spinner.text

        if not topic:
            self.output_label.text = "Please enter a topic for the script."
            return

        script = f"Generated Script:\n\nTopic: {topic}\nGenre: {genre}\nLength: {length} minutes\nTone: {tone}\n\n" \
                 "This is where the generated script content would go. You can implement the actual script generation logic here."

        self.output_label.text = script

if __name__ == '__main__':
    YouTubeScriptGeneratorApp().run()

