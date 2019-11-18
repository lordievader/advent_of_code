#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Test solution for AoC day 01.
"""
import pytest
import re

import part_1
import part_2


@pytest.fixture(scope='module')
def machine_obj():
    """Creates a machine with a few register values.
    """
    machine = part_1.Machine()
    machine.registers[0] = 2
    machine.registers[1] = 2
    machine.registers[2] = 1
    machine.registers[3] = 1
    return machine


@pytest.mark.parametrize('register_a,register_b,register_c,output', [
    (0, 1, 2, 4)
])
def test_part_1_addr(machine_obj, register_a, register_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.addr(register_a, register_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,value_b,register_c,output', [
    (0, 3, 2, 5)
])
def test_part_1_addi(machine_obj, register_a, value_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.addi(register_a, value_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,register_b,register_c,output', [
    (0, 1, 2, 4)
])
def test_part_1_mulr(machine_obj, register_a, register_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.mulr(register_a, register_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,value_b,register_c,output', [
    (0, 3, 2, 6)
])
def test_part_1_muli(machine_obj, register_a, value_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.muli(register_a, value_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,register_b,register_c,output', [
    (0, 1, 2, 2)
])
def test_part_1_banr(machine_obj, register_a, register_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.banr(register_a, register_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,value_b,register_c,output', [
    (0, 5, 2, 0)
])
def test_part_1_bani(machine_obj, register_a, value_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.bani(register_a, value_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,register_b,register_c,output', [
    (0, 1, 2, 2)
])
def test_part_1_borr(machine_obj, register_a, register_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.borr(register_a, register_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,value_b,register_c,output', [
    (0, 5, 2, 7)
])
def test_part_1_bori(machine_obj, register_a, value_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.bori(register_a, value_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,register_b,register_c,output', [
    (0, 1, 2, 2)
])
def test_part_1_setr(machine_obj, register_a, register_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.setr(register_a, register_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,value_b,register_c,output', [
    (0, 5, 2, 0)
])
def test_part_1_seti(machine_obj, register_a, value_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.seti(register_a, value_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('value_a,register_b,register_c,output', [
    (3, 1, 2, 1),
    (0, 1, 2, 0)
])
def test_part_1_gtir(machine_obj, value_a, register_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.gtir(value_a, register_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,value_b,register_c,output', [
    (0, 5, 2, 0),
    (0, 1, 2, 1)
])
def test_part_1_gtri(machine_obj, register_a, value_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.gtri(register_a, value_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,value_b,register_c,output', [
    (0, 2, 2, 1),
    (0, 1, 2, 0)
])
def test_part_1_gtrr(machine_obj, register_a, value_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.gtrr(register_a, value_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('value_a,register_b,register_c,output', [
    (2, 1, 2, 1),
    (0, 1, 2, 0)
])
def test_part_1_eqir(machine_obj, value_a, register_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.eqir(value_a, register_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,value_b,register_c,output', [
    (0, 2, 2, 1),
    (0, 1, 2, 0)
])
def test_part_1_eqri(machine_obj, register_a, value_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.eqri(register_a, value_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('register_a,value_b,register_c,output', [
    (0, 1, 2, 1),
    (0, 2, 2, 0)
])
def test_part_1_eqrr(machine_obj, register_a, value_b, register_c, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    machine_obj.eqrr(register_a, value_b, register_c)
    assert machine_obj.registers[register_c] == output


@pytest.mark.parametrize('problem_input,output', [
    ((
        "Before: [3, 2, 1, 1]\n"
        "9 2 1 2\n"
        "After:  [3, 2, 2, 1]\n"
        ), 3)
])
def test_part_1_number_of_opcodes(problem_input, output):
    assert part_1.number_of_opcodes(problem_input) == output


@pytest.mark.parametrize('problem_input,output', [
    ((
        "Before: [3, 2, 1, 1]\n"
        "9 2 1 2\n"
        "After:  [3, 2, 2, 1]\n"
        ), 1)
])
def test_part_1(problem_input, output):
    assert part_1.solution(problem_input) == output


def test_part_2():
    with open('part_1_input', 'r') as input_file:
        problem_input = input_file.read()

    problem_input_part_1 = re.split(r'\n\n\n', problem_input)[0]
    problem_input_part_2 = re.split(r'\n\n\n', problem_input)[1]
    # part_2.map_opcodes(problem_input_part_1)
    part_2.solution(problem_input_part_1, problem_input_part_2)
