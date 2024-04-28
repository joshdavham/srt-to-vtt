import os
import srt_to_vtt


class TestClass:
    def test_convert(self):
        """
        Takes test_input.srt, converts it to test_output.vtt using srt_to_vtt.srt_to_vtt
        and compares it with valid_output.vtt.
        """

        base_directory = os.path.dirname(__file__)
        input_path = os.path.join(base_directory, "test_input.srt")
        expected_output_path = os.path.join(base_directory, "valid_output.vtt")
        output_path = os.path.join(base_directory, "test_output.vtt")

        srt_to_vtt.srt_to_vtt(input_path, output_path)

        with open(output_path, "r") as vtt_file:
            test_lines = vtt_file.readlines()

        with open(expected_output_path, "r") as vtt_file:
            valid_lines = vtt_file.readlines()

        assert len(test_lines) == len(valid_lines)

        for i in range(len(test_lines)):

            test_line = test_lines[i]
            valid_line = valid_lines[i]

            assert test_line == valid_line
