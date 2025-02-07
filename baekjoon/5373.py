from sys import stdin


def main():
    test_count = int(input())
    top_face_strings: list[str] = []
    for _ in range(test_count):
        cube = Cube()
        _ = int(stdin.readline().strip())
        for operation_string in stdin.readline().split():
            face_name = operation_string[0]
            clockwise = True if operation_string[1] == "+" else False
            cube.rotate(face_name, clockwise)
        top_face_colors = cube.faces["U"].colors
        top_face_string = "\n".join("".join(r) for r in top_face_colors)
        top_face_strings.append(top_face_string)
    print("\n".join(top_face_strings))


CUBE_SIZE = 3


class Face:
    def __init__(
        self, color: str, up_face: str, right_face: str, down_face: str, left_face: str
    ):
        self.colors = [[color] * CUBE_SIZE for _ in range(CUBE_SIZE)]
        self.up_face = up_face
        self.right_face = right_face
        self.down_face = down_face
        self.left_face = left_face

    def get_nearby_sequence(self, other_face: str) -> list[str]:
        # Returns a row or column right near that face.
        # The numbers are ordered as it is seen from that other face.

        if other_face == self.up_face:
            return list(reversed(self.colors[0]))
        elif other_face == self.right_face:
            return [r[-1] for r in reversed(self.colors)]
        elif other_face == self.down_face:
            return self.colors[-1].copy()
        elif other_face == self.left_face:
            return [r[0] for r in self.colors]
        else:
            raise ValueError

    def set_nearby_sequence(self, other_face: str, sequence: list[str]):
        # Assings a sequence of colors to a row or column right near that face.
        # The numbers should be ordered as it is seen from that other face.

        if other_face == self.up_face:
            for i, color in enumerate(sequence):
                self.colors[0][CUBE_SIZE - 1 - i] = color
        elif other_face == self.right_face:
            for i, color in enumerate(sequence):
                self.colors[CUBE_SIZE - 1 - i][-1] = color
        elif other_face == self.down_face:
            for i, color in enumerate(sequence):
                self.colors[-1][i] = color
        elif other_face == self.left_face:
            for i, color in enumerate(sequence):
                self.colors[i][0] = color
        else:
            raise ValueError


class Cube:
    def __init__(self):
        self.faces = {
            "U": Face("w", up_face="B", right_face="R", down_face="F", left_face="L"),
            "B": Face("o", up_face="U", right_face="L", down_face="D", left_face="R"),
            "R": Face("b", up_face="U", right_face="B", down_face="D", left_face="F"),
            "F": Face("r", up_face="U", right_face="R", down_face="D", left_face="L"),
            "L": Face("g", up_face="U", right_face="F", down_face="D", left_face="B"),
            "D": Face("y", up_face="B", right_face="L", down_face="F", left_face="R"),
        }

    def rotate(self, face_name: str, clockwise: bool):
        # Get the face.
        face = self.faces[face_name]

        # Rotate the colors on that face.
        colors_buffer = [[""] * CUBE_SIZE for _ in range(CUBE_SIZE)]
        colors = face.colors
        if clockwise:
            for r in range(CUBE_SIZE):
                for c in range(CUBE_SIZE):
                    colors_buffer[c][CUBE_SIZE - 1 - r] = colors[r][c]
        else:
            for r in range(CUBE_SIZE):
                for c in range(CUBE_SIZE):
                    colors_buffer[CUBE_SIZE - 1 - c][r] = colors[r][c]
        face.colors = colors_buffer

        # Rotate the nearby sequence on adjacent faces.
        up_face = face.up_face
        right_face = face.right_face
        down_face = face.down_face
        left_face = face.left_face
        prev_up = self.faces[up_face].get_nearby_sequence(face_name)
        prev_right = self.faces[right_face].get_nearby_sequence(face_name)
        prev_down = self.faces[down_face].get_nearby_sequence(face_name)
        prev_left = self.faces[left_face].get_nearby_sequence(face_name)
        if clockwise:
            self.faces[up_face].set_nearby_sequence(face_name, prev_left)
            self.faces[right_face].set_nearby_sequence(face_name, prev_up)
            self.faces[down_face].set_nearby_sequence(face_name, prev_right)
            self.faces[left_face].set_nearby_sequence(face_name, prev_down)
        else:
            self.faces[up_face].set_nearby_sequence(face_name, prev_right)
            self.faces[right_face].set_nearby_sequence(face_name, prev_down)
            self.faces[down_face].set_nearby_sequence(face_name, prev_left)
            self.faces[left_face].set_nearby_sequence(face_name, prev_up)


main()
