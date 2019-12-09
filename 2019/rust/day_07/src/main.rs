use permute;
use std::collections::HashMap;
mod read_input;
mod timing;
mod intcode;


fn amplify(input: &Vec<i32>, mut phases: Vec<i32>) -> i32 {
    // amp A
    let input_values = vec![0, phases.pop().unwrap()];
    let mut output_value = intcode::execute(input, input_values);
    // println!("{:?}", output_value);

    // amd B - E
    while !phases.is_empty() {
        let input_values = vec![output_value.0, phases.pop().unwrap()];
        output_value = intcode::execute(input, input_values);
        // println!("{:?}", output_value);    
    }
    return output_value.0;
}

fn part_1(input: &Vec<i32>) -> i32 {
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


fn amplify_part_2(input: &Vec<i32>, mut phases: Vec<i32>) -> i32 {
    let mut amp_map = HashMap::new();
    let mut input_value: i32 = 0;
    for name in vec!["A", "B", "C", "D", "E"].into_iter() {
        let input_values = vec![input_value, phases.pop().unwrap()];
        let amp = intcode::get_output(input, 0, input_values, 0);
        // println!("Name: {}: {:?}", name, amp);
        input_value = amp.output_value;
        amp_map.insert(name, amp);
    }

    let mut finished = false;
    while !finished {
        for name in vec!["A", "B", "C", "D", "E"].into_iter() {
            let input_values = vec![input_value];
            let amp = amp_map.get(name).unwrap();
            let update = intcode::get_output(&amp.state, amp.index, input_values, amp.output_value);
            if !update.finished {
                input_value = update.output_value;
            }
            finished = update.finished;
            // println!("Name: {}: {:?}", name, update);
            amp_map.insert(name, update);
        }
    }
    input_value
    // 0
}

fn part_2(input: &Vec<i32>) -> i32 {
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


mod tests{
    use super::*;

    #[test]
    fn test_amplify(){
        let raw_input = read_input::read_lines("test.txt").unwrap().pop().unwrap();
        let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        let phases = vec![0, 1, 2, 3, 4];
        assert_eq!(amplify(&input, phases), 43210);
    }

    #[test]
    fn test_part1() {
        let raw_input = read_input::read_lines("test.txt").unwrap().pop().unwrap();
        let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        assert_eq!(part_1(&input), 43210);

        let raw_input = read_input::read_lines("test2.txt").unwrap().pop().unwrap();
        let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        assert_eq!(part_1(&input), 54321);

        let raw_input = read_input::read_lines("test3.txt").unwrap().pop().unwrap();
        let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        assert_eq!(part_1(&input), 65210);
    }

    #[test]
    fn test_amplify_part_2(){
        let raw_input = read_input::read_lines("test4.txt").unwrap().pop().unwrap();
        let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        let phases = vec![5,6,7,8,9];
        assert_eq!(
            amplify_part_2(&input, phases), 
            139629729
        );

        let raw_input = read_input::read_lines("test5.txt").unwrap().pop().unwrap();
        let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        let phases = vec![6,5,8,7,9];
        assert_eq!(
            amplify_part_2(&input, phases), 
            18216
        );
    }

    #[test]
    fn test_part_2() {
        let raw_input = read_input::read_lines("test4.txt").unwrap().pop().unwrap();
        let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        assert_eq!(
            part_2(&input),
            139629729
        );

        let raw_input = read_input::read_lines("test5.txt").unwrap().pop().unwrap();
        let input: Vec<i32> = raw_input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        assert_eq!(
            part_2(&input), 
            18216
        );
    }
}