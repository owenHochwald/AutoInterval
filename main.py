pitches = [
    ["C"],
    ["C#", "Db"],
    ["D"],
    ["D#", "Eb"],
    ["E"],
    ["F"],
    ["F#", "Gb"],
    ["G"],
    ["G#", "Ab"],
    ["A"],
    ["A#", "Bb"],
    ["B"]
]

intervals = {
    "P1": 0, "d2": 0,
    "m2": 1, "A1": 1,
    "M2": 2, "d3": 2,
    "m3": 3, "A2": 3,
    "M3": 4, "d4": 4,
    "P4": 5, "A3": 5,
    "d5": 6, "A4": 6,
    "P5": 7, "d6": 7,
    "m6": 8, "A5": 8,
    "M6": 9, "d7": 9,
    "m7": 10, "A6": 10,
    "M7": 11, "d8": 11,
    "P8": 12
}

NUM_PITCHES = 12


def get_starting_pitch() -> tuple:
    pitch = input("Enter a pitch: ")
    for group_index, group in enumerate(pitches):
        if pitch in group:
            return pitch, group_index
    else:
        print("Invalid pitch. Please enter a pitch from the list.")
        return get_starting_pitch()


def get_interval_distance() -> str:
    interval = input("Enter an interval (P1, d2, m2, M2, d3, m3, M3, d4, P4, A4, d5, P5, d6, m6, M6, d7, m7, M7, d8): ")
    if interval not in intervals:
        print("Invalid interval. Please enter an interval from the list.")
        return get_interval_distance()
    return interval


def get_direction() -> str:
    direction = input("Enter direction (up or down): ")
    if direction.lower() not in ["up", "down"]:
        print("Invalid direction. Please enter 'up' or 'down'.")
        return get_direction()
    return direction


def calculate_interval(starting_pitch, pitch_index, interval_distance, direction):
    # starting_pitch_group_index = pitches.index(starting_pitch)
    interval_distance_increment = intervals.get(interval_distance)

    if direction == "up":
        second_pitch_group_index = (pitch_index + interval_distance_increment) % NUM_PITCHES
    else:
        second_pitch_group_index = (pitch_index - interval_distance_increment) % NUM_PITCHES

    second_pitch = pitches[second_pitch_group_index]
    if len(second_pitch) > 0:
        return f"Starting on {starting_pitch} and going {direction} a {interval_distance} gives you {second_pitch[0]}, which is a change of {interval_distance_increment} half-step/s."
    else:
        return f"Starting on {starting_pitch} and going {direction} a {interval_distance} gives you {second_pitch[0]} / {second_pitch[1]}, which is a change of {interval_distance_increment} half-step/s."

if __name__ == '__main__':
    starting_pitch, pitch_index = get_starting_pitch()
    interval_distance = get_interval_distance()
    direction = get_direction()
    print(calculate_interval(starting_pitch, pitch_index, interval_distance, direction))