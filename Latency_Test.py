from guizero import App, Box, Combo, Drawing, MenuBar, Picture, PushButton, Text


def Begin_AA_Test():
    print("Audio To Audio Test Started")

def Begin_VA_Test():
    print("Video To Audio Test Started")



app = App(title="Latency Tester for IFE", width=800,height=400, layout="grid", bg= (137,165,255))

#Start_Picture = Picture(app, image="Start_Button.gif", grid=[0,2], align="left")


Blank_Box_Top = Box(app, width=800, height=100, grid=[0,0], border=True)                                         # blank border that covers the top of the screen
Test_Label_Spacer = Box(app, width=300, height=100, grid=[1,1], border=True)


A_A_Box = Box(app, width=250, height=40, grid=[0,1], border=True, align="left")                                                # Text label for audio to audio test
Audio_Audio_Text = Text(A_A_Box, text="Audio to Audio Latency Test", align="left")                               # Text for Audio to Audio test
A_A_Button = PushButton(app, command=Begin_AA_Test, image="Start_Button.gif", grid=[0,2], align="left")          # Button to start audio to audio test




#Video to Audio Section
V_A_Box = Box(app, width=250, height=40, grid=[1,1], border=True, align="left")                                                # Text label for Video to Audio Test
Video_Audio_Text = Text(V_A_Box, text="Video to Audio Latency Test", align="left")
V_A_Button = PushButton(app, command=Begin_VA_Test, image="Start_Run.gif", grid=[0,2], align="right")          # Button to start audio to audio test


app.display()

#hi kevin
#hello world
