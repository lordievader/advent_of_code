mod read_input;
mod timing;
use std::collections::HashMap;
use petgraph::Graph;
use petgraph::visit::Dfs;


#[derive(Debug)]
struct Entry<'t> {
    inside: &'t str,
    outside: &'t str,
}

fn part_1(input: &Vec<Entry>) -> i32 {
    //Build the graph, then find all the paths towards the origin.
    let mut graph = Graph::new();
    let mut node_map = HashMap::new();
    for entry in input.into_iter() {
        let inside_node;
        if !node_map.contains_key(entry.inside) {
            inside_node = graph.add_node(entry.inside);
            node_map.insert(entry.inside, inside_node.clone());
        }
        else{
            inside_node = *node_map.get(entry.inside).unwrap();
        }

        let outside_node;
        if !node_map.contains_key(entry.outside) {
            outside_node = graph.add_node(entry.outside);
            node_map.insert(entry.outside, outside_node.clone());
        }
        else{
            outside_node = *node_map.get(entry.outside).unwrap();
        }

        graph.add_edge(outside_node, inside_node, 1);
    }

    let mut total_count = 0;
    for node in node_map.keys() {
        let node_ref = *node_map.get(node).unwrap();
        let mut dfs = Dfs::new(&graph, node_ref);
        let mut count = 0;
        dfs.next(&graph);
        while let Some(_) = dfs.next(&graph) {
            count += 1;
        }
        total_count += count;
    }
    total_count
}

fn part_2(input: &Vec<Entry>) -> i32 {
    //Build the graph. Then build the path from YOU to the origin.
    //Build the path from SANTA to the origin, while checking if YOU shared an orbit step.
    let mut graph = Graph::new();
    let mut node_map = HashMap::new();
    for entry in input.into_iter() {
        let inside_node;
        if !node_map.contains_key(entry.inside) {
            inside_node = graph.add_node(entry.inside);
            node_map.insert(entry.inside, inside_node.clone());
        }
        else{
            inside_node = *node_map.get(entry.inside).unwrap();
        }

        let outside_node;
        if !node_map.contains_key(entry.outside) {
            outside_node = graph.add_node(entry.outside);
            node_map.insert(entry.outside, outside_node.clone());
        }
        else{
            outside_node = *node_map.get(entry.outside).unwrap();
        }

        graph.add_edge(outside_node, inside_node, 1);
    }

    let mut step_count = 0;
    let mut visits = HashMap::new();
    let you = *node_map.get("YOU").unwrap();
    let mut dfs = Dfs::new(&graph, you);
    while let Some(nx) = dfs.next(&graph) {
        visits.insert(graph[nx], step_count);
        step_count += 1;
    }

    let mut total_step_count = 0;
    let santa = *node_map.get("SAN").unwrap();
    dfs = Dfs::new(&graph, santa);
    while let Some(nx) = dfs.next(&graph) {
        if visits.contains_key(graph[nx]) {
            total_step_count += visits.get(graph[nx]).unwrap();
            break;
        }
        total_step_count += 1;
    }

    // Correct for the initial orbits (-2)
    total_step_count - 2 
}

fn main() {
    let raw_input = read_input::read_lines("input.txt").unwrap();
    let input = raw_input.iter().map(|x| {
            let split = x.split(")").collect::<Vec<&str>>();
            Entry {
                inside: split.first().unwrap(),
                outside: split.last().unwrap(),
            }
        })
        .collect::<Vec<Entry>>();

    let start_part_1 = timing::start();
    let part_1_answer = part_1(&input);
    timing::stop(start_part_1);
    println!("Part 1 answer: {}", part_1_answer);

    let start_part_2 = timing::start();
    let part_2_answer = part_2(&input);
    timing::stop(start_part_2);
    println!("Part 2 answer: {}", part_2_answer);
}
