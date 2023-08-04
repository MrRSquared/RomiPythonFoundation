#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on.
    It is taken from here. 
    https://robotpy.readthedocs.io/en/latest/guide/anatomy.html

"""

# I merged many aspcets of this example https://github.com/robotpy/examples/tree/main/commands-v2/romi on Github to get this running...
# The Following Header is also helpful...

# Example that shows how to connect to a ROMI from RobotPy
#
# Requirements
# ------------
#
# You must have the robotpy-halsim-ws package installed. This is best done via:
#
#    # Windows
#    py -3 -m pip install robotpy[commands2,sim]
#
#    # Linux/macOS
#    pip3 install robotpy[commands2,sim]
#
# Run the program
# ---------------
#
# To run the program you will need to explicitly use the ws-client option:
#
#    # Windows
#    py -3 robot.py sim --ws-client
#
#    # Linux/macOS
#    python robot.py sim --ws-client
#
# By default the WPILib simulation GUI will be displayed. To disable the display
# you can add the --nogui option
#

import wpilib
import wpilib.drive
# This is required for the simulator to work.
import os



class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.left_motor = wpilib.Spark(0)
        self.right_motor = wpilib.Spark(1)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        self.stick = wpilib.Joystick(1)
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.4, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())


if __name__ == "__main__":
    # These are the two lines required to connect to the Romi through Python.
    # If your ROMI isn't at the default address, set that here
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"


    wpilib.run(MyRobot)