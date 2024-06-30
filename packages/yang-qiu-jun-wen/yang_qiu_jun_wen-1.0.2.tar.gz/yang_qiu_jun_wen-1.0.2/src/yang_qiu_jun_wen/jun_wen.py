def jun_wen(x):
    """
    计算列表x中所有数值类型的元素之和。

    参数：
    x -- 一个包含整数或浮点数的列表

    返回：
    列表x中的数值类型元素之和，如果列表为空或没有数值类型元素，则返回0。
    """
    # 初始化总和为0
    total = 0

    # 遍历列表中的每一个元素
    for item in x:
        # 如果元素是整数或浮点数类型，则累加到总和
        if isinstance(item, (int, float)):
            total += item

    return total