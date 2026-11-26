def Avg(grades):
    """محاسبه معدل نمرات"""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def max_grade(grades):
    """پیدا کردن بیشترین نمره"""
    if not grades:
        return 0
    return max(grades)

def min_grade(grades):
    """پیدا کردن کمترین نمره"""
    if not grades:
        return 0
    return min(grades)