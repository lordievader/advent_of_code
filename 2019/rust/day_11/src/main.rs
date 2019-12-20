mod read_input;
mod timing;
mod intcode;
use std::fmt;
use std::cmp::max;
use std::cmp::min;
use std::collections::HashSet;


struct Robot {
    direction: char,
    x: usize,
    y: usize,
    paint: i64,
    turn: i64,
    paint_count: i64,
}

impl fmt::Display for Robot {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Robot: paints {paints}, x: {x}, y: {y}",
         paints=self.paint_count, x=self.x, y=self.y)
    }
}

impl Robot {
    fn run_program(&mut self, mut program: intcode::Amp, input_value: i64) -> intcode::Amp {
        program.input_values.push(input_value);
        program = intcode::execute(program);
        self.paint = program.output_value;
        program = intcode::execute(program);
        self.turn = program.output_value;
        program
    }

    fn turn(&mut self) {
        if self.turn == 0 { // turn left
            self.direction = match self.direction{
                'u' => 'l',
                'l' => 'd',
                'd' => 'r',
                'r' => 'u',
                _ => 'u',
            }
        }
        else { // turn right
            self.direction = match self.direction{
                'u' => 'r',
                'r' => 'd',
                'd' => 'l',
                'l' => 'u',
                _ => 'u',
            }
        }
    }

    fn move_robot(&mut self) {
        let (x, y) = match self.direction {
            'u' => (self.x + 0, self.y + 1),
            'd' => (self.x + 0, self.y - 1),
            'r' => (self.x + 1, self.y + 0),
            'l' => (self.x - 1, self.y + 0),
            _ => (self.x, self.y),
        };
        self.x = x;
        self.y = y;
    }

    fn run(&mut self, mut grid: Vec<Vec<u8>>, mut program: intcode::Amp) -> (usize, Vec<Vec<u8>>) {
        let mut x1 = self.x;
        let mut x2 = self.x;
        let mut y1 = self.y;
        let mut y2 = self.y;
        let mut coordinates = HashSet::new();
        while program.finished != 1 {
            let sensor_value = grid[self.y][self.x] as i64;
            program = self.run_program(program, sensor_value);
            if self.paint != sensor_value {
                self.paint_count += 1;
                grid[self.y][self.x] = self.paint as u8;
            }
            coordinates.insert((self.x, self.y));
            self.turn();
            self.move_robot();
            x1 = min(self.x, x1);
            x2 = max(self.x, x2);
            y1 = min(self.y, y1);
            y2 = max(self.y, y2);
        }
        print_grid(&grid, x1, x2, y1, y2);
        (coordinates.len(), grid)
    }
}

fn print_grid(grid: &Vec<Vec<u8>>, x1: usize, x2: usize, y1: usize, y2: usize){
    let mut output = Vec::new();
    for y in y1..y2{
        let mut line_output = Vec::new();
        for x in x1..x2 {
            if grid[y][x] == 0 {
                line_output.push(" ");
            }
            else{
                line_output.push("█");
            }
        }
        output.push(line_output.join(""));
    }
    println!("{}\n", output.join("\n"));
}

fn part_1(input: &Vec<i64>) -> usize {
    // 100 x 100 grid, index 0,0  is the middle i.e. 50, 50;
    let size = 100;
    let mut grid: Vec<Vec<u8>> = Vec::new();
    for _ in 0..size {
        grid.push(vec![0; size])
    }
    let program = intcode::Amp{
        state: input.to_vec(),
        index: 0,
        input_values: vec![],
        output_value: 0,
        finished: 0,
        relative_base: 0,
    };
    let mut robot = Robot{
        x: (size / 2) as usize,
        y: (size / 2) as usize,
        direction: 'u',
        paint: 0,
        turn: 0,
        paint_count: 0
    };
    let (unique_locations, grid) = robot.run(grid, program);
    unique_locations - 1
}

fn part_2(input: &Vec<i64>) -> usize {
    // 100 x 100 grid, index 0,0  is the middle i.e. 50, 50;
    let size = 100;
    let mut grid: Vec<Vec<u8>> = Vec::new();
    for _ in 0..size {
        grid.push(vec![0; size])
    }
    grid[size/2][size/2] = 1;
    let program = intcode::Amp{
        state: input.to_vec(),
        index: 0,
        input_values: vec![],
        output_value: 0,
        finished: 0,
        relative_base: 0,
    };
    let mut robot = Robot{
        x: (size / 2) as usize,
        y: (size / 2) as usize,
        direction: 'u',
        paint: 0,
        turn: 0,
        paint_count: 0
    };
    let (unique_locations, grid) = robot.run(grid, program);
    unique_locations - 1
}

fn main() {
    let raw_input = read_input::read_lines("input.txt").unwrap().pop().unwrap();
    let input: Vec<i64> = raw_input.split(",").map(|x| x.parse::<i64>().unwrap()).collect();
    // println!("{:?}", input);

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