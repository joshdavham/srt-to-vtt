from argparse import ArgumentParser


def srt_to_vtt(srt_file_path, vtt_file_path):

    with open(srt_file_path, "r") as srt_file:
        lines = srt_file.readlines()

    with open(vtt_file_path, "w") as vtt_file:

        # Required WEBVTT header and blank line for .vtt files
        vtt_file.write("WEBVTT\n\n")

        for line in lines:

            # Remove caption numbers as they're no longer
            # needed in .vtt files
            if line.strip().isdigit():
                continue

            # .vtt timestamps use commas, rather than
            # periods in their timestamps
            if "-->" in line:
                line = line.replace(",", ".")

            vtt_file.write(line)


def run():
    args = ArgumentParser(
        description="Python package to enable easy "
        "conversion of .srt files to .vtt files."
    )
    args.add_argument("-i", type=str, required=True, help="input filepath (.srt)")
    args.add_argument("-o", type=str, required=True, help="output filepath (.vtt)")
    ci = vars(args.parse_args())

    srt_to_vtt(srt_file_path=ci["i"], vtt_file_path=ci["o"])


if __name__ == "__main__":
    run()
