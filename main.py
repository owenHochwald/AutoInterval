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


def get_starting_pitch() -> str:
    pitch = input("Enter a pitch: ")
    for group in pitches:
        if pitch in group:
            return pitch, group
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


def calculate_interval(starting_pitch, pitches, interval_distance, direction) -> str:
    starting_pitch_index = pitches.index(starting_pitch)
    interval_distance_increment = intervals[interval_distance]
    num_pitches = len(pitches)

    if direction == "up":
        second_pitch_index = starting_pitch_index + interval_distance_increment
        while second_pitch_index >= num_pitches:
            second_pitch_index -= num_pitches
    else:
        second_pitch_index = starting_pitch_index - interval_distance_increment
        while second_pitch_index < 0:
            second_pitch_index += num_pitches

    second_pitch = pitches[second_pitch_index]

    return f"Starting on {starting_pitch} and going {direction} a {interval_distance} gives you {second_pitch}"


if __name__ == '__main__':
    starting_pitch, pitches = get_starting_pitch()
    interval_distance = get_interval_distance()
    direction = get_direction()
    print(calculate_interval(starting_pitch, pitches, interval_distance, direction))