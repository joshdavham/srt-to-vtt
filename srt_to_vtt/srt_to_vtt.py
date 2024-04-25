def srt_to_vtt(srt_file_path, vtt_file_path):

    with open(srt_file_path, 'r') as srt_file:
        lines = srt_file.readlines()

    with open(vtt_file_path, 'w') as vtt_file:

        #Required WEBVTT header and blank line for .vtt files
        vtt_file.write('WEBVTT\n\n')

        for line in lines:

            #Remove caption numbers as they're no longer
            #needed in .vtt files
            if line.strip().isdigit():
                continue

            #.vtt timestamps use commas, rather than
            #periods in their timestamps
            if '-->' in line:
                line = line.replace(',', '.')

            vtt_file.write(line)

    