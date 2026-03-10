def dompier_music(switches):

    notes = {
        261: "C4",
        294: "D4",
        329: "E4",
        349: "F4",
        392: "G4",
        440: "A4",
        494: "B4",
        523: "C5",
        0: "REST"
    }

    result = []

    for binary in switches:
        decimal = int(binary, 2)
        result.append(notes[decimal])



    return result
switches = ["0100000101", "0100000101", "0110001000", "0110001000", "0110111000", "0110111000", "0110001000", "0000000000"]
print(dompier_music(switches))
