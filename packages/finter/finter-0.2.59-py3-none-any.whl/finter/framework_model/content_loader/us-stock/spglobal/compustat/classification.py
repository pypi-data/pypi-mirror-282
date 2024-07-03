from finter.framework_model.content import Loader


class ClassificationLoader(Loader):
    def __init__(self, cm_name):
        self.__CM_NAME = cm_name
        self.__FREQ = cm_name.split(".")[-1]

    def get_df(
        self, start: int, end: int, fill_nan=True, currency=None, *args, **kwargs
    ):
        raw = self._load_cache(
            self.__CM_NAME,
            start,
            end,
            universe="us-compustat-stock",
            freq=self.__FREQ,
            fill_nan=fill_nan,
            *args,
            **kwargs,
        )

        univ = self._load_cache(
            "content.spglobal.compustat.universe.us-stock-constituent.1d",
            start,  # to avoid start dependency in dataset
            end,
            universe="us-compustat-stock",
            freq=self.__FREQ,
            fill_nan=fill_nan,
            *args,
            **kwargs,
        )

        univ.columns = [col[:-2] for col in univ.columns]
        # 중복된 컬럼명을 찾음
        duplicated_columns = univ.columns[univ.columns.duplicated()].unique()

        # 중복된 컬럼들을 max 값으로 유지
        for col in duplicated_columns:
            max_vals = univ.filter(like=col).max(axis=1)
            univ = univ.drop(columns=univ.filter(like=col).columns)
            univ[col] = max_vals

        # 중복된 컬럼 제거
        univ = univ.loc[:, ~univ.columns.duplicated()]

        # 필터 적용
        raw = raw.loc[univ.index[0] :] * univ

        return raw
