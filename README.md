### Laser Guided Robot Arm Project

pyControl(Main) file should be run in Thonny, every other file can be run on any substantial system able to run Python.
Data has to be processed in each file then manually transfered into the next file:
- Start by picking up image and use a camera calibration undistort video" library to remove fish-eye destortion
- Run corrected image through the computerVision file to get position of "laser dot"
- Take coords from computerVision file and punch them into generateJointAngles file
- Take the array from generateJointAngles file and punch it into pyControl(main) file to finally move robot arm to targeted position

