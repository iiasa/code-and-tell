import pandas as pd
from pandas._testing import assert_frame_equal
from typing import Union
from pathlib import Path


def read_data(file: Union[str, Path]) -> pd.DataFrame:
    return pd.read_csv(file)


if __name__ == "__main__":
    df1 = read_data("sample_data.csv")
    df2 = read_data(
        Path("/home/hackstock/Documents/code/MESSAGEix-weekly") / "sample_data.csv"
    )
    assert_frame_equal(df1, df2)
    print(df1.head(3))
    print(df2.head(3))
