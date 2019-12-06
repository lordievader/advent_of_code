mod read_input;
mod timing;
mod intcode;

fn part_1(input: &Vec<i32>) -> i32 {
    let output_value = intcode::execute(input, 1);
    output_value.0
}

fn part_2(input: &Vec<i32>) -> i32 {
    let output_value = intcode::execute(input, 5);
    output_value.0
}

fn main() {
    let raw_input = read_input::read_lines("input.txt").unwrap().pop().unwrap();
    let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();

    let start_part_1 = timing::start();
    let part_1_answer = part_1(&input);
    timing::stop(start_part_1);
    println!("Part 1 answer: {}", part_1_answer);

    let start_part_2 = timing::start();
    let part_2_answer = part_2(&input);
    timing::stop(start_part_2);
    println!("Part 2 answer: {}", part_2_answer);
}
