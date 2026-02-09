import sys

def file_to_plain_hex(input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()

    hex_string = data.hex().upper()

    with open(output_file, "w") as out:
        out.write(hex_string)

    print(f"Converted {len(data)} bytes into hex.")
    print(f"Output written to: {output_file}")

if __name__ == "__main__":
    infile = input("Type input file name >>")
    outfile = input("Type output file name >>" )

    file_to_plain_hex(infile, outfile)
