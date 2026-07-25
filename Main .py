from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class AssistantUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.output_label = Label(
            text="Tech Assistant Initialized.",
            size_hint_y=None
        )
        self.output_label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))

        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.scroll.add_widget(self.output_label)
        self.add_widget(self.scroll)

        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=5)
        self.user_input = TextInput(hint_text="Enter message...", multiline=False)
        send_btn = Button(text="Send", size_hint_x=0.3)
        send_btn.bind(on_press=self.process_input)

        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        self.add_widget(input_layout)

    def process_input(self, instance):
        query = self.user_input.text.strip()
        if query:
            self.output_label.text += f"\n\nYou: {query}\nAI: Processing..."
            self.user_input.text = ""

class AssistantApp(App):
    def build(self):
        return AssistantUI()

if __name__ == "__main__":
    AssistantApp().run()
