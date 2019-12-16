use permute;
use std::collections::HashMap;
mod read_input;
mod timing;
mod intcode;


fn amplify(input: &Vec<i64>, mut phases: Vec<i64>) -> i64 {
    // amp A
    let amp = intcode::Amp {
        state: input.to_vec(),
        index: 0,
        input_values: vec![0, phases.pop().unwrap()],
        output_value: 0,
        finished: false,
        relative_base: 0,
    };
    let mut state = intcode::execute(&amp);
    while state.finished == false {
        state = intcode::execute(&state);
    }

    // amp B - E
    let mut output_value = state.output_value;
    while !phases.is_empty() {
        let mut state = intcode::Amp {
            state: input.to_vec(),
            index: 0,
            input_values: vec![output_value, phases.pop().unwrap()],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        state = intcode::execute(&state);
        while state.finished == false {
            state = intcode::execute(&state);
        }
        output_value = state.output_value;
    }
    return output_value;
}

fn part_1(input: &Vec<i64>) -> i64 {
    let phases = vec![0, 1, 2, 3, 4];
    let mut max_output = 0;
    for perm in permute::permute(phases).into_iter() {
        let output = amplify(input, perm);
        if output > max_output {
            max_output = output;
        }
    }
    max_output
}


fn amplify_part_2(input: &Vec<i64>, mut phases: Vec<i64>) -> i64 {
    let mut amp_map = HashMap::new();
    let mut input_value: i64 = 0;
    for name in vec!["A", "B", "C", "D", "E"].into_iter() {
        let amp = intcode::Amp {
            state: input.to_vec(),
            index: 0,
            input_values: vec![input_value, phases.pop().unwrap()],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };

        let amp = intcode::execute(&amp);
        // println!("Name: {}: {:?}", name, amp);
        input_value = amp.output_value;
        amp_map.insert(name, amp);
    }

    let mut finished = false;
    while !finished {
        for name in vec!["A", "B", "C", "D", "E"].into_iter() {
            let mut amp = amp_map.get(name).unwrap().clone();
            amp.input_values = vec![input_value];
            let update = intcode::execute(&amp);
            if !update.finished {
                input_value = update.output_value;
            }
            finished = update.finished;
            // println!("Name: {}: {:?}", name, update);
            amp_map.insert(name, update);
        }
    }
    input_value
}

fn part_2(input: &Vec<i64>) -> i64 {
    let phases = vec![5,6,7,8,9];
    let mut max_output = 0;
    for perm in permute::permute(phases).into_iter() {
        let output = amplify_part_2(input, perm);
        if output > max_output {
            max_output = output;
        }
    }
    max_output
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

    #[test]
    fn test_amplify(){
        let raw_input = read_input::read_lines("test.txt").unwrap().pop().unwrap();
        let input: Vec<i64> = raw_input.split(",").map(|x| x.parse::<i64>().unwrap()).collect();
        let phases = vec![0, 1, 2, 3, 4];
        assert_eq!(amplify(&input, phases), 43210);
    }

    #[test]
    fn test_part1() {
        let raw_input = read_input::read_lines("test.txt").unwrap().pop().unwrap();
        let input: Vec<i64> = raw_input.split(",").map(|x| x.parse::<i64>().unwrap()).collect();
        assert_eq!(part_1(&input), 43210);

        let raw_input = read_input::read_lines("test2.txt").unwrap().pop().unwrap();
        let input: Vec<i64> = raw_input.split(",").map(|x| x.parse::<i64>().unwrap()).collect();
        assert_eq!(part_1(&input), 54321);

        let raw_input = read_input::read_lines("test3.txt").unwrap().pop().unwrap();
        let input: Vec<i64> = raw_input.split(",").map(|x| x.parse::<i64>().unwrap()).collect();
        assert_eq!(part_1(&input), 65210);
    }

    #[test]
    fn test_amplify_part_2(){
        let raw_input = read_input::read_lines("test4.txt").unwrap().pop().unwrap();
        let input: Vec<i64> = raw_input.split(",").map(|x| x.parse::<i64>().unwrap()).collect();
        let phases = vec![5,6,7,8,9];
        assert_eq!(
            amplify_part_2(&input, phases), 
            139629729
        );

        let raw_input = read_input::read_lines("test5.txt").unwrap().pop().unwrap();
        let input: Vec<i64> = raw_input.split(",").map(|x| x.parse::<i64>().unwrap()).collect();
        let phases = vec![6,5,8,7,9];
        assert_eq!(
            amplify_part_2(&input, phases), 
            18216
        );
    }

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