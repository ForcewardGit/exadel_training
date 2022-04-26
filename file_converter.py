class converter:
    def csv_to_json(self, csv_file_name: str):
        """ A class method to convert a csv file to a JSON file.
            Creates a new file with a name just like a given file name.
        """
        from json import dump

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

        if len(content) > 2:
            for key in dict_keys:
                d[key] = list()
        else:
            for key in dict_keys:
                d[key] = None
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
            dump(d, f)

        return None


    def json_to_csv(self, json_file_name: str):
        """ A class method to convert a JSON file to a csv file.
            Creates a new file with a name just like a given file name.
        """
        from json import load
        with open(json_file_name, "r") as f:
            d = load(f)
        
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
    c.csv_to_json("duration.csv")
    c.json_to_csv("sample.json")