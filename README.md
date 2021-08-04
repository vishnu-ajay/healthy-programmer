# Healthy Programmer
A Python program to remind a programmer to take breaks during coding.
Coders work non-stop for hours in front of the computer, leading to bad posture, dehydration and eye issues.
In order to adopt healthy practices, I designed this program to remind the user to take breaks and freshen up.
## Module Used
Used Pygame module version pygame==2.0.1 (mentioned in requirements.txt) for playing the music used for the reminders.
## Features
  ### Reminders
  - Reminder to drink 1 glass of water, every thirty minutes, starting from 9 AM.
  - Reminder to exercise the eyes, every thirty minutes, starting from 9:15 AM.
  - Reminder to exercise the body, every forty-five minutes, starting from 9:15 AM.
  - Program runs from 9AM to 5PM only
  ### Logs
  - Every action done is logged into a text file, Logs.txt, with a timestamp.
## Challenges Faced
- Some activities overlap at a given time, so all of those cases had to be fixed.
- The calculation of time-interval was tricky. There are other ways to do this, while I took an odd-even approach.
