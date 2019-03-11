from guizero import App, Box, Combo, Drawing, MenuBar, Picture, PushButton, Text






app = App(title="Latency Tester for IFE", width=800,height=400, layout="auto", bg="blue")
A_A_Box = Box(app, width="fill", align="left", border=True)
Audio_Audio_Text = Text(A_A_Box, text="Audio to Audio Latency Test", align="left")
A_A_Button = PushButton(app, width=100, height=100, align="left")


V_A_Box = Box(app, width="fill", align="right", border=True)
Video_Audio_Text = Text(V_A_Box, text="Video to Audio Latency Test", align="right")


app.display()
