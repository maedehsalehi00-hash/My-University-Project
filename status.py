def check_status(average):
    """تعیین وضعیت قبولی یا مردودی بر اساس معدل"""
    if average >= 10:
        return "Acc"  # Accepted (قبول)
    else:
        return "Rej"  # Rejected (رد)