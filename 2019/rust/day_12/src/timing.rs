use std::time::Instant;

pub fn start() -> Instant {
    Instant::now()
}

pub fn stop(start: Instant) {
    let duration = start.elapsed();
    println!("Time elapsed is: {:?}", duration);
}