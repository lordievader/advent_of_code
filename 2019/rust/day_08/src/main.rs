use std::collections::HashMap;
mod read_input;
mod timing;

fn part_1(input: &Vec<i32>, width: usize, height: usize) -> i32 {
    let mut index: usize = 0;
    let length = input.len();
    let pixels = width * height;
    let mut min_count = 0;
    let mut min_index = 0;
    let mut changed = false;
    while index < length {
        let count = input[index..index + pixels].iter().filter(|&n| *n == 0).count();
        if changed == false || count < min_count {
            min_count = count;
            min_index = index;
            changed = true;
        }
        index += pixels;
    }
    let ones = input[min_index..min_index + pixels].iter().filter(|&n| *n == 1).count();
    let twos = input[min_index..min_index + pixels].iter().filter(|&n| *n == 2).count();
    (ones * twos) as i32
}

fn part_2(input: &Vec<i32>, width: usize, height: usize) -> Vec<Vec<i32>> {
    
    let length = input.len();
    let mut index: usize = 0;
    
    let mut image: Vec<Vec<i32>> = Vec::new();
    for _ in 0..height {
        image.push(vec![2; width]);
    }
    
    while index < length {
        let x = index % width;
        let y = (index / width) % height;
        if image[y][x] == 2 {
            let color = input[index];
            if color != 2 {
                image[y][x] = color;
            }
        }
        index += 1;
    }
    image
}

fn main() {
    let raw_input = read_input::read_lines("input.txt").unwrap().pop().unwrap();
    let input: Vec<i32> = raw_input.chars().map(|x| x.to_string().parse::<i32>().unwrap()).collect();

    let start_part_1 = timing::start();
    let part_1_answer = part_1(&input, 25, 6);
    timing::stop(start_part_1);
    println!("Part 1 answer: {}", part_1_answer);

    let start_part_2 = timing::start();
    let part_2_answer = part_2(&input, 25, 6);
    timing::stop(start_part_2);
    println!("Part 2 answer:");
    for line in part_2_answer.iter() {
        for item in line.iter() {
            if *item == 0 {
                print!(" ");
            }
            else {
                print!("+");
            }
        }
        println!("");
    }
}


mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        let raw_input = read_input::read_lines("test.txt").unwrap().pop().unwrap();
        let input: Vec<i32> = raw_input.chars().map(|x| x.to_string().parse::<i32>().unwrap()).collect();
        println!("{:?}", input);
        assert_eq!(part_1(&input, 3, 2), 1);
    }

    #[test]
    fn test_part_2() {
        let raw_input = read_input::read_lines("test2.txt").unwrap().pop().unwrap();
        let input: Vec<i32> = raw_input.chars().map(|x| x.to_string().parse::<i32>().unwrap()).collect();
        println!("{:?}", input);
        assert_eq!(part_2(&input, 2, 2), vec![vec![0, 1], vec![1, 0]]);
    }
}