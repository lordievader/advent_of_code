use std::collections::HashSet;
use std::collections::HashMap;
mod read_input;
mod timing;

fn up(x: i32, y: i32, instruction: &str, past: &mut HashMap<(i32, i32), i32>, mut steps: i32) -> (i32, i32, i32) {
    let amount = &String::from(instruction)[1..].parse::<i32>().unwrap();
    for index in 0..(*amount as i32) {
        past.insert((x, y + index), steps);
        steps += 1;
    }
    (x, y + amount, steps)
}

fn down(x: i32, y: i32, instruction: &str, past: &mut HashMap<(i32, i32), i32>, mut steps: i32) -> (i32, i32, i32) {
    let amount = &String::from(instruction)[1..].parse::<i32>().unwrap();
    for index in 0..(*amount as i32) {
        past.insert((x, y - index), steps);
        steps += 1;
    }
    (x, y - amount, steps)
}

fn left(x: i32, y: i32, instruction: &str, past: &mut HashMap<(i32, i32), i32>, mut steps: i32) -> (i32, i32, i32) {
    let amount = &String::from(instruction)[1..].parse::<i32>().unwrap();
    for index in 0..(*amount as i32) {
        past.insert((x - index, y), steps);
        steps += 1;
    }
    (x - amount, y, steps)
}

fn right(x: i32, y: i32, instruction: &str, past: &mut HashMap<(i32, i32), i32>, mut steps: i32) -> (i32, i32, i32) {
    let amount = &String::from(instruction)[1..].parse::<i32>().unwrap();
    for index in 0..(*amount as i32) {
        past.insert((x + index, y), steps);
        steps += 1;
    }
    (x + amount, y, steps)
}

fn wire(instructions: Vec<&str>) -> HashMap<(i32, i32), i32> {
    let mut past: HashMap<(i32, i32), i32> = HashMap::new();
    let mut x = 0;
    let mut y = 0;
    let mut steps = 0;
    for instruction in instructions.into_iter() {
        let opcode = instruction.chars().next().unwrap();
        let coordinates = match opcode {
            'U' => up(x, y, instruction, &mut past, steps),
            'D' => down(x, y, instruction, &mut past, steps),
            'L' => left(x, y, instruction, &mut past, steps),
            'R' => right(x,y, instruction, &mut past, steps),
            _ => (x, y, steps),
        };
        x = coordinates.0;
        y = coordinates.1;
        steps = coordinates.2;
    }
    past
}

fn construct_wires(input: &Vec<String>) -> Vec<HashMap<(i32, i32), i32>> {
    let mut wires: Vec<HashMap<(i32, i32), i32>> = Vec::new();
    for line in input.into_iter() {
        let instructions = line.split(",").collect::<Vec<&str>>();
        let past = wire(instructions);
        wires.push(past);
    }
    wires
}

fn crossing_wires(wires: &Vec<HashMap<(i32, i32), i32>>) -> HashSet<(i32, i32)> {
    let wire_a: HashSet<(i32, i32)> = wires[0].keys().cloned().collect();
    let wire_b: HashSet<(i32, i32)> = wires[1].keys().cloned().collect();
    let intersection: HashSet<_> = wire_a.intersection(&wire_b).cloned().collect();
    intersection
}

fn closest(past: &HashSet<(i32, i32)>) -> i32 {
    let mut min_distance = 0;
    for coordinates in past.into_iter(){
        if coordinates.0 == 0 && coordinates.1 == 0 {
            continue;
        }
        let distance = coordinates.0.abs() + coordinates.1.abs();
        if distance < min_distance || min_distance == 0 {
            min_distance = distance;
        }
    }
    min_distance
}

fn least_steps(wires: &Vec<HashMap<(i32, i32), i32>>, intersection: &HashSet<(i32, i32)>) -> i32 {
    let mut min_steps = 0;
    for coordinates in intersection.into_iter() {
        if coordinates.0 == 0 && coordinates.1 == 0 {
            continue;
        }
        let steps_a = wires[0].get(coordinates).unwrap();
        let steps_b = wires[1].get(coordinates).unwrap();
        let total_steps = steps_a + steps_b;
        if total_steps < min_steps || min_steps == 0 {
            min_steps = total_steps;
        }
    }
    min_steps
}

fn main() {
    let input = read_input::read_lines("input.txt").unwrap();

    let start_part_1 = timing::start();
    let wires = construct_wires(&input);
    let intersection = crossing_wires(&wires);
    let part_1_answer = closest(&intersection);
    timing::stop(start_part_1);
    println!("Part 1 answer: {}", part_1_answer);

    let start_part_2 = timing::start();
    let part_2_answer = least_steps(&wires, &intersection);
    timing::stop(start_part_2);
    println!("Part 2 answer: {}", part_2_answer);
}

mod tests{
    use super::*;

    #[test]
    fn test_up() {
        let x = 0;
        let y = 0;
        let steps = 0;
        let instruction: &str = &String::from("U42");
        let mut past: HashMap<(i32, i32), i32> = HashMap::new();
        let (x, y, _) = up(x, y, instruction, &mut past, steps);
        assert_eq!(x, 0);
        assert_eq!(y, 42);
        for index in 0..42 {
            assert!(past.contains_key(&(0, index)));
            assert_eq!(past.get(&(0, index)), Some(&index));
        }
    }

    #[test]
    fn test_down() {
        let x = 0;
        let y = 0;
        let steps = 0;
        let instruction: &str = &String::from("D42");
        let mut past: HashMap<(i32, i32), i32> = HashMap::new();
        let (x, y, _) = down(x, y, instruction, &mut past, steps);
        assert_eq!(x, 0);
        assert_eq!(y, -42);
        for index in 0..42 {
            assert!(past.contains_key(&(0, -index)));
            assert_eq!(past.get(&(0, -index)), Some(&index));
        }
    }

    #[test]
    fn test_left() {
        let x = 0;
        let y = 0;
        let steps = 0;
        let instruction: &str = &String::from("L42");
        let mut past: HashMap<(i32, i32), i32> = HashMap::new();
        let (x, y, _) = left(x, y, instruction, &mut past, steps);
        assert_eq!(x, -42);
        assert_eq!(y, 0);
        for index in 0..42 {
            assert!(past.contains_key(&(-index, 0)));
            assert_eq!(past.get(&(-index, 0)), Some(&index));
        }
    }

    #[test]
    fn test_right() {
        let x = 0;
        let y = 0;
        let steps = 0;
        let instruction: &str = &String::from("R42");
        let mut past: HashMap<(i32, i32), i32> = HashMap::new();
        let (x, y, _) = right(x, y, instruction, &mut past, steps);
        assert_eq!(x, 42);
        assert_eq!(y, 0);
        for index in 0..42 {
            assert!(past.contains_key(&(index, 0)));
            assert_eq!(past.get(&(index, 0)), Some(&index));
        }
    }

    #[test]
    fn test_wire() {
        let mut instructions: Vec<&str> = Vec::new();
        let u = String::from("U01");
        let d = String::from("D01");
        let l = String::from("L01");
        let r = String::from("R01");
        instructions.push(&u);
        instructions.push(&r);
        instructions.push(&d);
        instructions.push(&l);
        

        let past = wire(instructions);
        assert!(past.contains_key(&(0, 0)));
        assert!(past.contains_key(&(0, 1)));
        assert!(past.contains_key(&(1, 0)));
        assert!(past.contains_key(&(1, 1)));
    }

    #[test]
    fn test_closest() {
        let mut past: HashSet<(i32, i32)> = HashSet::new();
        past.insert((0, 0));
        past.insert((6, 5));
        past.insert((3, 3));
        assert_eq!(closest(&past), 6);
    }
}