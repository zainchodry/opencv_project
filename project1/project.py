import cv2
import face_recognition
import numpy as np


INPUT_VIDEO = "/home/enigmatix/Videos/Screencasts/project1_video.webm"
OUTPUT_VIDEO = "/home/enigmatix/Videos/Screencasts/output.webm"

FACE_MATCH_THRESHOLD = 0.55

MISSING_GRACE_SECONDS = 5.0

SCALE = 0.5

FRAME_SKIP = 1

MAX_ENCODING_BANK_SIZE = 10

ENCODING_SAMPLE_INTERVAL = 5


print("=" * 60)
print("FACE RECOGNITION SYSTEM")
print("=" * 60)

print("Opening video...")

video = cv2.VideoCapture(INPUT_VIDEO)

if not video.isOpened():

    print("ERROR: Could not open video.")

    exit()


fps = video.get(cv2.CAP_PROP_FPS)

width = int(
    video.get(cv2.CAP_PROP_FRAME_WIDTH)
)

height = int(
    video.get(cv2.CAP_PROP_FRAME_HEIGHT)
)

total_frames = int(
    video.get(cv2.CAP_PROP_FRAME_COUNT)
)


if fps <= 0:
    fps = 30


MISSING_GRACE_FRAMES = int(fps * MISSING_GRACE_SECONDS)


print()
print("Video information:")
print("FPS:", fps)
print("Width:", width)
print("Height:", height)
print("Total frames:", total_frames)
print(f"Grace period: {MISSING_GRACE_SECONDS}s = {MISSING_GRACE_FRAMES} frames")
print()

fourcc = cv2.VideoWriter_fourcc(
    *"VP80"
)

output = cv2.VideoWriter(
    OUTPUT_VIDEO,
    fourcc,
    fps,
    (width, height)
)


if not output.isOpened():

    print("ERROR: Could not create output video.")

    video.release()

    exit()

people = {}

next_person_id = 1

frame_number = 0

last_annotated_frame = None


while True:

    success, frame = video.read()

    if not success:
        break


    frame_number += 1


    if frame_number % FRAME_SKIP != 0:

        display_frame = (
            last_annotated_frame
            if last_annotated_frame is not None
            else frame
        )

        output.write(display_frame)

        cv2.imshow(
            "Face Recognition",
            display_frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        continue


    small_frame = cv2.resize(
        frame,
        (0, 0),
        fx=SCALE,
        fy=SCALE
    )

    rgb_frame = cv2.cvtColor(
        small_frame,
        cv2.COLOR_BGR2RGB
    )


    face_locations = face_recognition.face_locations(
        rgb_frame,
        model="hog"
    )


    face_encodings = face_recognition.face_encodings(
        rgb_frame,
        face_locations
    )


    current_person_ids = set()


    for face_encoding, face_location in zip(
        face_encodings,
        face_locations
    ):

        top, right, bottom, left = face_location


        matched_person_id = None

        best_distance = float("inf")


        for person_id, person_data in people.items():

            distances = face_recognition.face_distance(
                person_data["encodings"],
                face_encoding
            )

            person_best = float(distances.min())


            if person_best < best_distance:

                best_distance = person_best

                matched_person_id = person_id


        if (
            matched_person_id is not None
            and
            best_distance <= FACE_MATCH_THRESHOLD
        ):

            person_id = matched_person_id

        else:

            person_id = next_person_id

            next_person_id += 1


            people[person_id] = {

                "encodings": [face_encoding],

                "appearance_count": 1,

                "last_seen": frame_number,

                "left_frame": None,

                "visible": True
            }


            print(
                f"[Frame {frame_number}] "
                f"NEW PERSON: Person {person_id}"
            )



        if person_id in people:

            person = people[
                person_id
            ]


            frames_missing = (
                frame_number
                - person["last_seen"]
            )

            if person["visible"] is False:

                person[
                    "appearance_count"
                ] += 1


                frames_absent = (
                    frame_number - person["last_seen"]
                )

                seconds_absent = frames_absent / fps

                print(
                    f"[Frame {frame_number}] "
                    f"Person {person_id} "
                    f"RETURNED after {frames_absent} frames "
                    f"({seconds_absent:.1f}s) "
                    f"-> Appearance "
                    f"{person['appearance_count']}"
                )

                person["left_frame"] = None


            person[
                "last_seen"
            ] = frame_number


            person[
                "visible"
            ] = True


            if frame_number % ENCODING_SAMPLE_INTERVAL == 0:

                bank = person["encodings"]

                bank.append(face_encoding)

                if len(bank) > MAX_ENCODING_BANK_SIZE:
                    bank.pop(1) if len(bank) > 1 else bank.pop(0)

                person["encodings"] = bank


        current_person_ids.add(
            person_id
        )


        top = int(
            top / SCALE
        )

        right = int(
            right / SCALE
        )

        bottom = int(
            bottom / SCALE
        )

        left = int(
            left / SCALE
        )

        center_x = (left + right) // 2
        center_y = (top + bottom) // 2

        radius = max(
            (right - left) // 2,
            (bottom - top) // 2
        )

        radius = int(radius * 1.15)

        cv2.circle(
            frame,
            (center_x, center_y),
            radius + 4,
            (0, 180, 0),
            1
        )

        cv2.circle(
            frame,
            (center_x, center_y),
            radius,
            (0, 255, 0),
            2
        )

        cv2.circle(
            frame,
            (center_x, center_y),
            3,
            (0, 255, 0),
            -1
        )


        appearance = people[
            person_id
        ][
            "appearance_count"
        ]


        label = (
            f"Person {person_id} "
            f"| Appearance {appearance}"
        )


        label_x = max(center_x - radius, 5)
        label_y = max(center_y - radius - 12, 25)


        (text_w, text_h), baseline = cv2.getTextSize(
            label,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            2
        )

        cv2.rectangle(
            frame,
            (label_x - 2, label_y - text_h - 4),
            (label_x + text_w + 2, label_y + baseline),
            (0, 0, 0),
            -1
        )


        cv2.putText(
            frame,

            label,

            (label_x, label_y),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.55,

            (0, 255, 0),

            2
        )

    for person_id, person in people.items():

        if person_id not in current_person_ids:

            frames_missing = (
                frame_number
                - person["last_seen"]
            )


            if frames_missing <= MISSING_GRACE_FRAMES:

                pass


            else:

                if person["visible"] is True:
                    person["left_frame"] = frame_number

                person["visible"] = False


    visible_count = len(
        current_person_ids
    )

    total_people = len(
        people
    )

    total_appearances = sum(
        person["appearance_count"]
        for person in people.values()
    )

    cv2.rectangle(
        frame,

        (10, 10),

        (380, 140),

        (0, 0, 0),

        -1
    )


    cv2.putText(
        frame,

        f"Faces Visible: {visible_count}",

        (20, 40),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.65,

        (0, 255, 255),

        2
    )


    cv2.putText(
        frame,

        f"Unique People: {total_people}",

        (20, 70),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.65,

        (0, 255, 255),

        2
    )


    cv2.putText(
        frame,

        f"Appearances: {total_appearances}",

        (20, 100),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.65,

        (0, 255, 255),

        2
    )


    cv2.putText(
        frame,

        f"Frame: {frame_number}",

        (20, 130),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.55,

        (255, 255, 255),

        2
    )


    last_annotated_frame = frame.copy()

    cv2.imshow(
        "Face Recognition",
        frame
    )

    output.write(
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):

        print("Stopped by user.")

        break

video.release()

output.release()

cv2.destroyAllWindows()

print()
print("=" * 60)
print("FINAL FACE APPEARANCE REPORT")
print("=" * 60)


for person_id in sorted(people):

    count = people[
        person_id
    ][
        "appearance_count"
    ]


    print(
        f"Person {person_id}: "
        f"{count} appearances"
    )


print("=" * 60)


print(
    f"Total unique people: "
    f"{len(people)}"
)


print(
    f"Total appearances: "
    f"{sum(person['appearance_count'] for person in people.values())}"
)


print(
    f"Output video: "
    f"{OUTPUT_VIDEO}"
)


print("=" * 60)