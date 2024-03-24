/**
 * FCFS scheduling algorithm.
 */
 
import java.util.List;

public class FCFS implements Algorithm {
// Queue holding all tasks to be scheduled.
    private List<Task> queue;

    public FCFS(List<Task> queue) {
        this.queue = queue;
    }

    @Override
    public void schedule() {
    // Loop through and process each task in the order they are in the queue.
        for (Task task : queue) {
        // Run each task on the CPU for its entire burst time.
            CPU.run(task, task.getBurst());
            System.out.println("Task finished: " + task.getName() + "\n");
        }
    }

    @Override
    public Task pickNextTask() {
    // Check if the queue is empty. If empty, return null; otherwise, remove and return the first task in the queue.
        return queue.isEmpty() ? null : queue.remove(0);
    }
}