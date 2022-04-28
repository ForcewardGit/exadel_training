from types import NoneType


class converter:
    def csv_to_json(self, csv_file_name: str):
        """ A class method to convert a csv file to a JSON file.
            Creates a new file with a name just like a given file name.
            Returns a dictionary representation of a csv.
        """
        ### Create a dictionary from a csv file ###
        d = dict() # csv column names as keys, values - column content
        with open(csv_file_name, "r") as f:
            content = f.read().split("\n")
            dict_keys = content[0].split(",")

        ### Ignore empty rows ###
        content = [content_data for content_data in content if content_data != ""]
        
        ### In case when the file content is not filled ###
        if len(content) < 2:
            print("Not a complete file!")
            return None

        ### Represent a column content as a list or just a single value depending on length ###
        if len(content) > 2:
            for key in dict_keys:
                d[key] = list()
        else:
            for key in dict_keys:
                d[key] = None

        ### Iterate through each row, and for each row through its columns to add values to 
        #   dictionary's appropriate key's value
        ###
        for i in range(1, len(content)):
            row_data = content[i].split(",")
            for j in range(len(row_data)):
                record = row_data[j]
                if row_data[j].isnumeric():
                    if len(content) > 2:
                        d[dict_keys[j]].append(int(record))
                    else:
                        d[dict_keys[j]] = int(record)
                elif record.lower() == "true" or record.lower() == "false":
                    flag = True if record.lower() == "true" else False
                    if len(content) > 2:
                        d[dict_keys[j]].append(flag)
                    else:
                        d[dict_keys[j]] = flag
                else:
                    if record.lower() == "null":
                        record = None
                    try:
                        if len(content) > 2:
                            d[dict_keys[j]].append(float(record))
                        else:
                            d[dict_keys[j]] = float(record)
                    except (ValueError, TypeError):
                        if len(content) > 2:
                            d[dict_keys[j]].append(record)
                        else:
                            d[dict_keys[j]] = record
   
        ### Create json file and load data to it ###
        json_file_name = csv_file_name.split(".")[0] + ".json"
        with open(json_file_name, "w") as f:
            f.write("{\n\t")
            i = 0
            for key, value in d.items():
                i += 1
                feature = "\"" + key + "\"" + ": "
                # print(value, value[0] is value[-1], value[0] == value[-1])
                if len(content) > 2:
                    feature += "["
                    for k in range(len(value)):
                        v = value[k]
                        if type(v) is bool:
                            feature += str(v).lower()
                        elif type(v) is NoneType:
                            feature += "null"
                        elif type(v) is str:
                            feature += "\"" + v + "\""
                        else:
                            feature += str(v)
                        feature += ", " if k != len(value)-1 else ""
                    feature += "]"
                else:
                    if type(value) is bool:
                        feature += str(value).lower()
                    elif type(value) is NoneType:
                        feature += "null"
                    elif type(value) is str:
                        feature += "\"" + str(value) + "\""
                    else:
                        feature += str(value)
                f.write(feature + ",\n\t") if i != len(d) else f.write(feature)
            f.write("\n}")
        
        ### Get rid of ' if there are any ###
        with open(json_file_name, "r") as f:
            content = f.read()
            content = content.replace("'", "\"")
        
        ### Write new string without ' characters ###_
        with open(json_file_name, "w") as f:
            f.write(content)

        return d


    def json_to_csv(self, json_file_name: str):
        """ A class method to convert a JSON file to a csv file.
            Creates a new file with a name just like a given file name.
        """
        ### Load JSON file into a dictionary ###
        with open(json_file_name, "r") as f:
            d = dict()
            dict_items = list() # a list of (key, value) tuples
            content = f.read()
            content = content[1:-1]
            content = content.replace("\n", "")
            content = content.replace("\"", "").strip()
            
            for i in range(len(content)):
                if content[i] == "," and content[i-1] == "]":
                    content = content[:i] + "|" + content[i+1:]
            dict_items = content.split("|") if "[" in content else content.split(",")
            
            for item in dict_items:
                # print(item.split(":"))
                key, value = tuple(item.split(":"))
                key, value = key.strip(), value.strip()
                if value[0] == "[":
                    value = value[1:-1]
                value = value.split(",")
                value = [item.strip() for item in value]
                d[key] = value
        
        csv_file_name = json_file_name.split(".")[0] + ".csv"
        
        ### Write a header of csv file first ###
        with open(csv_file_name, "w") as f:
            for key in d.keys():
                f.write(key + ",") if key != list(d.keys())[-1] else f.write(key + "\n")
        
        ### Separate same row elements ###
        csv_row_contents = list()
        if type(list(d.values())[0]) is list:
            for i in range(len(list(d.values())[0])):
                csv_ith_row = list()
                for csv_column in d.values():
                    csv_ith_row.append(csv_column[i])
                csv_row_contents.append(csv_ith_row)
        else:
            row = []
            for value in d.values():
                row.append(value)
            csv_row_contents.append(row)
        
        ### Write the remaining content of csv file ###
        with open(csv_file_name, "a") as f:
            for row in csv_row_contents:
                for data in row:
                    f.write(str(data) + ",") if data != row[-1] else f.write(str(data) + "\n")
        

        return None

        

if __name__ == "__main__":
    c = converter()
    # c.csv_to_json("duration.csv")
    c.json_to_csv("sample.json")
