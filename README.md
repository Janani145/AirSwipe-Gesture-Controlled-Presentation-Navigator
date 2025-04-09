# AirSwipe-Gesture-Controlled-Presentation-Navigator
his project uses computer vision to recognize hand gestures for navigating slides. It is developed using Python with OpenCV, MediaPipe, and PyAutoGUI.

A webcam captures real-time video, and MediaPipe detects multiple hands and their landmarks. Each hand is assigned a unique ID for individual tracking.

The user can press keys 1 to 5 to select a specific hand for gesture recognition. This enables control in multi-user or multi-hand scenarios.

The system identifies swiping gestures based on the movement of the index and ring fingers. Moving the index finger quickly to the left triggers a "previous slide" action.

A "next slide" action is recognized when both index and ring fingers move to the right and the ring finger is raised.

It uses the change in x-coordinates of finger landmarks between frames to detect swipe direction and speed.

To avoid false triggers, gestures are only processed for the selected hand. Pressing "c" clears the selection, and "q" quits the app.

Visual feedback is provided on the webcam feed with hand IDs, wrist markers, and drawn landmarks.

The approach balances accuracy and simplicity by using only key landmarks and basic gesture logic.

This system is useful for hands-free slide control during presentations, especially when physical remotes aren't available.

It enhances user interaction with minimal hardware and is ideal for smart classrooms, virtual meetings, or stage presentations.

The code is modular and can be extended to recognize more gestures like zoom, click, or drag actions.

It also introduces the concept of gesture-based UI control, which can be expanded into virtual touchless systems.

By using efficient models and real-time processing, the system runs smoothly even on standard laptops with webcams.

Overall, the project demonstrates how AI and vision-based input can replace traditional interfaces for more natural interaction.
