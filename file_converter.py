class converter:
    def csv_to_json(self, csv_file_name: str):
        """ A class method to convert a csv file to a JSON file.
            Creates a new file with a name just like a given file name.
        """
        ### Create a dictionary from a csv file ###
        d = dict()
        with open(csv_file_name, "r") as f:
            content = f.read().split("\n")
            dict_keys = content[0].split(",")

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
                if row_data[j].isnumeric():
                    try:
                        if len(content) > 2:
                            d[dict_keys[j]].append(int(row_data[j]))
                        else:
                            d[dict_keys[j]] = int(row_data[j])
                    except ValueError:
                        if len(content) > 2:
                            d[dict_keys[j]].append(row_data[j])
                        else:
                            d[dict_keys[j]] = row_data[j]                     
                else:
                    try:
                        if len(content) > 2:
                            d[dict_keys[j]].append(float(row_data[j]))
                        else:
                            d[dict_keys[j]] = float(row_data[j])
                    except ValueError:
                        if len(content) > 2:
                            d[dict_keys[j]].append(row_data[j])
                        else:
                            d[dict_keys[j]] = row_data[j]

            
        ### Create json file and load data to it ###
        json_file_name = csv_file_name.split(".")[0] + ".json"
        with open(json_file_name, "w") as f:
            f.write("{")
            i = 0
            for key, value in d.items():
                i += 1
                feature = "\"" + key + "\"" + ": " + str(value)
                f.write(feature + ",") if i != len(d) else f.write(feature)
            f.write("}")
        
        ### Get rid of ' if there are any ###
        with open(json_file_name, "r") as f:
            content = f.read()
            content = content.replace("'", "\"")
            print(content)
        
        ### Write new string without ' characters ###
        with open(json_file_name, "w") as f:
            f.write(content)

        return None


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