import pandas as pd
from typing import Tuple
from sklearn.model_selection import train_test_split

FEATURE_COLS = [
    "da_power_mw", "rt_power_mw", "heat_rate_mmbtu_per_mwh",
    "temp_f", "dewpoint_f", "hdd", "cdd",
    "day_of_week", "holiday_flag"
]

TARGET_COL = "gas_burn_mmbtu"

def load_panel(path: str) -> pd.DataFrame:
    df = pd.read_parquet(path)
    df = df.sort_values(["generator_id", "timestamp"])
    return df

def train_val_test_split(
    df: pd.DataFrame,
    test_size: float = 0.2,
    val_size: float = 0.1,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    train_df, test_df = train_test_split(
        df, test_size=test_size, shuffle=False
    )
    train_df, val_df = train_test_split(
        train_df, test_size=val_size, shuffle=False
    )
    return train_df, val_df, test_df
