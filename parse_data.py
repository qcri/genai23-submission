import json


def parseCsvLine(line):
    data = line.split('","')
    assert(len(data) == 6)
    data[0] = data[0][1:]
    data[-1] = data[-1][:-2]
    return data

def createIdToLineNum(lines):
    id_to_line = {}
    for line_num, line in enumerate(lines):
        id = line.partition('","')[0][1:]
        id_to_line[int(id)] = line_num
    return id_to_line

def parseAndCombineData():
    csv_file = open('./data/philosophy.csv', 'r', encoding="utf8")
    json_file = open('./data/pg_embeddings.json', 'r', encoding="utf8")
    records = json.load(json_file)["RECORDS"]
    new_records = {"RECORDS": []}
    lines = csv_file.readlines()
    lines = lines[1:]
    id_to_line = createIdToLineNum(lines)
    for record in records:
        record_csv = parseCsvLine(lines[id_to_line[record["id"]]])
        new_record = {}
        new_record["id"] = str(record["id"])
        new_record["embedding"] = eval(record["embedding"])
        new_record["title"] = record_csv[1]
        new_record["url"] = record_csv[2]
        new_record["published_date"] = record_csv[3]
        new_record["content"] = record_csv[4]
        new_record["content_length"] = int(record_csv[5])
        new_records["RECORDS"].append(new_record)
    csv_file.close()
    json_file.close()
    combined_data_file = open('./data/parsed_data.json', 'w', encoding="utf8")
    json.dump(new_records, combined_data_file)
    combined_data_file.close()
    
        
parseAndCombineData()

