# Importing all necessary libraries
import cv2
import os
import textwrap

#txwrpr = textwrap.TextWrapper

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2
color = (255, 128, 0)
thickness = 3

def putTextWrap(img, text, pos, max_width):
    words = textwrap.wrap(text, width=max_width)
    y_offset = 0
    for word in words:
        textsize = cv2.getTextSize(word, font, fontScale, thickness)[0]
        cv2.putText(img, word, (pos[0], pos[1] + y_offset), font, fontScale, color, thickness, cv2.LINE_AA)
        y_offset += textsize[1] + 15
    return img

def putTextWrapRight(img, text, pos, max_width):
    words = textwrap.wrap(text, width=max_width)
    words = [line.rjust(max_width) for line in words]
    textsize = cv2.getTextSize(words[0], font, fontScale, thickness)[0]
    x_offset = textsize[0]
    y_offset = 0
    for word in words:
        textsize = cv2.getTextSize(word, font, fontScale, thickness)[0]
        cv2.putText(img, word, (pos[0] - x_offset, pos[1] + y_offset), font, fontScale, color, thickness, cv2.LINE_AA)
        y_offset += textsize[1] + 15
    return img

def putTextWrapCenter(img, text, pos, max_width):
    words = textwrap.wrap(text, width=max_width)
    if len(words) > 0:
        textsize = cv2.getTextSize(words[0], font, fontScale, thickness)[0]
        x_offset = int(textsize[0] / 2)
        y_offset = 0
        for word in words:
            textsize = cv2.getTextSize(word, font, fontScale, thickness)[0]
            cv2.putText(img, word, (pos[0] - x_offset, pos[1] + y_offset), font, fontScale, color, thickness, cv2.LINE_AA)
            y_offset += textsize[1] + 15
    return img

# Read the video from specified path
pic = cv2.imread("XboxDiagram.png")

year = "2025"
frcGame = "Reefscape"
competition = "CIR"
#controller = "Primary"
controller = "Secondary"
outputFolder = str(year) + frcGame + competition

try:
	
	# creating a folder named data
	if not os.path.exists(outputFolder):
		os.makedirs(outputFolder)

# if not created then raise error
except OSError:
	print('Error: Creating directory of data')

# if video is still left continue creating images
name = './' + outputFolder + '/' + controller + '1259.jpg'
print('Creating...' + name)

coordTitle = (450, 50)

coordA = (1645, 780)
coordB = (1790, 660)
coordX = (1591, 910)
coordY = (1645, 530)

coordLB    = ( 290, 310)
coordRB    = (1865, 310)
coordBack  = ( 900, 495)
coordStart = (1257, 495)

coordLT = ( 587, 123)
coordRT = (1571, 123)
coordLS = (  65, 980)
coordRS = (1560, 1330)

coordPOVUp    = ( 823,  730)
coordPOVDown  = ( 823, 1085)
coordPOVLeft  = ( 650,  885)
coordPOVRight = ( 980,  875)

coordLeftStick = (320, 623)
coordRightStick = (1340, 1225)

labelTitle = "Team 1259 " + frcGame + " " + year + " "  + controller

if controller == "Primary":
    labelA        = "Eject + L1"
    labelB        = "Coral Prep"
    labelX        = "Climb Deploy"
    labelY        = "Cancel All"

    labelLB       = "Field Relative"
    labelRB       = "On-the-fly Path"
    labelBack     = "Climb"
    labelStart    = "Slow"

    labelLT       = "Jog Rotate CW"
    labelRT       = "Jog Rotate CCW"
    labelLS       = "N/A"
    labelRS       = "N/A"

    labelPOVUp    = "Stop All"
    labelPOVDown  = "Helmet To Intake Position"
    labelPOVLeft  = "Reset To Tag Angle"
    labelPOVRight = "Reset Load Pose"

    labelLeftStick = "Swerve Translate"
    labelRightStick = "Swerve Rotate"
else:
    labelA        = "L2"
    labelB        = "L3"
    labelX        = "L1"
    labelY        = "L4"

    labelLB       = "Eject Post"
    labelRB       = "Score w/o Path"
    labelBack     = "ElevReset"
    labelStart    = "CoralRetract"

    labelLT       = "AlgaeL3-4"
    labelRT       = "AlgaeL2-3"
    labelLS       = "Helmet To Intake Position"
    labelRS       = "Helmet To Climb Position"

    labelPOVUp    = "Elev Jog Up"
    labelPOVDown  = "Elev Jog Down"
    labelPOVLeft  = "Coral Deploy Manip"
    labelPOVRight = "Coral Retract Manip"

    labelLeftStick = "N/A"
    labelRightStick = "N/A"

"""
color = (255, 128, 0)
pic = cv2.drawMarker(pic, coordA, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordB, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordX, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordY, color, cv2.MARKER_CROSS, 30, 2)

color = (255, 0, 0)
pic = cv2.drawMarker(pic, coordLB, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordRB, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordBack, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordStart, color, cv2.MARKER_CROSS, 30, 2)

color = (255, 0, 128)
pic = cv2.drawMarker(pic, coordLT, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordRT, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordLS, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordRS, color, cv2.MARKER_CROSS, 30, 2)

color = (0, 128, 255)
pic = cv2.drawMarker(pic, coordPOVUp, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordPOVDown, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordPOVLeft, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordPOVRight, color, cv2.MARKER_CROSS, 30, 2)

color = (0, 0, 0)
pic = cv2.drawMarker(pic, coordLeftStick, color, cv2.MARKER_CROSS, 30, 2)
pic = cv2.drawMarker(pic, coordRightStick, color, cv2.MARKER_CROSS, 30, 2)

"""

color = (0, 0, 0)
pic = putTextWrap(pic, labelTitle		, coordTitle, 150)

color = (255, 128, 0)
pic = putTextWrap(pic, labelA		, coordA, 30)
pic = putTextWrap(pic, labelB		, coordB, 30)
pic = putTextWrap(pic, labelX		, coordX, 30)
pic = putTextWrap(pic, labelY		, coordY, 30)

pic = putTextWrapCenter(pic, labelLB		, coordLB, 30)
pic = putTextWrapCenter(pic, labelRB		, coordRB, 30)
pic = putTextWrapCenter(pic, labelBack		, coordBack, 30)
pic = putTextWrapCenter(pic, labelStart	, coordStart, 30)

pic = putTextWrapCenter(pic, labelLT		, coordLT, 30)
pic = putTextWrapCenter(pic, labelRT		, coordRT, 30)

if controller == "Primary":
    pic = putTextWrap(pic, labelLS		, coordLS, 30)
    pic = putTextWrap(pic, labelRS		, coordRS, 30)
else:
    pic = putTextWrap(pic, labelLS		, coordLS, 12)
    pic = putTextWrap(pic, labelRS		, coordRS, 12)

pic = putTextWrapCenter(pic, labelPOVUp	, coordPOVUp, 10)
pic = putTextWrapCenter(pic, labelPOVDown	, coordPOVDown, 10)
pic = putTextWrapRight(pic, labelPOVLeft	, coordPOVLeft, 10)
pic = putTextWrap(pic, labelPOVRight, coordPOVRight, 8)

pic = putTextWrapRight(pic, labelLeftStick, coordLeftStick, 10)
pic = putTextWrapCenter(pic, labelRightStick, coordRightStick, 10)

















# writing the extracted images
cv2.imwrite(name, pic)

# Release all space and windows once done
cv2.destroyAllWindows()
