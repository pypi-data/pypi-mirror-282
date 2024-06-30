import pandas as pd
import numpy as np
def rma(src: pd.Series, length: int = 14) -> pd.Series:
    """指数加权移动平均线（rma），alpha加权值 = 1 /长度

    Args:
        src (pd.Series): 数据源（e.g. data["close"]）
        length (int, optional): 周期长度. Defaults to 14.

    Raises:
        ValueError: 周期长度必须大于0

    Returns:
        pd.Series: rma
    """

    # 检查长度是否大于0
    if length <= 0:
        raise ValueError("周期长度必须大于0")

    # 初始化alpha
    alpha = 1 / length

    # 创建一个与src同样长度的Series来存储结果，初始化为NaN
    result = pd.Series(np.nan, index=src.index)

    # 填充第一个值，通常与SMA相同（或者使用第一个src值作为近似）
    result.iloc[0] = src.iloc[0] if length == 1 else src[:length].mean()

    # 计算RMA值
    for i in range(1, len(src)):
        if not np.isnan(result.iloc[i - 1]):  # 检查前一个值是否不是NaN
            result.iloc[i] = alpha * src.iloc[i] + (1 -
                                                    alpha) * result.iloc[i - 1]
        else:  # 如果前一个值是NaN（例如，在序列开始时），则使用SMA或src值
            # 这里我们使用SMA作为替代，但你也可以选择使用src的当前值
            if i >= length:
                result.iloc[i] = src[i - length:i].mean() * (
                    1 - alpha) + alpha * src.iloc[i]
            else:
                # 如果还没有足够的值来计算SMA，则可以使用src的当前值或保持为NaN
                result.iloc[i] = src.iloc[i]

    return result.astype(np.float32)