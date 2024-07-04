from py_output_compare.compare_file import (
    get_compare_output_by_path,
    get_score_by_path,
    print_compare_output_by_path,
)
from py_output_compare.find_file import (
    find_files,
    find_first_file_contain_id,
    find_first_file,
    count_files,
)
from py_output_compare.test_case import TestCase


class Problem:

    def __init__(
        self,
        problem_name: str,
        input_cases: list[TestCase] = [TestCase("")],
        do_normalize_input: bool = False,
        timeout_setting: float = 6,
        teacher_name: str = "manee-2024",
    ):
        self.problem_name = problem_name
        self.input_cases = input_cases
        self.do_normalize_input = do_normalize_input
        self.teacher_name = teacher_name
        self.timeout_setting = timeout_setting

    def get_max_score(self) -> int:
        return len(self.input_cases)

    def get_score_all(self) -> str:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        all_student = find_files(self.problem_name)
        result = []

        max_score = self.get_max_score()
        number_of_student = 0
        student_score_sum = 0

        print(f"start evaluate {self.problem_name}...")

        for student_file_path in all_student:
            score_num, score_emoji = get_score_by_path(
                student_file_path,
                teacher_file_path,
                self.input_cases,
                self.do_normalize_input,
                self.timeout_setting,
            )

            number_of_student += 1
            student_score_sum += score_num

            this_student_score = f"{score_num} {score_emoji} {student_file_path}"
            result.append(this_student_score)
        problem_score_max = max_score * number_of_student

        score_summary = (
            f"{number_of_student} students submit file\n"
            f"score_summary: [{student_score_sum:<4}]-({problem_score_max:<4}) [get]-(max)\n"
            f"average_score: [{(student_score_sum/number_of_student):<4.2f}]-({max_score:<4}) [get]-(max)"
        )

        result.append("-" * 80)
        result.append(score_summary)

        return "\n".join(result)

    def get_score_by_path_all(self, student_path_list: list[str]) -> str:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        result = []
        for student_file_path in student_path_list:
            score_num, score_emoji = get_score_by_path(
                student_file_path,
                teacher_file_path,
                self.input_cases,
                self.do_normalize_input,
                self.timeout_setting,
            )

            final_score_output = f"{score_num} {score_emoji} {student_file_path}"
            result.append(final_score_output)
        return "\n".join(result)

    def get_score_by_path(self, student_path: str) -> str:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        score_num, score_emoji = get_score_by_path(
            student_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )

        final_score_output = f"{score_num} {score_emoji} {student_path}"
        return final_score_output

    def get_output_by_path(self, student_path: str) -> str:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        result = get_compare_output_by_path(
            student_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )
        return result

    def get_output_id(self, student_id: str) -> str:
        student_file_path = find_first_file_contain_id(self.problem_name, student_id)
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        result = get_compare_output_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )
        return result

    def get_output_from_upload_file(self, upload_file_name="to_evaluate.py") -> str:
        student_file_path = find_first_file(upload_file_name)
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        result = get_compare_output_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
            score_web_format=True,
        )
        return result

    def get_score_id(self, student_id: str) -> str:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        student_file_path = find_first_file_contain_id(self.problem_name, student_id)

        score_num, score_emoji = get_score_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )

        final_score_output = f"{score_num} {score_emoji} {student_file_path}"
        return final_score_output

    def print_score_id(self, student_id: str) -> None:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        student_file_path = find_first_file_contain_id(self.problem_name, student_id)

        score_num, score_emoji = get_score_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )

        print(f"{score_num} {score_emoji} {student_file_path}")

    def print_score_all(self) -> None:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        all_student = find_files(self.problem_name)

        for student_file_path in all_student:
            score_num, score_emoji = get_score_by_path(
                student_file_path,
                teacher_file_path,
                self.input_cases,
                self.do_normalize_input,
                self.timeout_setting,
            )

            print(f"{score_num} {score_emoji} {student_file_path}")

    def print_output_id(self, student_id: str) -> None:
        student_file_path = find_first_file_contain_id(self.problem_name, student_id)
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        print_compare_output_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )

    def print_output_by_path(self, student_path: str) -> None:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        print_compare_output_by_path(
            student_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )

    def get_submit_count(self) -> int:
        return count_files(self.problem_name)
