/**
 
Non-preemptive priority scheduling algorithm.
*/
import java.util.Comparator;
import java.util.Collections;
import java.util.List;

public class Priority implements Algorithm {
    // Queue holding all tasks to be scheduled.
    private List<Task> queue;

    public Priority(List<Task> queue) {
        this.queue = queue;
        // Sort the tasks based on priority in a descending order
        Collections.sort(queue, Collections.reverseOrder(Comparator.comparing(Task::getPriority)));
    }

    @Override
    public void schedule() {
        // Loop through and process each task based on priority order.
        for (Task task : queue) {
            // Run each task on the CPU for its entire burst time and print when its finished
            CPU.run(task, task.getBurst());
            System.out.println("Task finished: " + task.getName() + "\n");
        }
    }

    @Override
    public Task pickNextTask() {
        // Check if the queue is empty. If empty, return null otherwise remove and return the first (highest priority) task in the queue.
        return queue.isEmpty() ? null : queue.remove(0);
    }
}
