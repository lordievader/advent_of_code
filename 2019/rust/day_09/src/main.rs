mod read_input;
mod timing;
mod intcode;

fn part_1(input: &Vec<i64>) -> i64 {
    let length = input.len();
    let amp = intcode::Amp {
        state: input.to_vec(),
        index: 0,
        input_values: vec![1],
        output_value: 0,
        finished: 0,
        relative_base: 0,
    };
    let mut state = intcode::execute(amp);
    while state.finished == 0 {
        state = intcode::execute(state);
        println!("{}/{}", state.index, length);
    }
    if state.finished == 2 {
        println!("ERROR");
    }
    state.output_value
}

fn part_2(input: &Vec<i64>) -> i64 {
    let length = input.len();
    let amp = intcode::Amp {
        state: input.to_vec(),
        index: 0,
        input_values: vec![2],
        output_value: 0,
        finished: 0,
        relative_base: 0,
    };
    let mut state = intcode::execute(amp);
    while state.finished == 0 {
        state = intcode::execute(state);
        println!("{}/{}", state.index, length);
    }
    if state.finished == 2 {
        println!("ERROR");
    }
    state.output_value
}

fn main() {
    let raw_input = read_input::read_lines("input.txt").unwrap().pop().unwrap();
    let input: Vec<i64> = raw_input.split(",").map(|x| x.parse::<i64>().unwrap()).collect();

    let start_part_1 = timing::start();
    let part_1_answer = part_1(&input);
    timing::stop(start_part_1);
    println!("Part 1 answer: {}", part_1_answer);

    let start_part_2 = timing::start();
    let part_2_answer = part_2(&input);
    timing::stop(start_part_2);
    println!("Part 2 answer: {}", part_2_answer);
}


mod tests{
    use super::*;

    // #[test]
    // fn test_part1() {
    //     let raw_input = read_input::read_lines("test.txt").unwrap().pop().unwrap();
    //     let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
    //     assert_eq!(part_1(&input), 43210);

    //     let raw_input = read_input::read_lines("test2.txt").unwrap().pop().unwrap();
    //     let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
    //     assert_eq!(part_1(&input), 54321);

    //     let raw_input = read_input::read_lines("test3.txt").unwrap().pop().unwrap();
    //     let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
    //     assert_eq!(part_1(&input), 65210);
    // }

    // #[test]
    // fn test_part_2() {
    //     let raw_input = read_input::read_lines("test4.txt").unwrap().pop().unwrap();
    //     let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
    //     assert_eq!(
    //         part_2(&input),
    //         139629729
    //     );

    //     let raw_input = read_input::read_lines("test5.txt").unwrap().pop().unwrap();
    //     let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
    //     assert_eq!(
    //         part_2(&input), 
    //         18216
    //     );
    // }
}