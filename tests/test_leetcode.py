from datetime import datetime

import pyarrow as pa
import pytest

from problems.leetcode import (
    problem_176,
    problem_196,
    problem_197,
    problem_550,
    problem_577,
    problem_584,
    problem_595,
    problem_596,
    problem_610,
    problem_619,
    problem_620,
    problem_1045,
    problem_1068,
    problem_1075,
    problem_1141,
    problem_1148,
    problem_1161,
    problem_1164,
    problem_1193,
    problem_1211,
    problem_1280,
    problem_1327,
    problem_1378,
    problem_1581,
    problem_1633,
    problem_1667,
    problem_1683,
    problem_1729,
    problem_1757,
    problem_1934,
    problem_1978,
    problem_2356,
)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {"salary": [100, 200, 300]},
            {"SecondHighestSalary": [200]},
            id="distinct_salaries",
        ),
        pytest.param(
            {"salary": [100, 200, 200, 300]},
            {"SecondHighestSalary": [200]},
            id="multiple_second_highest",
        ),
        pytest.param(
            {"salary": [100]}, {"SecondHighestSalary": [None]}, id="single_salary"
        ),
        pytest.param(
            {"salary": [100, 100, 100]},
            {"SecondHighestSalary": [None]},
            id="all_salaries_same",
        ),
        pytest.param({"salary": []}, {"SecondHighestSalary": [None]}, id="empty_table"),
    ],
)
def test_problem_176(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_176(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "id": [1, 2, 3],
                "email": ["a@example.com", "b@example.com", "c@example.com"],
            },
            {
                "id": [1, 2, 3],
                "email": ["a@example.com", "b@example.com", "c@example.com"],
            },
            id="unique_emails",
        ),
        pytest.param(
            {
                "id": [1, 2, 3, 4],
                "email": [
                    "a@example.com",
                    "b@example.com",
                    "a@example.com",
                    "b@example.com",
                ],
            },
            {"id": [1, 2], "email": ["a@example.com", "b@example.com"]},
            id="duplicate_emails",
        ),
        pytest.param(
            {"id": [1], "email": ["a@example.com"]},
            {"id": [1], "email": ["a@example.com"]},
            id="single_row",
        ),
    ],
)
def test_problem_196(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_196(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 2)],
                "temperature": [20, 25],
                "id": [1, 2],
            },
            {"id": [2]},
            id="happy_path_basic",
        ),
        pytest.param(
            {
                "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 2)],
                "temperature": [25, 25],
                "id": [1, 2],
            },
            {"id": []},
            id="no_temperature_increase",
        ),
        pytest.param(
            {
                "recordDate": [datetime(2023, 1, 1)],
                "temperature": [20],
                "id": [1],
            },
            {"id": []},
            id="single_record",
        ),
        pytest.param(
            {
                "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 2)],
                "temperature": [25, 20],
                "id": [1, 2],
            },
            {"id": []},
            id="temperature_decrease",
        ),
        pytest.param(
            {
                "recordDate": [datetime(2023, 1, 1), datetime(2023, 1, 3)],
                "temperature": [20, 25],
                "id": [1, 2],
            },
            {"id": []},
            id="skip_a_day",
        ),
    ],
)
def test_problem_197(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("id", pa.int64())])
    )
    result = problem_197(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "player_id": [1, 1, 2, 3, 3],
                "device_id": [2, 2, 3, 1, 4],
                "event_date": [
                    datetime(2016, 3, 1),
                    datetime(2016, 3, 2),
                    datetime(2017, 6, 25),
                    datetime(2016, 3, 2),
                    datetime(2018, 7, 3),
                ],
                "games_played": [5, 6, 1, 0, 5],
            },
            {"fraction": [0.33]},
            id="happy_path_basic",
        ),
        pytest.param(
            {
                "player_id": [1, 1, 1, 2, 2],
                "event_date": [
                    datetime(2023, 1, 1),
                    datetime(2023, 1, 2),
                    datetime(2023, 1, 3),
                    datetime(2023, 1, 1),
                    datetime(2023, 1, 2),
                ],
                "games_played": [1, 2, 3, 4, 5],
            },
            {"fraction": [1.0]},
            id="happy_path_multiple_dates",
        ),
        pytest.param(
            {
                "player_id": [1],
                "event_date": [datetime(2023, 1, 1)],
                "games_played": [1],
            },
            {"fraction": [0.0]},
            id="edge_case_single_entry",
        ),
    ],
)
def test_problem_550(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_550(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
        pytest.param(
            {"empId": [1, 2], "name": ["Alice", "Bob"]},
            {"empId": [1, 2], "bonus": [1000, 1500]},
            {"name": ["Alice", "Bob"], "bonus": [1000, 1500]},
            id="happy_path_basic",
        )
    ],
)
def test_problem_577(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_577(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "id": [1, 2, 4, 5],
                "name": ["Will", "Jane", "Bill", "Zack"],
                "referee_id": [None, None, None, 1],
            },
            {"name": ["Will", "Jane", "Bill", "Zack"]},
            id="happy_path_all_valid",
        ),
        pytest.param(
            {
                "id": [3, 6],
                "name": ["Alex", "Mark"],
                "referee_id": [2, 2],
            },
            {"name": []},
            id="edge_case_all_referee_id_2",
        ),
        pytest.param(
            {
                "id": [1, 3, 5, 6],
                "name": ["Will", "Alex", "Zack", "Mark"],
                "referee_id": [None, 2, 1, 2],
            },
            {"name": ["Will", "Zack"]},
            id="mixed_case_some_valid",
        ),
    ],
)
def test_problem_584(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("name", pa.string())])
    )
    result = problem_584(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
                "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
                "area": [652_230, 28_748, 2_381_741, 468, 1_246_700],
                "population": [25_500_100, 2_831_741, 37_100_000, 78_115, 20_609_294],
                "gdp": [
                    20_343_000_000,
                    12_960_000_000,
                    188_681_000_000,
                    3_712_000_000,
                    100_990_000_000,
                ],
            },
            {
                "name": ["Afghanistan", "Algeria"],
                "population": [25_500_100, 37_100_000],
                "area": [652_230, 2_381_741],
            },
            id="happy_path_various_countries",
        ),
        pytest.param(
            {
                "name": ["CountryA", "CountryB"],
                "continent": ["ContinentA", "ContinentB"],
                "area": [3_000_000, 4_000_000],
                "population": [30_000_000, 40_000_000],
                "gdp": [1_000_000_000, 2_000_000_000],
            },
            {
                "name": ["CountryA", "CountryB"],
                "population": [30_000_000, 40_000_000],
                "area": [3_000_000, 4_000_000],
            },
            id="edge_case_all_countries_meeting_criteria",
        ),
    ],
)
def test_problem_595(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_595(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "student": [
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "F",
                    "G",
                    "H",
                    "I",
                    "J",
                    "K",
                    "L",
                ],
                "class": [
                    "Math",
                    "Math",
                    "Biology",
                    "Math",
                    "Computer",
                    "Math",
                    "Math",
                    "Math",
                    "Computer",
                    "Computer",
                    "Computer",
                    "Computer",
                ],
            },
            {"class": ["Math", "Computer"]},
            id="happy_path_multiple_classes",
        ),
        pytest.param(
            {
                "class": ["History", "History", "History", "History", "History"],
                "student": ["Alice", "Bob", "Charlie", "David", "Eve"],
            },
            {"class": ["History"]},
            id="edge_case_exactly_5_students",
        ),
        pytest.param(
            {
                "class": ["Art", "Art", "Art", "Art"],
                "student": ["Alice", "Bob", "Charlie", "David"],
            },
            {"class": []},
            id="edge_case_less_than_5_students",
        ),
    ],
)
def test_problem_596(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("class", pa.string())])
    )
    result = problem_596(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {"x": [3], "y": [4], "z": [5]},
            {"x": [3], "y": [4], "z": [5], "triangle": ["Yes"]},
            id="valid_triangle",
        ),
        pytest.param(
            {"x": [5], "y": [5], "z": [5]},
            {"x": [5], "y": [5], "z": [5], "triangle": ["Yes"]},
            id="equilateral_triangle",
        ),
        pytest.param(
            {"x": [2], "y": [2], "z": [3]},
            {"x": [2], "y": [2], "z": [3], "triangle": ["Yes"]},
            id="isosceles_triangle",
        ),
        pytest.param(
            {"x": [1], "y": [1], "z": [2]},
            {"x": [1], "y": [1], "z": [2], "triangle": ["No"]},
            id="degenerate_triangle",
        ),
        pytest.param(
            {"x": [0], "y": [0], "z": [0]},
            {"x": [0], "y": [0], "z": [0], "triangle": ["No"]},
            id="zero_length_sides",
        ),
        pytest.param(
            {"x": [1], "y": [2], "z": [3]},
            {"x": [1], "y": [2], "z": [3], "triangle": ["No"]},
            id="non_triangle",
        ),
    ],
)
def test_problem_610(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_610(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "num": [1, 2, 3, 4],
            },
            {"num": [4]},
            id="all_single_numbers",
        ),
        pytest.param(
            {
                "num": [1, 2, 2, 3, 3, 4],
            },
            {
                "num": [4],
            },
            id="mixed_single_and_duplicate_numbers",
        ),
        pytest.param(
            {
                "num": [2, 2, 3, 3],
            },
            {
                "num": [None],
            },
            id="all_duplicates",
        ),
    ],
)
def test_problem_619(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_619(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "id": [1, 2, 3, 4],
                "description": ["interesting", "boring", "exciting", "boring"],
            },
            {"id": [3, 1], "description": ["exciting", "interesting"]},
            id="happy_path_mixed_ids_and_descriptions",
        ),
        pytest.param(
            {"id": [1, 3], "description": ["boring", "boring"]},
            {"id": [], "description": []},
            id="edge_case_all_boring",
        ),
        pytest.param(
            {"id": [2, 4], "description": ["interesting", "exciting"]},
            {"id": [], "description": []},
            id="edge_case_no_odd_ids",
        ),
        pytest.param(
            {"id": [1], "description": ["interesting"]},
            {"id": [1], "description": ["interesting"]},
            id="edge_case_single_row_matching",
        ),
        pytest.param(
            {"id": [2], "description": ["boring"]},
            {"id": [], "description": []},
            id="edge_case_single_row_not_matching",
        ),
    ],
)
def test_problem_620(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data,
        schema=pa.schema(
            [pa.field("id", pa.int64()), pa.field("description", pa.string())]
        ),
    )
    result = problem_620(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
        pytest.param(
            {"customer_id": [1, 1, 2, 2], "product_key": [1, 2, 1, 2]},
            {"product_key": [1, 2]},
            {"customer_id": [1, 2]},
            id="happy_path_all_bought_all",
        ),
        pytest.param(
            {"customer_id": [1, 1, 2, 2], "product_key": [1, 2, 1, 3]},
            {"product_key": [1]},
            {"customer_id": []},
            id="happy_path_no_matching_distinct_count",
        ),
        pytest.param(
            {"customer_id": [], "product_key": []},
            {"product_key": [1]},
            {"customer_id": []},
            id="edge_case_empty_table_1",
        ),
        pytest.param(
            {"customer_id": [1, 1, 2, 2], "product_key": [1, 2, 1, 3]},
            {"product_key": []},
            {"customer_id": []},
            id="edge_case_empty_table_2",
        ),
        pytest.param(
            {"customer_id": [], "product_key": []},
            {"product_key": []},
            {"customer_id": []},
            id="edge_case_both_tables_empty",
        ),
    ],
)
def test_problem_1045(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(
        input_data_1,
        schema=pa.schema(
            [pa.field("customer_id", pa.int64()), pa.field("product_key", pa.int64())]
        ),
    )
    table_2 = pa.Table.from_pydict(
        input_data_2, schema=pa.schema([pa.field("product_key", pa.int64())])
    )
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("customer_id", pa.int64())])
    )
    result = problem_1045(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
        pytest.param(
            {
                "product_id": [1, 2, 3],
                "product_name": ["Nokia", "Nokia", "Apple"],
                "year": [2008, 2009, 2011],
                "price": [5000, 5000, 9000],
            },
            {"product_id": [1, 2, 3]},
            {
                "product_name": ["Nokia", "Nokia", "Apple"],
                "year": [2008, 2009, 2011],
                "price": [5000, 5000, 9000],
            },
            id="happy_path",
        )
    ],
)
def test_problem_1068(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1068(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
        pytest.param(
            {
                "employee_id": [1, 2, 3],
                "project_id": [101, 102, 103],
                "experience_years": [5, 10, 15],
            },
            {"employee_id": [1, 2, 3], "department": ["HR", "IT", "Finance"]},
            {"project_id": [101, 102, 103], "experience_years": [5.0, 10.0, 15.0]},
            id="happy_path",
        ),
        pytest.param(
            {
                "employee_id": [1, 2, 3],
                "project_id": [101, 101, 101],
                "experience_years": [33, 34, 34],
            },
            {"employee_id": [1, 2, 3], "department": ["HR", "IT", "IT"]},
            {"project_id": [101], "experience_years": [33.67]},
            id="happy_path_rounding_2",
        ),
    ],
)
def test_problem_1075(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1075(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "user_id": [1, 1, 1, 2, 2, 2],
                "session_id": [1, 1, 1, 4, 4, 4],
                "activity_date": [
                    datetime(2019, 7, 20, 0, 0),
                    datetime(2019, 7, 20, 0, 0),
                    datetime(2019, 7, 20, 0, 0),
                    datetime(2019, 7, 21, 0, 0),
                    datetime(2019, 7, 21, 0, 0),
                    datetime(2019, 7, 21, 0, 0),
                ],
                "activity_type": [
                    "open_session",
                    "scroll_down",
                    "end_session",
                    "open_session",
                    "send_message",
                    "end_session",
                ],
            },
            {
                "day": [
                    datetime(2019, 7, 20, 0, 0),
                    datetime(2019, 7, 21, 0, 0),
                ],
                "active_users": [1, 1],
            },
            id="happy_path_1",
        )
    ],
)
def test_problem_1141(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result_table = problem_1141(input_table)
    assert result_table.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "article_id": [1, 2, 3],
                "author_id": [3, 7, 4],
                "viewer_id": [3, 7, 4],
                "view_date": [
                    datetime(2019, 8, 1),
                    datetime(2019, 8, 1),
                    datetime(2019, 7, 21),
                ],
            },
            {
                "id": [3, 4, 7],
            },
            id="happy_path",
        ),
        pytest.param(
            {
                "article_id": [1, 2],
                "author_id": [3, 7],
                "viewer_id": [3, 7],
                "view_date": [datetime(2019, 8, 1), datetime(2019, 8, 1)],
            },
            {
                "id": [3, 7],
            },
            id="all_match",
        ),
    ],
)
def test_problem_1148(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1148(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "machine_id": [0, 0, 0, 0],
                "process_id": [0, 0, 1, 1],
                "activity_type": ["start", "end", "start", "end"],
                "timestamp": [0.712, 1.52, 3.14, 4.12],
            },
            {"machine_id": [0], "processing_time": [0.894]},
            id="happy_path_single_machine",
        ),
        pytest.param(
            {
                "machine_id": [0, 0, 1, 1, 2, 2],
                "process_id": [0, 0, 1, 1, 2, 2],
                "activity_type": ["start", "end", "start", "end", "start", "end"],
                "timestamp": [0.5, 1.5, 0.7, 1.2, 0.9, 2.0],
            },
            {"machine_id": [0, 1, 2], "processing_time": [1.0, 0.5, 1.1]},
            id="multiple_machines",
        ),
        pytest.param(
            {
                "machine_id": [0, 0, 1],
                "process_id": [0, 0, 1],
                "activity_type": ["start", "end", "start"],
                "timestamp": [0.5, 1.5, 0.7],
            },
            {"machine_id": [0, 1], "processing_time": [1.0, None]},
            id="incomplete_process",
        ),
    ],
)
def test_problem_1161(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1161(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "product_id": [1, 1, 2],
                "change_date": [
                    datetime(2019, 8, 15),
                    datetime(2019, 8, 16),
                    datetime(2019, 8, 17),
                ],
                "new_price": [100, 110, 120],
            },
            {"product_id": [1, 2], "price": [110, 10]},
            id="happy-path",
        ),
        pytest.param(
            {
                "product_id": [1, 2],
                "change_date": [
                    datetime(2019, 8, 17),
                    datetime(2019, 8, 18),
                ],
                "new_price": [100, 110],
            },
            {"product_id": [1, 2], "price": [10, 10]},
            id="no-products-before-cutoff",
        ),
        pytest.param(
            {
                "product_id": [1],
                "change_date": [
                    datetime(2019, 8, 18),
                ],
                "new_price": [20],
            },
            {"product_id": [1], "price": [10]},
            id="single-product-after-cutoff",
        ),
        pytest.param(
            {
                "product_id": [1, 2],
                "new_price": [100, 100],
                "change_date": [
                    datetime(2019, 8, 1),
                    datetime(2019, 8, 2),
                ],
            },
            {"product_id": [1, 2], "price": [100, 100]},
            id="all-products-before-cutoff",
        ),
    ],
)
def test_problem_1164(input_data, expected_data):
    input_table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1164(input_table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "trans_date": [
                    datetime(2023, 1, 1),
                    datetime(2023, 1, 15),
                    datetime(2023, 2, 1),
                ],
                "state": ["approved", "pending", "approved"],
                "amount": [100, 200, 300],
                "country": ["US", "US", "CA"],
                "id": [1, 2, 3],
            },
            {
                "month": ["2023-01", "2023-02"],
                "country": ["US", "CA"],
                "trans_count": [2, 1],
                "approved_count": [1, 1],
                "trans_total_amount": [300, 300],
                "approved_total_amount": [100, 300],
            },
            id="happy_path_1",
        ),
        pytest.param(
            {
                "trans_date": [datetime(2023, 3, 1)],
                "state": ["approved"],
                "amount": [500],
                "country": [None],
                "id": [4],
            },
            {
                "month": ["2023-03"],
                "country": [None],
                "trans_count": [1],
                "approved_count": [1],
                "trans_total_amount": [500],
                "approved_total_amount": [500],
            },
            id="happy_path_null_country",
        ),
        pytest.param(
            {
                "trans_date": [datetime(2023, 4, 1), datetime(2023, 4, 2)],
                "state": ["pending", "rejected"],
                "amount": [150, 250],
                "country": ["FR", "FR"],
                "id": [5, 6],
            },
            {
                "month": ["2023-04"],
                "country": ["FR"],
                "trans_count": [2],
                "approved_count": [0],
                "trans_total_amount": [400],
                "approved_total_amount": [0],
            },
            id="edge_case_all_unapproved",
        ),
    ],
)
def test_problem_1193(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1193(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "query_name": ["query1", "query1", "query2"],
                "rating": [4, 5, 2],
                "position": [2, 1, 1],
            },
            {
                "query_name": ["query1", "query2"],
                "quality": [3.5, 2.0],
                "poor_query_percentage": [0.0, 100.0],
            },
            id="happy_path_1",
        ),
        pytest.param(
            {
                "query_name": ["query1", "query2", "query2"],
                "rating": [3, 1, 5],
                "position": [1, 1, 1],
            },
            {
                "query_name": ["query1", "query2"],
                "quality": [3.0, 3.0],
                "poor_query_percentage": [0.0, 50.0],
            },
            id="happy_path_2",
        ),
    ],
)
def test_problem_1211(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1211(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, input_data_3, expected_data",
    [
        pytest.param(
            {
                "student_id": [1, 2, 13, 6],
                "student_name": ["Alice", "Bob", "John", "Alex"],
            },
            {"subject_name": ["Math", "Physics", "Programming"]},
            {
                "student_id": [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
                "subject_name": [
                    "Math",
                    "Physics",
                    "Programming",
                    "Programming",
                    "Physics",
                    "Math",
                    "Math",
                    "Programming",
                    "Physics",
                    "Math",
                    "Math",
                ],
            },
            {
                "student_id": [1, 1, 1, 2, 2, 2, 6, 6, 6, 13, 13, 13],
                "student_name": [
                    "Alice",
                    "Alice",
                    "Alice",
                    "Bob",
                    "Bob",
                    "Bob",
                    "Alex",
                    "Alex",
                    "Alex",
                    "John",
                    "John",
                    "John",
                ],
                "subject_name": [
                    "Programming",
                    "Physics",
                    "Math",
                    "Programming",
                    "Math",
                    "Physics",
                    "Programming",
                    "Physics",
                    "Math",
                    "Programming",
                    "Physics",
                    "Math",
                ],
                "attended_exams": [1, 2, 3, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            },
            id="happy_path",
        ),
        pytest.param(
            {
                "student_id": [1, 2, 13, 6],
                "student_name": ["Alice", "Bob", "John", None],
            },
            {"subject_name": ["Math", "Physics", "Programming"]},
            {
                "student_id": [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
                "subject_name": [
                    "Math",
                    "Physics",
                    "Programming",
                    "Programming",
                    "Physics",
                    "Math",
                    "Math",
                    "Programming",
                    "Physics",
                    "Math",
                    "Math",
                ],
            },
            {
                "student_id": [1, 1, 1, 2, 2, 2, 6, 6, 6, 13, 13, 13],
                "student_name": [
                    "Alice",
                    "Alice",
                    "Alice",
                    "Bob",
                    "Bob",
                    "Bob",
                    None,
                    None,
                    None,
                    "John",
                    "John",
                    "John",
                ],
                "subject_name": [
                    "Programming",
                    "Physics",
                    "Math",
                    "Programming",
                    "Math",
                    "Physics",
                    "Programming",
                    "Physics",
                    "Math",
                    "Programming",
                    "Physics",
                    "Math",
                ],
                "attended_exams": [1, 2, 3, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            },
            id="happy_path_null_name",
        ),
    ],
)
def test_problem_1280(input_data_1, input_data_2, input_data_3, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    table_3 = pa.Table.from_pydict(input_data_3)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1280(table_1, table_2, table_3)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
        pytest.param(
            {"product_id": [1, 2], "product_name": ["Product A", "Product B"]},
            {
                "product_id": [1, 2],
                "order_date": [datetime(2020, 2, 15), datetime(2020, 2, 20)],
                "unit": [150, 50],
            },
            {"product_name": ["Product A"], "unit": [150]},
            id="happy_path_single_match",
        ),
        pytest.param(
            {"product_id": [1], "product_name": ["Product A"]},
            {"product_id": [1], "order_date": [datetime(2020, 3, 1)], "unit": [150]},
            {"product_name": [], "unit": []},
            id="no_matching_year_month",
        ),
        pytest.param(
            {"product_id": [1], "product_name": ["Product A"]},
            {"product_id": [1], "order_date": [datetime(2020, 2, 15)], "unit": [50]},
            {"product_name": [], "unit": []},
            id="no_products_with_unit_sum_gte_100",
        ),
    ],
)
def test_problem_1327(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(
        expected_data,
        schema=pa.schema(
            [pa.field("product_name", pa.string()), pa.field("unit", pa.int64())]
        ),
    )
    result = problem_1327(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "table_data, table_2_data, expected_data",
    [
        pytest.param(
            {"id": [1, 2], "unique_id": [101, 102], "name": ["Alice", "Bob"]},
            {"id": [1, 2], "extra": ["x", "y"]},
            {"unique_id": [101, 102], "name": ["Alice", "Bob"]},
            id="happy_path_matching_ids",
        ),
        pytest.param(
            {"id": [1, 2], "unique_id": [101, 102], "name": ["Alice", "Bob"]},
            {"id": [3, 4], "extra": ["x", "y"]},
            {"unique_id": [101, 102], "name": ["Alice", "Bob"]},
            id="happy_path_non_matching_ids",
        ),
    ],
)
def test_problem_1378(table_data, table_2_data, expected_data):
    table = pa.Table.from_pydict(table_data)
    table_2 = pa.Table.from_pydict(table_2_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1378(table, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
        pytest.param(
            {
                "visit_id": [1, 2, 5, 5, 5, 4, 6, 7, 8],
                "customer_id": [23, 9, 54, 54, 54, 30, 96, 54, 54],
            },
            {
                "visit_id": [1, 2, 5],
                "transaction_id": [12, 13, 9],
                "amount": [910, 970, 200],
            },
            {"customer_id": [30, 96, 54], "count_no_trans": [1, 1, 2]},
            id="happy_path",
        ),
        pytest.param(
            {"visit_id": [10, 11], "customer_id": [100, 101]},
            {"visit_id": [1, 2], "transaction_id": [12, 13], "amount": [910, 970]},
            {"customer_id": [100, 101], "count_no_trans": [1, 1]},
            id="no_matching_visit_id",
        ),
    ],
)
def test_problem_1581(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    result = problem_1581(table_1, table_2)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
        pytest.param(
            {"contest_id": [1, 2], "user_id": [1, 2]},
            {"contest_id": [1, 1, 2], "user_id": [1, 2, 3]},
            {
                "contest_id": [1, 2],
                "percentage": [1.0, 0.5],
            },
            id="happy-path-1",
        ),
        pytest.param(
            {"contest_id": [1, 2, 3], "user_id": [1, 2, 3]},
            {"contest_id": [1, 2, 2, 3, 3, 3], "user_id": [1, 2, 3, 4, 5, 6]},
            {
                "contest_id": [3, 2, 1],
                "percentage": [1.0, 0.67, 0.33],
            },
            id="happy-path-2",
        ),
        pytest.param(
            {"contest_id": [1], "user_id": [1]},
            {"contest_id": [1], "user_id": [1]},
            {"contest_id": [1], "percentage": [1.0]},
            id="edge-single-row-table-2",
        ),
    ],
)
def test_problem_1633(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(input_data_1)
    table_2 = pa.Table.from_pydict(input_data_2)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1633(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {"user_id": [1, 2], "name": ["alice", "bob"]},
            {"user_id": [1, 2], "name": ["Alice", "Bob"]},
            id="happy_path_simple",
        ),
        pytest.param(
            {"user_id": [2, 1], "name": ["bob", "alice"]},
            {"user_id": [1, 2], "name": ["Alice", "Bob"]},
            id="happy_path_unsorted_user_id",
        ),
        pytest.param(
            {"user_id": [3, 4], "name": ["tyler", "MaRy KaThRyN"]},
            {"user_id": [3, 4], "name": ["Tyler", "Mary kathryn"]},
            id="edge_case_two_part_name_table",
        ),
        pytest.param(
            {"user_id": [1], "name": [""]},
            {"user_id": [1], "name": [""]},
            id="edge_case_empty_name",
        ),
        pytest.param(
            {"user_id": [1], "name": ["ALICE"]},
            {"user_id": [1], "name": ["Alice"]},
            id="edge_case_all_caps",
        ),
        pytest.param(
            {"user_id": [1, 2], "name": [None, "bob"]},
            {"user_id": [1, 2], "name": [None, "Bob"]},
            id="error_case_none_name",
        ),
    ],
)
def test_problem_1667(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_1667(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        (
            {"tweet_id": [1, 2], "content": ["Short", "This is a long tweet"]},
            {"tweet_id": [2]},
        ),
        (
            {
                "tweet_id": [1, 2],
                "content": ["This is a long tweet", "Another long tweet"],
            },
            {"tweet_id": [1, 2]},
        ),
    ],
    ids=[
        "content_greater_than_15",
        "all_content_greater_than_15",
    ],
)
def test_problem_1683(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    result = problem_1683(table)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {"user_id": [1, 1, 2, 2, 3], "follower_id": [10, 11, 12, 13, 14]},
            {"user_id": [1, 2, 3], "followers_count": [2, 2, 1]},
            id="multiple_users",
        ),
        pytest.param(
            {"user_id": [1], "follower_id": [10]},
            {"user_id": [1], "followers_count": [1]},
            id="single_user",
        ),
        pytest.param(
            {"user_id": [1, 1, 1], "follower_id": [10, 11, 12]},
            {"user_id": [1], "followers_count": [3]},
            id="single_user_multiple_followers",
        ),
    ],
)
def test_problem_1729(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    result = problem_1729(table)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        (
            {
                "product_id": [0, 1, 2, 3, 4],
                "low_fats": ["Y", "Y", "N", "Y", "N"],
                "recyclable": ["N", "Y", "Y", "Y", "N"],
            },
            {"product_id": [1, 3]},
        )
    ],
    ids=[
        "happy_path_mixed_values",
    ],
)
def test_problem_1757(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    result = problem_1757(table)
    expected_table = pa.Table.from_pydict(expected_data)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data_1, input_data_2, expected_data",
    [
        pytest.param(
            {"user_id": [1]},
            {"user_id": [1], "action": ["confirmed"]},
            {"user_id": [1], "confirmation_rate": [1.0]},
            id="user_confirmed",
        ),
        pytest.param(
            {"user_id": [1]},
            {"user_id": [1, 1], "action": ["confirmed", "confirmed"]},
            {"user_id": [1], "confirmation_rate": [1.0]},
            id="same_user_twice_confirmed",
        ),
        pytest.param(
            {"user_id": [1]},
            {"user_id": [1], "action": ["pending"]},
            {"user_id": [1], "confirmation_rate": [0.0]},
            id="user_not_confirmed",
        ),
        pytest.param(
            {"user_id": []},
            {"user_id": [], "action": []},
            {"user_id": [], "confirmation_rate": []},
            id="empty_tables",
        ),
        pytest.param(
            {"user_id": [1]},
            {"user_id": [1, 1], "action": ["confirmed", "pending"]},
            {"user_id": [1], "confirmation_rate": [0.5]},
            id="mixed_actions",
        ),
    ],
)
def test_problem_1934(input_data_1, input_data_2, expected_data):
    table_1 = pa.Table.from_pydict(
        input_data_1,
        schema=pa.schema(
            [
                pa.field("user_id", pa.int64()),
            ]
        ),
    )
    table_2 = pa.Table.from_pydict(
        input_data_2,
        schema=pa.schema(
            [
                pa.field("user_id", pa.int64()),
                pa.field("action", pa.string()),
            ]
        ),
    )
    expected_table = pa.Table.from_pydict(
        expected_data,
        schema=pa.schema(
            [
                pa.field("user_id", pa.int64()),
                pa.field("confirmation_rate", pa.float64()),
            ]
        ),
    )
    result = problem_1934(table_1, table_2)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {
                "employee_id": [3, 12, 13, 1, 9, 11, 14],
                "name": [
                    "Mila",
                    "Antonella",
                    "Emery",
                    "Kalel",
                    "Mikaela",
                    "Joziah",
                    "Hayden",
                ],
                "manager_id": [9.0, None, None, 11.0, None, 6.0, None],
                "salary": [60301, 31000, 67084, 21241, 50937, 28485, 4123],
            },
            {"employee_id": [11]},
            id="basic_filtering",
        ),
        pytest.param(
            {
                "employee_id": [3, 12, 13, 1, 9, 11, 14],
                "name": [
                    "Mila",
                    "Antonella",
                    "Emery",
                    "Kalel",
                    "Mikaela",
                    "Joziah",
                    "Hayden",
                ],
                "manager_id": [9.0, None, None, 11.0, None, 6.0, None],
                "salary": [60301, 31000, 67084, 31241, 50937, 38485, 41230],
            },
            {"employee_id": []},
            id="no_low_salary",
        ),
        pytest.param(
            {
                "employee_id": [3, 12, 13, 1, 9, 11, 14],
                "name": [
                    "Mila",
                    "Antonella",
                    "Emery",
                    "Kalel",
                    "Mikaela",
                    "Joziah",
                    "Hayden",
                ],
                "manager_id": [3, 12, 13, 1, 9, 11, 14],
                "salary": [60301, 31000, 67084, 21241, 50937, 28485, 4123],
            },
            {"employee_id": []},
            id="all_managers_are_employees",
        ),
        pytest.param(
            {
                "employee_id": [3, 12, 13, 1, 9, 11, 14],
                "name": [
                    "Mila",
                    "Antonella",
                    "Emery",
                    "Kalel",
                    "Mikaela",
                    "Joziah",
                    "Hayden",
                ],
                "manager_id": [None, None, None, None, None, None, None],
                "salary": [60301, 31000, 67084, 21241, 50937, 28485, 4123],
            },
            {"employee_id": []},
            id="all_manager_ids_null",
        ),
    ],
)
def test_problem_1978(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(
        expected_data, schema=pa.schema([pa.field("employee_id", pa.int64())])
    )
    result = problem_1978(table)
    assert result.equals(expected_table)


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param(
            {"teacher_id": [1, 1, 2, 2], "subject_id": [101, 102, 101, 103]},
            {"teacher_id": [1, 2], "cnt": [2, 2]},
            id="multiple_teachers_distinct_subjects",
        ),
        pytest.param(
            {"teacher_id": [1], "subject_id": [101]},
            {"teacher_id": [1], "cnt": [1]},
            id="single_teacher_single_subject",
        ),
        pytest.param(
            {"teacher_id": [1], "subject_id": [101]},
            {"teacher_id": [1], "cnt": [1]},
            id="single_teacher_repeated_subjects",
        ),
    ],
)
def test_problem_2356(input_data, expected_data):
    table = pa.Table.from_pydict(input_data)
    expected_table = pa.Table.from_pydict(expected_data)
    result = problem_2356(table)
    assert result.equals(expected_table)
