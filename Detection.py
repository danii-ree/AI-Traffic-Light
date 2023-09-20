import cv2

# Load the cascade classifiers for detecting pedestrians and cars
pedestrian_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
car_cascade = cv2.CascadeClassifier('haarcascade_cars.xml')

# Create lists to store trackers for pedestrians and cars
pedestrian_trackers = []
car_trackers = []

# Open a video capture object to read from the 'cars.mp4' video file
cap = cv2.VideoCapture(0)

# Initialize counters for pedestrians and cars
pedestrian_count = 0
car_count = 0

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect pedestrians and cars in the current frame
    pedestrians = pedestrian_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # Reset the counts if no pedestrians are detected
    if len(pedestrians) == 0:
        pedestrian_trackers = []
        pedestrian_count = 0

    # Reset the counts if no cars are detected
    if len(cars) == 0:
        car_trackers = []
        car_count = 0

    # Create lists to store pedestrians and cars that are currently being tracked
    pedestrians_being_tracked = []
    cars_being_tracked = []

    for (x, y, w, h) in pedestrians:
        pedestrian_center = (x + w // 2, y + h // 2)

        # Check if this pedestrian is already being tracked
        pedestrian_tracked = False
        for tracker in pedestrian_trackers:
            track_success, pedestrian_position = tracker.update(img)
            if track_success:
                pedestrian_position_center = (
                    int(pedestrian_position[0] + pedestrian_position[2] / 2),
                    int(pedestrian_position[1] + pedestrian_position[3] / 2)
                )
                distance = abs(pedestrian_center[0] - pedestrian_position_center[0]) + abs(
                    pedestrian_center[1] - pedestrian_position_center[1])

                if distance < 30:
                    pedestrian_tracked = True
                    break

        if not pedestrian_tracked:
            # Create a new tracker for this pedestrian
            tracker = cv2.TrackerCSRT_create()
            tracker.init(img, (x, y, w, h))
            pedestrian_trackers.append(tracker)
        else:
            pedestrians_being_tracked.append((x, y, w, h))

    # Remove trackers for pedestrians that have left the frame
    pedestrian_trackers = [tracker for tracker in pedestrian_trackers if tracker.update(img)[0]]

    # Update the pedestrian count based on the number of pedestrians being tracked
    pedestrian_count = len(pedestrian_trackers)

    for (x, y, w, h) in cars:
        car_center = (x + w // 2, y + h // 2)

        # Check if this car is already being tracked
        car_tracked = False
        for tracker in car_trackers:
            track_success, car_position = tracker.update(img)
            if track_success:
                car_position_center = (
                    int(car_position[0] + car_position[2] / 2),
                    int(car_position[1] + car_position[3] / 2)
                )
                distance = abs(car_center[0] - car_position_center[0]) + abs(car_center[1] - car_position_center[1])

                if distance < 30:
                    car_tracked = True
                    break

        if not car_tracked:
            # Create a new tracker for this car
            tracker = cv2.TrackerCSRT_create()
            tracker.init(img, (x, y, w, h))
            car_trackers.append(tracker)
        else:
            cars_being_tracked.append((x, y, w, h))

    # Remove trackers for cars that have left the frame
    car_trackers = [tracker for tracker in car_trackers if tracker.update(img)[0]]

    # Update the car count based on the number of cars being tracked
    car_count = len(car_trackers)

    # Draw rectangles around pedestrians and cars being tracked
    for (x, y, w, h) in pedestrians_being_tracked:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    for (x, y, w, h) in cars_being_tracked:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the pedestrian and car counts on the image
    cv2.putText(img, f'Pedestrian Count: {pedestrian_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(img, f'Car Count: {car_count}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
