use std::collections::HashMap;
use std::cmp::Ordering;
use std::f64::consts::PI;
mod read_input;
mod timing;

#[derive(Hash, Debug, Eq, Clone)]
struct Coordinates {
    x: i32,
    y: i32,
    distance: i32,
}

impl Ord for Coordinates {
    fn cmp(&self, other: &Self) -> Ordering {
        other.distance.cmp(&self.distance)
    }
}

impl PartialOrd for Coordinates {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Coordinates {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}

fn print_results(results: HashMap<&Coordinates, usize>) {
    for y in 0..15 {
        for x in 0..15 {
            let key = Coordinates{x: x as i32, y: y as i32, distance: 0};
            if results.contains_key(&key) {
                print!("{:4}|", results.get(&key).unwrap());
            }
            else{
                print!("    |");
            }
        }
        println!("");
    }
}

fn find_asteroids(input: &Vec<String>) -> Vec<Coordinates> {
    let mut asteroids = Vec::new();
    for (y, line) in input.iter().enumerate() {
        for (x, point) in line.chars().enumerate() {
            if point == '#' {
                let coordinates = Coordinates{x: x as i32, y: y as i32, distance: 0};
                asteroids.push(coordinates);
            }
        }
    }
    asteroids
}

fn find_max_pos(asteroids: Vec<Coordinates>) -> (Coordinates, usize){
    let mut position = Coordinates{x: 0, y: 0, distance: 0};
    let mut max_seen = 0;
    for coordinates in asteroids.iter() {
        let mut seen = Vec::new();
        for subcoordinates in asteroids.iter() {
            if coordinates == subcoordinates {
                 continue
            }
            
            let diff_x = (coordinates.x - subcoordinates.x) as f64;
            let diff_y = (coordinates.y - subcoordinates.y) as f64;
            let degrees: f64 = diff_x.atan2(diff_y);
            // println!("{:?} -> {:?} = {}", coordinates, subcoordinates, degrees * 180.0 / PI);
            if !seen.contains(&degrees) {
                seen.push(degrees);
            }
        }
        if seen.len() > max_seen {
            max_seen = seen.len();
            position = coordinates.clone();
        }
    }
    (position, max_seen)
}

fn part_1(input: &Vec<String>) -> usize {
    let asteroids = find_asteroids(input);
    let (_, max_seen) = find_max_pos(asteroids);
    max_seen
}

fn part_2(input: &Vec<String>) -> i32 {
    let asteroids = find_asteroids(input);
    let mut seen = HashMap::new();
    let mut degrees_list = Vec::new();
    let (coordinates, _) = find_max_pos(asteroids.clone());
    // println!("MAX at: {:?}", coordinates);
    for subcoordinates in asteroids.iter() {
        if &coordinates == subcoordinates {
                continue
        }
        let diff_x = (coordinates.x - subcoordinates.x) as f64;
        let diff_y = (coordinates.y - subcoordinates.y) as f64;
        let mut degrees = (-100.0 * (diff_x.atan2(diff_y) * 180.0 / PI)) as i32;
        if degrees < 0 {
            degrees += 36000;
        }
        let mut position = subcoordinates.clone();
        position.distance = diff_x.abs() as i32 + diff_y.abs() as i32;
        seen.entry(degrees).or_insert(Vec::new()).push(position);
        if !degrees_list.contains(&degrees) {
            degrees_list.push(degrees);
        }
    }

    for (_, value) in seen.iter_mut() {
        value.sort();
    }
    degrees_list.sort();
    let mut index = 0;
    let mut winner: Coordinates = Coordinates{x: 0, y: 0, distance: 0};
    while index != 200 {
        for key in degrees_list.iter() {
            let value = seen.get_mut(&key).unwrap();
            if value.len() > 0 {
                winner = value.pop().unwrap();
                // println!("index: {} deg:{} -> {:?}", index, key, winner);
                index += 1;
                if index == 200 {
                    break;
                }
            }
        }
    }
    // println!("{:?}", winner);
    winner.x * 100 + winner.y
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
    fn test_part1() {
        let input = read_input::read_lines("test.txt").unwrap();
        assert_eq!(part_1(&input), 8);
        println!("");

        // let input = read_input::read_lines("test2.txt").unwrap();
        // assert_eq!(part_1(&input), 33);
        // println!("");

        // let input = read_input::read_lines("test3.txt").unwrap();
        // assert_eq!(part_1(&input), 35);
        // println!("");

        // let input = read_input::read_lines("test4.txt").unwrap();
        // assert_eq!(part_1(&input), 41);
        // println!("");

        // let input = read_input::read_lines("test5.txt").unwrap();
        // assert_eq!(part_1(&input), 210);
        // println!("");
    }

    #[test]
    fn test_part2(){
        let input = read_input::read_lines("test5.txt").unwrap();
        assert_eq!(part_2(&input), 802);
        println!("");
    }
}
