def write_to_csv(row_value, csv_filename):
    write open(csv_filename, "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(row_value)



#quick launch
#printf '1\nlabelled-training-flows.csv\nlabelled-test-flows.csv' | python3 main.py
