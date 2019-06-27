from psychopy import visual,monitors,event
from psychopy.hardware.minolta import LS100
import numpy as np

photometer = LS100('/dev/tty.usbmodem14601') # set to port


automatic_measure = 0 # set to 1 if you want to take automated measures
n_luminance_levels = 20 # number of samples per color gun manipulation

file_name = raw_input('file name? ')


screen_size = (1920.,1080.) # screen size in pixels
mon = monitors.Monitor('BOLD_display', width=79.7,
                       distance=138) # width and distance in cm
mon.setSizePix(screen_size)
mon.saveMon()

win = visual.Window(screen_size, allowGUI=False, units='pix', monitor=mon, screen=0, fullscr=True)


bw_lum_measurements = []
red_lum_measurements = []
green_lum_measurements = []
blue_lum_measurements = []

default_start_lum = -1.1

lum = default_start_lum
patch = visual.GratingStim(win, tex="sin",texRes=256,
          size=[4000.0,4000.0], sf=[0,0], ori=0, units='pix', color=(lum,lum,lum), colorSpace='rgb')


check_center = visual.TextStim(win, pos=[0,0], text="+") # present a fixation cross to center the photoneter fov

check_center.draw()
win.flip()
event.waitKeys() # wait for a keypress to begin the sequence
win.flip()

# increase the intensity of all color guns
for n_trials in range(n_samples):

    lum += 0.1
    patch.setColor([lum,lum,lum])
    patch.draw()
    win.flip()

    if automatic_measure == 1:
        lum_measure = photometer.getLum()
        bw_lum_measurements.append(lum_measure)
    else:
        event.waitKeys()
        allKeys = event.getKeys()
        for thisKey in allKeys:
            if thisKey in ['q', 'escape']:
                win.close()
                core.quit()

print 'bw luminance measurements (cd/m2)', bw_lum_measurements


# increase the intensity of the red color gun

lum = default_start_lum
for n_trials in range(n_samples):

    lum += 0.1
    patch.setColor([lum,-1,-1])
    patch.draw()
    win.flip()

    if automatic_measure == 1:
        lum_measure = photometer.getLum()
        red_lum_measurements.append(lum_measure)
    else:
        event.waitKeys()
        allKeys=event.getKeys()
        for thisKey in allKeys:
            if thisKey in ['q', 'escape']:
                win.close()
                core.quit()

print 'red luminance measurements (cd/m2)', red_lum_measurements


# increase the intensity of the green color gun

lum = default_start_lum

for n_trials in range (n_samples):

    lum += 0.1
    patch.setColor([-1,lum,-1])
    patch.draw()
    win.flip()

    if automatic_measure == 1:
        lum_measure= photometer.getLum()
        green_lum_measurements.append(lum_measure)
    else:
        event.waitKeys()
        allKeys=event.getKeys()
        for thisKey in allKeys:
            if thisKey in ['q', 'escape']:
                win.close()
                core.quit()
print 'green luminance measurements (cd/m2)', green_lum_measurements


# increase the intensity of the blue color gun

lum = default_start_lum

for n_trials in range (n_samples):
    lum += 0.1
    patch.setColor([-1,-1,lum])
    patch.draw()
    win.flip()
    if automatic_measure == 1:
        lum_measure= photometer.getLum()
        blue_lum_measurements.append(lum_measure)#add the luminance measure to the list to print at the end
    else:
        event.waitKeys()
        allKeys=event.getKeys()
        for thisKey in allKeys:
            if thisKey in ['q', 'escape']:
                win.close()
                core.quit()
print 'blue luminance measurements (cd/m2)', blue_lum_measurements

# save the datumz

header = ('bw_lum, blue_lum, red_lum, green_lum')
data = np.column_stack((bw_lum_measurements, blue_lum_measurements,
 red_lum_measurements, green_lum_measurements))
np.savetxt(file_name + '.csv', data, header=header, delimiter=',',comments='')
