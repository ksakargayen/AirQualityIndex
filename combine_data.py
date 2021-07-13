import pandas as pd


def combine_data(year):
    average = []
    temp_i = 0
    for rows in pd.read_csv(f"Data/AQI/aqi{year}.csv", chunksize=24):
        add_var=0
        avg = 0
        df = pd.DataFrame(data=rows)
        data = [row["PM2.5"] for index, row in df.iterrows()]
        for i in data:
            if isinstance(i, (float, int)):
                add_var = add_var + i
            elif isinstance(i, str) and i != "NoData" and i != "PwrFail" and \
                    i != "---" and i != "InVld":
                add_var = add_var + float(i)
        avg = add_var/24
        temp_i = temp_i + 1

        average.append(avg)
    return average


if __name__ == "__main__":
    for y in range(2013, 2019):
        print(y, len(combine_data(y)))
