import srt_to_vtt

def test_convert():
    """
    Takes test_input.srt, converts it to test_output.vtt using srt_to_vtt.srt_to_vtt
    and compares it with valid_output.vtt.
    """

    srt_to_vtt.srt_to_vtt('test_input.srt', 'test_output.vtt')

    with open('test_output.vtt', 'r') as vtt_file:
        test_lines = vtt_file.readlines()

    with open('valid_output.vtt', 'r') as vtt_file:
        valid_lines = vtt_file.readlines()

    assert len(test_lines) == len(valid_lines)

    for i in range(len(test_lines)):

        test_line = test_lines[i]
        valid_line = valid_lines[i]

        assert test_line == valid_line
    
test_convert()