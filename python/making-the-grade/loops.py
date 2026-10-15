"""Functions for organizing and calculating student exam scores."""

FAILING_THRESHOLD = 40
GRADES = ("A", "B", "C", "D", "F")
PASSING_GRADE_COUNT = len(GRADES) - 1
PERFECT_SCORE = 100


def round_scores(student_scores: list[float]) -> list[int]:
    """Round every student score to the nearest integer.

    Parameters:
        student_scores: Student exam scores.

    Returns:
        A new list with the rounded scores, in the same order.

    Note:
        Python's round() sends a score exactly halfway between two integers
        to the even one, so 40.5 becomes 40 but 41.5 becomes 42.

    Examples:
        >>> round_scores([90.33, 40.5, 41.5, 55.44])
        [90, 40, 42, 55]
    """
    rounded_student_scores = []
    for score in student_scores:
        rounded_student_scores.append(round(score))
    return rounded_student_scores


def count_failed_students(student_scores: list[int]) -> int:
    """Count how many students failed the exam.

    Parameters:
        student_scores: Student exam scores.

    Returns:
        The number of scores at or below the failing threshold.

    Examples:
        >>> count_failed_students([90, 40, 55, 70, 30, 25, 80, 95, 38, 40])
        5
    """
    failed_student_count = 0
    for score in student_scores:
        if score <= FAILING_THRESHOLD:
            failed_student_count += 1
    return failed_student_count


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Select the scores that reach the given threshold.

    Parameters:
        student_scores: Student exam scores.
        threshold: The minimum score to be selected.

    Returns:
        A new list with the scores at or above the threshold, in the same
        order.

    Examples:
        >>> above_threshold([90, 40, 55, 70, 30, 68, 70, 75, 83, 96], 75)
        [90, 75, 83, 96]
    """
    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    return best_scores


def letter_grades(highest: int) -> list[int]:
    """Calculate the lower score threshold of each passing letter grade.

    Parameters:
        highest: The highest score achieved in the exam.

    Returns:
        The lower thresholds for the grades D, C, B and A, in that order.

    Note:
        The range from the failing threshold to the highest score is split
        into equal intervals, one per passing grade. Their length is rounded
        down to a whole number.

    Examples:
        >>> letter_grades(100)
        [41, 56, 71, 86]

        >>> letter_grades(88)
        [41, 53, 65, 77]
    """
    interval_length = (highest - FAILING_THRESHOLD) // PASSING_GRADE_COUNT
    return list(range(FAILING_THRESHOLD + 1, highest, interval_length))


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """Create the ranking lines for students sorted by score.

    Parameters:
        student_scores: Scores in descending order.
        student_names: Names of the students, in the same order as their
            scores.

    Returns:
        One line per student in the format '<rank>. <name>: <score>',
        starting at rank 1.

    Raises:
        ValueError: If the two lists have different lengths.

    Examples:
        >>> student_ranking([100, 99, 90], ['Joci', 'Sara', 'Kora'])
        ['1. Joci: 100', '2. Sara: 99', '3. Kora: 90']
    """
    student_ranks = []
    for rank, (score, name) in enumerate(
        zip(student_scores, student_names, strict=True), start=1
    ):
        student_ranks.append(f"{rank}. {name}: {score}")
    return student_ranks


def perfect_score(student_info: list[list[str | int]]) -> list[str | int]:
    """Find the first student with a perfect score.

    Parameters:
        student_info: Pairs of [<name>, <score>], one per student.

    Returns:
        The first pair whose score is perfect, or an empty list if there is
        none.

    Examples:
        >>> perfect_score([['Charles', 90], ['Tony', 80], ['Alex', 100]])
        ['Alex', 100]

        >>> perfect_score([['Charles', 90], ['Tony', 80]])
        []
    """
    for student in student_info:
        if student[1] == PERFECT_SCORE:
            return student
    return []
