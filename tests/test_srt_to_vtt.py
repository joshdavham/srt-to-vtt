import unittest
import os
import srt_to_vtt


class Test_srt_to_vtt(unittest.TestCase):

    def test_convert(self):
        """
        Takes test_input.srt, converts it to test_output.vtt using srt_to_vtt.srt_to_vtt
        and compares it with valid_output.vtt.
        """

        self.base_directory = os.path.dirname(__file__)
        self.input_path = os.path.join(self.base_directory, "test_input.srt")
        self.expected_output_path = os.path.join(
            self.base_directory, "valid_output.vtt"
        )
        self.output_path = os.path.join(self.base_directory, "test_output.vtt")

        srt_to_vtt.srt_to_vtt(self.input_path, self.output_path)

        with open(self.output_path, "r") as vtt_file:
            test_lines = vtt_file.readlines()

        with open(self.expected_output_path, "r") as vtt_file:
            valid_lines = vtt_file.readlines()

        self.assertEqual(len(test_lines), len(valid_lines))

        for i in range(len(test_lines)):

            test_line = test_lines[i]
            valid_line = valid_lines[i]

            self.assertEqual(test_line, valid_line)


if __name__ == "__main__":
    unittest.main()
