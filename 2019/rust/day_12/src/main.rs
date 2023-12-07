mod read_input;
mod timing;
use std::fmt;
use std::collections::HashSet;

#[derive(Clone)]
struct Moon {
    pos_x: i32,
    pos_y: i32,
    pos_z: i32,
    vel_x: i32,
    vel_y: i32,
    vel_z: i32,
}

impl fmt::Display for Moon {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Moon: pos ({x:4}, {y:4}, {z:4}); vel: ({vx:4}, {vy:4}, {vz:4});",
         x=self.pos_x, y=self.pos_y, z=self.pos_z,
         vx=self.vel_x, vy=self.vel_y, vz=self.vel_z)
    }
}

impl Moon {
    fn gravity(&mut self, other: &Moon) {
        if self.pos_x > other.pos_x {
            self.vel_x -= 1;
        } 
        else if self.pos_x < other.pos_x {
            self.vel_x += 1;
        }

        if self.pos_y > other.pos_y {
            self.vel_y -= 1;
        } 
        else if self.pos_y < other.pos_y {
            self.vel_y += 1;
        }

        if self.pos_z > other.pos_z {
            self.vel_z -= 1;
        } 
        else if self.pos_z < other.pos_z {
            self.vel_z += 1;
        }
    }

    fn move_moon(&mut self) {
        self.pos_x += self.vel_x;
        self.pos_y += self.vel_y;
        self.pos_z += self.vel_z;
    }

    fn potential_energy(&self) -> i32 {
        self.pos_x.abs() + self.pos_y.abs() + self.pos_z.abs()
    }

    fn kinetic_energy(&self) -> i32 {
        self.vel_x.abs() + self.vel_y.abs() + self.vel_z.abs()
    }

    fn total_energy(&self) -> i32 {
        self.potential_energy() * self.kinetic_energy()
    }

    fn duplicate_pos(&mut self) -> bool {
        if self.vel_x == 0 && self.vel_y == 0 && self.vel_z == 0 {
            return true;
        }
        else {
            return false;
        }
    }
}

fn process_input(input: &Vec<String>) -> Vec<Moon> {
    let mut moons = Vec::new();
    for line in input {
        let components: Vec<&str> = line[1..line.len()-1].split(", ").collect();
        let x: i32 = components[0].split("=").last().unwrap().parse().unwrap();
        let y: i32 = components[1].split("=").last().unwrap().parse().unwrap();
        let z: i32 = components[2].split("=").last().unwrap().parse().unwrap();
        let moon = Moon{
            pos_x: x,
            pos_y: y,
            pos_z: z,
            vel_x: 0,
            vel_y: 0,
            vel_z: 0,
        };
        moons.push(moon);
    }
    moons
}

fn step(mut io: &Moon, mut europe: &Moon, mut ganymede: &Moon, mut callisto: &Moon) {
    io.gravity(&europe);
    io.gravity(&ganymede);
    io.gravity(&callisto);

    // europe.gravity(&io);
    // europe.gravity(&ganymede);
    // europe.gravity(&callisto);

    // ganymede.gravity(&io);
    // ganymede.gravity(&europe);
    // ganymede.gravity(&callisto);

    // callisto.gravity(&io);
    // callisto.gravity(&europe);
    // callisto.gravity(&ganymede);

    io.move_moon();
    europe.move_moon();
    ganymede.move_moon();
    callisto.move_moon();

    // (io, europe, ganymede, callisto)
}

fn part_1(input: &Vec<String>, num_steps: u16) -> i32 {
    let mut moons = process_input(&input);
    let mut callisto = moons.pop().unwrap();
    let mut ganymede = moons.pop().unwrap();
    let mut europe = moons.pop().unwrap();
    let mut io = moons.pop().unwrap();
    for _ in 0..num_steps {
        // println!("After {} steps:\n{}\n{}\n{}\n{}\n", index, io, europe, ganymede, callisto);
        // let result = step(io, europe, ganymede, callisto);
        // io = result.0;
        // europe = result.1;
        // ganymede = result.2;
        // callisto = result.3;
        step(&io, &europe, &ganymede, &callisto);
    }

    // println!("After {} steps:\n{}\n{}\n{}\n{}\n", 10, io, europe, ganymede, callisto);
    // println!("{} {} {} {}", io.total_energy(), europe.total_energy(), ganymede.total_energy(), callisto.total_energy());
    io.total_energy() + europe.total_energy() + ganymede.total_energy() + callisto.total_energy()
}

fn part_2(input: &Vec<String>) -> i64 {
    let mut moons = process_input(&input);
    let mut callisto = moons.pop().unwrap();
    let mut ganymede = moons.pop().unwrap();
    let mut europe = moons.pop().unwrap();
    let mut io = moons.pop().unwrap();
    let mut steps = 0;
    // let result = step(io, europe, ganymede, callisto);
    // io = result.0;
    // europe = result.1;
    // ganymede = result.2;
    // callisto = result.3;

    // println!("After {} steps:\n{}\n{}\n{}\n{}\n", steps, io, europe, ganymede, callisto);
    while !(io.duplicate_pos() && europe.duplicate_pos() && ganymede.duplicate_pos() && callisto.duplicate_pos()) {
        // let result = step(io, europe, ganymede, callisto);
        // io = result.0;
        // europe = result.1;
        // ganymede = result.2;
        // callisto = result.3;
        steps += 1;
    }
    // println!("After {} steps:\n{}\n{}\n{}\n{}\n", steps, io, europe, ganymede, callisto);
    
    steps * 2 + 2 
}

fn main() {
    let input = read_input::read_lines("input.txt").unwrap();

    let start_part_1 = timing::start();
    let part_1_answer = part_1(&input, 1000);
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
        assert_eq!(part_1(&input, 10), 179);

        let input = read_input::read_lines("test2.txt").unwrap();
        assert_eq!(part_1(&input, 100), 1940);
    }

    #[test]
    fn test_part2() {
        let input = read_input::read_lines("test.txt").unwrap();
        assert_eq!(part_2(&input), 2772);

        let input = read_input::read_lines("test2.txt").unwrap();
        assert_eq!(part_2(&input), 4686774924);
    }
}