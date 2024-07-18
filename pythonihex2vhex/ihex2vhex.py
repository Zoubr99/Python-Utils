import os

def convert_intel_hex_to_readmemh():
    try:
        # Prompt user for input file path
        hex_file_path = input("Enter the path to the Intel Hex file: ").strip()

        # Check if the file exists
        if not os.path.isfile(hex_file_path):
            print(f"Error: The file '{hex_file_path}' does not exist.")
            return
        
        # Prompt user for output file path
        output_file_path = input("Enter the path for the output readmemh file: ").strip()

        # Convert Intel Hex to readmemh format
        with open(hex_file_path, 'r') as hex_file, open(output_file_path, 'w') as output_file:
            line_counter = 0
            line_buffer = []

            for line in hex_file:
                if line[0] == ':':  # Valid Intel Hex record
                    byte_count = int(line[1:3], 16)
                    address = int(line[3:7], 16)
                    record_type = int(line[7:9], 16)

                    if record_type == 0:  # Data record
                        data = [int(line[i:i+2], 16) for i in range(9, 9 + byte_count * 2, 2)]

                        for i in range(0, len(data), 4):
                            chunk = data[i:i+4]
                            formatted_chunk = ''.join(f'{byte:02X}' for byte in chunk)
                            output_file.write(formatted_chunk + ' ')
                            line_counter += 1

                        output_file.write('\n')

            print(f"Conversion complete: {line_counter} lines written to {output_file_path}")

    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")

if __name__ == '__main__':
    convert_intel_hex_to_readmemh()
