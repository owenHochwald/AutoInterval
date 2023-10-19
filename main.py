pitches = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
# for intervals bigger than an octave -> to some math to to the index to get the similar pitch
intervals = [
    "P1", "d2", "m2", "A1", "M2", "d3", "m3", "A2", "M3", "d4",
    "P4", "A3", "d5", "A4", "P5", "d6", "m6", "A5", "M6", "d7",
    "m7", "A6", "M7", "d8", "P8", "A7"
]
def get_starting_pitch(P) -> str:
    # validate input against list
    return input("Enter a pitch: ")
def get_interval_pitch() -> str:
    # validate input against list
    return input("Enter an interval: ")

def get_direction() -> str:
    direction = input("Enter direction (up or down): ")
    if direction.lower() not in ["up", "down"]:
        print("Invalid direction. Please enter 'up' or 'down'.")
        return get_direction()
    return direction

def calculate_interval(starting_pitch, interval_pitch, direction):
    starting_pitch_index = pitches.index(starting_pitch)
    interval_pitch_index = intervals.index(interval_pitch)
    if direction == "up":
        return pitches[(starting_pitch_index + interval_pitch_index) % 12]
    else:
        return pitches[(starting_pitch_index - interval_pitch_index) % 12]

if __name__ == '__main__':
    starting_pitch = get_starting_pitch()
    interval_pitch = get_interval_pitch()
    direction = get_direction()
    print(calculate_interval(starting_pitch, interval_pitch, direction))