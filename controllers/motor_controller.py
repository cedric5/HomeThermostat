import time
import RPi.GPIO as GPIO

def turn(direction = 1, number_of_turns = 1, speed = 5):
    print(f'direction: {direction}, turns: {number_of_turns}, speed: {speed}')
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Define GPIO signals to use
    # Physical pins 11,15,16,18
    # GPIO17,GPIO22,GPIO23,GPIO24
    StepPins = [17, 22, 23, 24]

    # Set all pins as output
    for pin in StepPins:
        print
        "Setup pins"
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

    # Define advanced sequence
    # as shown in manufacturers datasheet
    Seq = [[1, 0, 0, 1],
           [1, 0, 0, 0],
           [1, 1, 0, 0],
           [0, 1, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 1, 1],
           [0, 0, 0, 1]]

    StepCount = len(Seq)
    StepDir = direction  # Set to 1 or 2 for clockwise
    # Set to -1 or -2 for anti-clockwise

    WaitTime = speed / float(1000)

    # Initialise variables
    StepCounter = 0
    cycleCounter = 0
    cycles = (number_of_turns * 16300)
    print(cycles)
    # Start main loop
    while cycleCounter < cycles:
        cycleCounter = cycleCounter + 1
        # print
        # Seq[StepCounter]

        for pin in range(0, 4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin] != 0:
                print
                " Enable GPIO %i" % (xpin)
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        StepCounter += StepDir

        # If we reach the end of the sequence
        # start again
        if (StepCounter >= StepCount):
            StepCounter = 0
        if (StepCounter < 0):
            StepCounter = StepCount + StepDir

        # Wait before moving on
        time.sleep(WaitTime)
    GPIO.cleanup()