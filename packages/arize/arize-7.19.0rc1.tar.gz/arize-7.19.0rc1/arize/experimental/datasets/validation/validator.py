import uuid
from datetime import datetime
from typing import List

import pandas as pd

from . import errors as err


class Validator:
    @staticmethod
    def validate(
        df: pd.DataFrame,
    ) -> List[err.DatasetError]:
        ## check all require columns are present
        required_columns_errors = Validator._check_required_columns(df)
        if required_columns_errors:
            return required_columns_errors

        ## check id column is unique
        id_column_unique_constraint_error = Validator._check_id_column_is_unique(df)
        if id_column_unique_constraint_error:
            return id_column_unique_constraint_error

        return []

    @staticmethod
    def set_default_columns_for_dataset(df: pd.DataFrame) -> pd.DataFrame:
        current_time = pd.Timestamp(datetime.now()).floor("ms").tz_localize("UTC")
        if "created_at" in df.columns:
            if df["created_at"].isnull().values.any():
                df["created_at"].fillna(current_time, inplace=True)
        else:
            df["created_at"] = current_time

        if "updated_at" in df.columns:
            if df["updated_at"].isnull().values.any():
                df["updated_at"].fillna(current_time, inplace=True)
        else:
            df["updated_at"] = current_time

        if "id" in df.columns:
            if df["id"].isnull().values.any():
                df["id"] = df["id"].apply(lambda x: str(uuid.uuid4()) if pd.isnull(x) else x)
        else:
            df["id"] = [str(uuid.uuid4()) for _ in range(len(df))]

        df["__time"] = "1971-01-01T00:00:00.000Z"
        df["__time"] = pd.to_datetime(df["__time"], utc=True)
        return df

    @staticmethod
    def _check_required_columns(df: pd.DataFrame) -> List[err.DatasetError]:
        required_columns = ["id", "created_at", "updated_at", "__time"]
        missing_columns = set(required_columns) - set(df.columns)
        if missing_columns:
            return [err.RequiredColumnsError(missing_columns)]
        return []

    @staticmethod
    def _check_id_column_is_unique(df: pd.DataFrame) -> List[err.DatasetError]:
        if not df["id"].is_unique:
            return [err.IDColumnUniqueConstraintError]
        return []
