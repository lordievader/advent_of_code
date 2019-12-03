mod read_input;
mod timing;

fn add(input: &Vec<i32>, index: usize) -> Vec<i32> {
    let mut output = input.to_vec();
    let a = output[output[(index + 1) as usize] as usize];
    let b = output[output[(index + 2) as usize] as usize];
    let outcome_location = input[(index + 3) as usize];
    output[outcome_location as usize] = a + b;
    output
}

fn mul(input: &Vec<i32>, index: usize) -> Vec<i32> {
    let mut output = input.to_vec();
    let a = output[output[(index + 1) as usize] as usize];
    let b = output[output[(index + 2) as usize] as usize];
    let outcome_location = input[(index + 3) as usize];
    output[outcome_location as usize] = a * b;
    // println!("{} * {} = {} -- {:?}", a, b, a * b, output);
    output
}

fn execute(input: &Vec<i32>) -> Vec<i32> {
    let length = input.len();
    let mut output = input.to_vec();
    for index in (0..length).step_by(4) {
        let opcode = output[index];
        if opcode == 99 {
            break;
        }
        output = match opcode {
            1 => add(&output, index),
            2 => mul(&output, index),
            _ => output,
        };
        // println!("Index: {}, opcode: {} -- {:?}", index, opcode, output);
    }
    output
}

fn part_1(input: &Vec<i32>) -> i32 {
    let mut input_mod: Vec<i32> = input.to_vec();
    input_mod[1] = 12;
    input_mod[2] = 2;
    let output = execute(&input_mod);
    // println!("Last state: {:?}", output);
    output[0]
}

fn part_2(input: &Vec<i32>) -> i32 {
    let mut output: Vec<i32> = execute(&input);
    let mut noun = 0;
    let mut verb = 0;
    for x in 0..99 {
        for y in 0..99 {
            let mut input_mod: Vec<i32> = input.to_vec();
            input_mod[1] = x;
            input_mod[2]= y;
            output = execute(&input_mod);
            if output[0] == 19690720 {
                verb = y;
                break;
            }
        }
        if output[0] == 19690720 {
            noun = x;
            break;
        }
    }
    100 * noun + verb
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
    fn test_add() {
        assert_eq!(add(&vec![1, 0, 0, 0, 99], 0), vec![2, 0, 0, 0, 99]);
    }

    #[test]
    fn test_mul(){
        assert_eq!(mul(&vec![2, 3, 0, 3, 99], 0), vec![2, 3, 0, 6, 99]);
    }

    #[test]
    fn test_execute(){
        assert_eq!(execute(&vec![1, 0, 0, 0, 99]), vec![2, 0, 0, 0, 99]);
        assert_eq!(execute(&vec![2, 3, 0, 3, 99]), vec![2, 3, 0, 6, 99]);
        assert_eq!(execute(&vec![2, 4, 4, 5, 99, 0]), vec![2, 4, 4, 5, 99, 9801]);
        assert_eq!(execute(&vec![1, 1, 1, 4, 99, 5, 6, 0, 99]), vec![30, 1, 1, 4, 2, 5, 6, 0, 99]);
    }
}