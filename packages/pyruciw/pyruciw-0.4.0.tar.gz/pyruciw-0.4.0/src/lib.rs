use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::cmp::Reverse;

#[pyclass]
#[derive(Debug, PartialEq, PartialOrd, Clone)]
enum EventType {
    Arrival,
    Service,
}

#[pyclass]
#[derive(Debug, PartialEq, PartialOrd, Clone)]
struct Event {
    #[pyo3(get, set)]
    time: f64,
    #[pyo3(get, set)]
    event_type: EventType,
}

#[pymethods]
impl Event {
    #[new]
    fn new(time: f64, event_type: EventType) -> Self {
        Self { time, event_type }
    }
}

impl Eq for Event {}

impl Ord for Event {
    fn cmp(&self, other: &Self) -> Ordering {
        self.partial_cmp(other).unwrap_or(Ordering::Equal)
    }
}

#[pyclass]
struct Environment {
    event_queue: BinaryHeap<Reverse<Event>>,
    clock: f64,
    queue_length: usize,
}

#[pymethods]
impl Environment {
    #[new]
    fn new() -> Self {
        Self {
            event_queue: BinaryHeap::new(),
            clock: 0.0,
            queue_length: 0,
        }
    }

    fn schedule_event(&mut self, event: Event) {
        self.event_queue.push(Reverse(event));
    }

    fn run_until(&mut self, end_time: f64) {
        while let Some(Reverse(current_event)) = self.event_queue.pop() {
            if current_event.time < end_time {
                self.clock = current_event.time;
                current_event.execute(self);
            } else {
                self.clock = end_time;
                break;
            }
        }
    }

    fn now(&self) -> f64 {
        self.clock
    }

    fn get_queue_length(&self) -> usize {
        self.queue_length
    }
}

impl Event {
    fn execute(&self, env: &mut Environment) {
        match self.event_type {
            EventType::Arrival => {
                env.queue_length += 1;
                let service_time = 2.0;
                env.schedule_event(Event::new(self.time + service_time, EventType::Service));
            }
            EventType::Service => {
                if env.queue_length > 0 {
                    env.queue_length -= 1;
                }
            }
        }
    }
}

#[pyfunction]
fn simulate_queue(arrival_rate: f64, _service_rate: f64, end_time: f64) -> Vec<usize> {
    let mut env = Environment::new();
    let mut lengths = Vec::new();
    let mut time = 0.0;

    while time < end_time {
        env.schedule_event(Event::new(time, EventType::Arrival));
        time += arrival_rate;
    }

    env.run_until(end_time);

    lengths.push(env.get_queue_length());

    lengths
}


#[pymodule]
#[pyo3(name="pyruciw")]
fn pyruciw(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Environment>()?;
    m.add_class::<Event>()?;
    m.add_class::<EventType>()?;
    m.add_function(wrap_pyfunction!(simulate_queue, m)?)?;
    Ok(())
}

