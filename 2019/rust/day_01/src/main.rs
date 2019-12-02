mod read_input;
mod timing;

fn required_fuel(mass: i32) -> i32 {
    let fuel = (mass / 3) - 2;
    fuel
}

fn required_fuel_part_2(mass: i32) -> i32 {
    let mut total_fuel: Vec<i32> = Vec::new();
    let fuel = required_fuel(mass);
    let mut left = fuel;
    total_fuel.push(fuel);
    while left > 0 {
        let extra_fuel = required_fuel(left);
        if extra_fuel <= 0 {
            break;
        }
        else {
            total_fuel.push(extra_fuel);
            left = extra_fuel;
        }
        
    }
    total_fuel.into_iter().sum()
}

fn part_1(input: &Vec<String>) -> i32 {
    let mut fuel: Vec<i32> = Vec::new();
    for mass in input.into_iter() {
        fuel.push(required_fuel(mass.parse::<i32>().unwrap()));
    }
    fuel.into_iter().sum()
}

fn part_2(input: &Vec<String>) -> i32 {
    let mut fuel: Vec<i32> = Vec::new();
    for mass in input.into_iter() {
        fuel.push(required_fuel_part_2(mass.parse::<i32>().unwrap()));
    }
    fuel.into_iter().sum()
}

fn main() {
    let input = read_input::read_lines("input.txt").unwrap();
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
    fn test_required_fuel() {
        assert_eq!(required_fuel(12), 2);
        assert_eq!(required_fuel(14), 2);
        assert_eq!(required_fuel(1969), 654);
        assert_eq!(required_fuel(100756), 33583);
    }

    #[test]
    fn test_required_fuel_part_2() {
        assert_eq!(required_fuel_part_2(14), 2);
        assert_eq!(required_fuel_part_2(1969), 966);
        assert_eq!(required_fuel_part_2(100756), 50346);
    }
}